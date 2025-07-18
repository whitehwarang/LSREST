
from ..Base import BaseTR


class _ChartTR(BaseTR):
    Url     = "/overseas-stock/chart"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class g3103(_ChartTR):
    TRCode = "g3103"
    Name   = "해외주식 API 일주월 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, delaygb, keysymbol, exchcd, symbol, gubun, date):
        super().__init__(token)
        self.body = {'g3103InBlock': {'delaygb': delaygb, 'keysymbol': keysymbol, 'exchcd': exchcd, 'symbol': symbol, 'gubun': gubun, 'date': date}}


class g3202(_ChartTR):
    TRCode = "g3202"
    Name   = "해외주식 API 차트NTICK 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, delaygb, keysymbol, exchcd, symbol, ncnt, qrycnt, comp_yn, sdate, edate, cts_seq):
        super().__init__(token)
        self.body = {'g3202InBlock': {'delaygb': delaygb, 'keysymbol': keysymbol, 'exchcd': exchcd, 'symbol': symbol, 'ncnt': ncnt, 'qrycnt': qrycnt, 'comp_yn': comp_yn, 'sdate': sdate, 'edate': edate, 'cts_seq': cts_seq}}


class g3203(_ChartTR):
    TRCode = "g3203"
    Name   = "해외주식 API 차트NMIN 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, delaygb, keysymbol, exchcd, symbol, ncnt, qrycnt, comp_yn, sdate, edate, cts_date, cts_time):
        super().__init__(token)
        self.body = {'g3203InBlock': {'delaygb': delaygb, 'keysymbol': keysymbol, 'exchcd': exchcd, 'symbol': symbol, 'ncnt': ncnt, 'qrycnt': qrycnt, 'comp_yn': comp_yn, 'sdate': sdate, 'edate': edate, 'cts_date': cts_date, 'cts_time': cts_time}}


class g3204(_ChartTR):
    TRCode = "g3204"
    Name   = "해외주식 API 차트일주월년별 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, sujung, delaygb, keysymbol, exchcd, symbol, gubun, qrycnt, comp_yn, sdate, edate, cts_date, cts_info):
        super().__init__(token)
        self.body = {'g3204InBlock': {'sujung': sujung, 'delaygb': delaygb, 'keysymbol': keysymbol, 'exchcd': exchcd, 'symbol': symbol, 'gubun': gubun, 'qrycnt': qrycnt, 'comp_yn': comp_yn, 'sdate': sdate, 'edate': edate, 'cts_date': cts_date, 'cts_info': cts_info}}

