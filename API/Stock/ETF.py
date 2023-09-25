
from API.Base import BaseTR


class _ETFTR(BaseTR):
    Url     = "/stock/etf"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1901(_ETFTR):
    TRCode = "t1901"
    Name   = "ETF현재가(시세)조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1901InBlock': {'shcode': shcode}}

    
class t1902(_ETFTR):
    TRCode = "t1902"
    Name   = "ETF시간별추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, time):
        super().__init__(token)
        self.body = {'t1902InBlock': {'shcode': shcode, 'time': time}}

    
class t1903(_ETFTR):
    TRCode = "t1903"
    Name   = "ETF일별추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, date):
        super().__init__(token)
        self.body = {'t1903InBlock': {'shcode': shcode, 'date': date}}

    
class t1904(_ETFTR):
    TRCode = "t1904"
    Name   = "ETF구성종목조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, date, sgb):
        super().__init__(token)
        self.body = {'t1904InBlock': {'shcode': shcode, 'date': date, 'sgb': sgb}}

    
class t1906(_ETFTR):
    TRCode = "t1906"
    Name   = "ETFLP호가"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1906InBlock': {'shcode': shcode}}

    