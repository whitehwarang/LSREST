from .. import Stock, Async, Sync


async def timely_stock_chegyuel(session, 
                                token:str,
                                shcode:str,
                                cvolume:int,
                                starttime:str,
                                endtime:str):
    tr_inst = Stock.t1301(token=token,
                          shcode=shcode,
                          cvolume=cvolume,
                          starttime=starttime,
                          endtime=endtime,
                          cts_time="",
                          )
    return await Async.async_rq_tr(session, tr_inst)


async def daily_chart(session, 
                      token:str, 
                      shcode:str,
                      qrycnt:int,
                      sdate:str, 
                      edate:str, 
                      sujung:str="Y"):
    tr_inst = Stock.t8410(token=token, 
                          shcode=shcode, 
                          gubun=Stock.t8410.GUBUN.DAILY,
                          qrycnt=qrycnt,
                          sdate=sdate,
                          edate=edate,
                          sujung=sujung
                          )
    return await Async.async_rq_tr(session, tr_inst)


async def minutely_chart(session, 
                         token:str, 
                         shcode:str,
                         ncnt:int,
                         qrycnt:int,
                         sdate:str,
                         stime:str,
                         edate:str,
                         etime:str):
    tr_inst = Stock.t8412(token=token,
                          shcode=shcode,
                          ncnt=ncnt,
                          qrycnt=qrycnt,
                          sdate=sdate,
                          stime=stime,
                          edate=edate,
                          etime=etime,
                          )
    return await Async.async_rq_tr(session, tr_inst)


async def market_buy_order(session, 
                           token:str,
                           code7:str,
                           quantity:int):
    tr_inst = Stock.CSPAT00601(token=token,
                               IsuNo=code7,
                               OrdQty=quantity,
                               OrdPrc=0.0,
                               BnsTpCode=Stock.Order.BNSTPCODE.BUY,
                               OrdprcPtnCode=Stock.Order.ORDPRCPTNCODE.MARKET,
                               MgntrnCode=Stock.Order.MGNTRNCODE.NORMAL,
                               OrdCndiTpCode=Stock.Order.ORDCNDITPCODE.NONE,
                               )
    return await Async.async_rq_tr(session, tr_inst)


async def specific_buy_order(session,
                             token:str,
                             code7:str,
                             quantity:int,
                             price:float):
    tr_inst = Stock.CSPAT00601(token=token,
                               IsuNo=code7,
                               OrdQty=quantity,
                               OrdPrc=price,
                               BnsTpCode=Stock.Order.BNSTPCODE.BUY,
                               OrdprcPtnCode=Stock.Order.ORDPRCPTNCODE.SPECIFIC,
                               MgntrnCode=Stock.Order.MGNTRNCODE.NORMAL,
                               OrdCndiTpCode=Stock.Order.ORDCNDITPCODE.NONE,
                               )
    return await Async.async_rq_tr(session, tr_inst)


async def change_order(session,
                       token:str, 
                       OrgOrdNo:str,
                       IsuNo:str,
                       OrdQty:int,
                       OrdPrc:float,
                       OrdprcPtnCode:Stock.Order.ORDPRCPTNCODE):
    tr_inst = Stock.SCPAT00701(token=token,
                               OrgOrdNo=OrgOrdNo,
                               IsuNo=IsuNo,
                               OrdQty=OrdQty,
                               OrdPrc=OrdPrc,
                               OrdprcPtnCode=OrdprcPtnCode)
    return await Async.async_rq_tr(session, tr_inst)


async def cancel_order(session,
                       token:str,
                       OrgOrdNo:str,
                       IsuNo:str,
                       OrdQty:int):
    tr_inst = Stock.SCPAT00801(token=token,
                               OrgOrdNo=OrgOrdNo,
                               IsuNo=IsuNo,
                               OrdQty=OrdQty)
    return await Async.async_rq_tr(session,tr_inst)

