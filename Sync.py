import json

import requests

from .Base import BaseTR
from .Const import BASE_URL_POST  #, BASE_URL_WEBSOCKET, BASE_URL_WEBSOCKET_FOR_TEST


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
            if isinstance(rp['body'][sub_outblock_nm], dict): continue
            else:
                body[sub_outblock_nm] = rp['body'][sub_outblock_nm] + body[sub_outblock_nm]

    return body


