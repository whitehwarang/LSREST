import json

import requests
from aiohttp import ClientSession
import websockets

from .Base import BaseTR, BaseWS
from const import BASE_URL_POST  #, BASE_URL_WEBSOCKET, BASE_URL_WEBSOCKET_FOR_TEST


def _post(tr_inst:BaseTR, test_print=False) -> dict:
    """ 동기식으로 tr을 request(post)한다. """
    if test_print:
        print(tr_inst.header)
        print(tr_inst.body)
    rp = requests.post(url=BASE_URL_POST+tr_inst.Url, 
                       headers=getattr(tr_inst, 'header', None), 
                       params=getattr(tr_inst, 'params', None), 
                       data=json.dumps(getattr(tr_inst, 'body', None)),
                       )
    header : dict = rp.headers
    body : dict = json.loads(rp.content)
    if test_print:
        print(header)
        print(body)
    return {'header': header, 'body': body}


def rq_tr(tr_inst:BaseTR) -> dict:
    """ 동기식으로 tr을 request한다. """
    tr_inst.keep_limit()
    tr_inst.incr_cnt()
    rp : dict = _post(tr_inst)
    body : dict = rp['body']

    # 연속 조회 루틴
    while rp['header'].get('tr_cont') == 'Y':

        # header setting
        tr_inst.header['tr_cont'] = rp['header'].get('tr_cont') or "N"
        tr_inst.header['tr_cont_key'] = rp['header'].get('tr_cont_key') or ""

        # block name setting
        _inblock_nm : str = f"{tr_inst.TRCode}InBlock"
        _outblock_nms : tuple = tuple(key for key in body.keys() if "OutBlock" in key)
        if not _outblock_nms: break  # OutBlock 없으면 연속조회 루틴 탈출
        _main_outblock_nm : str = min(_outblock_nms)

        # body setting
        _cts_dict : dict = {k: v for k, v in body.get(_main_outblock_nm).items() if k.startswith('cts_')}
        tr_inst.body[_inblock_nm].update(_cts_dict)

        # re-request(post)
        tr_inst.keep_limit()
        tr_inst.incr_cnt()
        rp : dict = _post(tr_inst)
        
        # append re-requested data to previously requested data.
        for sub_outblock_nm in _outblock_nms:
            if sub_outblock_nm == _main_outblock_nm: continue
            body[sub_outblock_nm] = rp['body'][sub_outblock_nm] + body[sub_outblock_nm]

    return body


async def _async_post(session:ClientSession, tr_inst:BaseTR, test_print:bool=False) -> dict:
    """ 비동기로 tr을 request(post) 한다. """
    if test_print:
        print(tr_inst.header)
        print(tr_inst.body)
    async with session.post(url=tr_inst.Url,
                            headers=getattr(tr_inst, 'header', None),
                            params=getattr(tr_inst, 'params', None),
                            data=json.dumps(getattr(tr_inst, 'body', None))
                            ) as rp:
        body : dict = await rp.json()
        header : dict = rp.headers
        if test_print:
            print(header)
            print(body)
    return {'header': header, 'body': body}


class AsyncNoOutBlockReceivedError(Exception): pass


async def async_rq_tr(session:ClientSession, tr_inst:BaseTR) -> dict:
    """ 비동기로 tr을 request(요청)한다."""
    await tr_inst.async_keep_limit()
    await tr_inst.async_incr_cnt()
    rp : dict = await _async_post(session, tr_inst)
    body : dict = rp['body']

    # 연속조회 루틴
    while rp['header'].get('tr_cont') == 'Y':
        # 연속조회를 위해 monkey patch하여 re-request(post)

        # header setting
        tr_inst.header['tr_cont'] = rp['header'].get('tr_cont') or "N"
        tr_inst.header['tr_cont_key'] = rp['header'].get('tr_cont_key') or ""

        # block name setting
        _inblock_nm: str = f"{tr_inst.TRCode}InBlock"
        _outblock_nms: tuple = tuple(key for key in body.keys() if "OutBlock" in key)
        if not _outblock_nms: break  # OutBlock 없으면 연속조회 루틴 탈출
        _main_outblock_nm :str = min(_outblock_nms)

        # body setting
        _cts_dict : dict = {k: v for k, v in body.get(_main_outblock_nm).items() if k.startswith('cts_')}
        tr_inst.body[_inblock_nm].update(_cts_dict)

        # re-request
        await tr_inst.async_keep_limit()
        await tr_inst.async_incr_cnt()
        rp : dict = await _async_post(session, tr_inst)
        
        # check whether all OutBlocks were received. if not, re-request.
        if any(sub_outblock_nm not in rp['body'] for sub_outblock_nm in _outblock_nms):
            #print('Re-Requested!!!')
            await tr_inst.async_keep_limit()
            await tr_inst.async_incr_cnt()
            rp : dict = await _async_post(session, tr_inst)
        
        # if all OutBlocks were not received two times consecutively, raise error.
        if any(sub_outblock_nm not in rp['body'] for sub_outblock_nm in _outblock_nms):
            raise AsyncNoOutBlockReceivedError

        # append re-requested data to the previously one.
        for sub_outblock_nm in _outblock_nms:
            if sub_outblock_nm == _main_outblock_nm: continue
            body[sub_outblock_nm] = rp['body'][sub_outblock_nm] + body[sub_outblock_nm]
            
    return body


async def connect_ws(ws_inst:BaseWS, callback:function=print) -> None:
    """ 웹 소켓에 접속하여 실시간 정보 수신 및 처리 """

    async with websockets.connect(ws_inst.Url) as ws:
        # 웹 소켓 서버로 데이터를 전송한다.
        s : str = json.dumps(ws_inst.into_dict())
        await ws.send(s)
        ws_inst.connect()

        # 웹 소켓 서버로부터 메시지가 오면 처리한다.
        while ws_inst.connection:
            rcvd_string : str = await ws.recv()
            data : dict = json.loads(rcvd_string)
            callback(data)
        else:   # 웹 소켓 서버 접속을 끊었을 때(disconnect())의 처리.
            ws_inst.disconnect()
            ws_inst.switch_unreg()
            s : str = json.dumps(ws_inst.into_dict())
            await ws.send(s)
