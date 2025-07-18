
from ..Base import BaseTR


class _SiseTR(BaseTR):
    Url     = "/overseas-stock/market-data"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class g3101(_SiseTR):
    TRCode = "g3101"
    Name   = "해외주식 API 현재가 조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, delaygb, keysymbol, exchcd, symbol):
        super().__init__(token)
        self.body = {'g3101InBlock': {'delaygb': delaygb, 'keysymbol': keysymbol, 'exchcd': exchcd, 'symbol': symbol}}

            
class g3102(_SiseTR):
    TRCode = "g3102"
    Name   = "해외주식 API 시간대별"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, delaygb, keysymbol, exchcd, readcnt, cts_seq):
        super().__init__(token)
        self.body = {'g3102InBlock': {'delaygb': delaygb, 'keysymbol': keysymbol, 'exchcd': exchcd, 'readcnt': readcnt, 'cts_seq': cts_seq}}

            
class g3104(_SiseTR):
    TRCode = "g3104"
    Name   = "해외주식 API 종목정보 조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, delaygb, keysymbol, exchcd, symbol):
        super().__init__(token)
        self.body = {'g3104InBlock': {'delaygb': delaygb, 'keysymbol': keysymbol, 'exchcd': exchcd, 'symbol': symbol}}

            
class g3106(_SiseTR):
    TRCode = "g3106"
    Name   = "해외주식 API 현재가호가 조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, delaygb, keysymbol, exchcd, symbol):
        super().__init__(token)
        self.body = {'g3106InBlock': {'delaygb': delaygb, 'keysymbol': keysymbol, 'exchcd': exchcd, 'symbol': symbol}}

            
class g3190(_SiseTR):
    TRCode = "g3190"
    Name   = "해외주식 API 마스터 조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, delaygb, natcode, exgubun, readcnt, cts_value):
        super().__init__(token)
        self.body = {'g3190InBlock': {'delaygb': delaygb, 'natcode': natcode, 'exgubun': exgubun, 'readcnt': readcnt, 'cts_value': cts_value}}

            