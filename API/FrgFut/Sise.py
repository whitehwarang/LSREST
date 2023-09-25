
from API.Base import BaseTR


class _SiseTR(BaseTR):
    Url     = "/overseas-futureoption/market-data"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class o3101(_SiseTR):
    TRCode = "o3101"
    Name   = "해외선물마스터조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'o3101InBlock': {'gubun': gubun}}

    
class o3104(_SiseTR):
    TRCode = "o3104"
    Name   = "해외선물 일별체결 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, shcode, date):
        super().__init__(token)
        self.body = {'o3104InBlock': {'gubun': gubun, 'shcode': shcode, 'date': date}}

    
class o3105(_SiseTR):
    TRCode = "o3105"
    Name   = "해외선물 현재가(종목정보) 조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, symbol):
        super().__init__(token)
        self.body = {'o3105InBlock': {'symbol': symbol}}

    
class o3106(_SiseTR):
    TRCode = "o3106"
    Name   = "해외선물 현재가호가 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, symbol):
        super().__init__(token)
        self.body = {'o3106InBlock': {'symbol': symbol}}

    
class o3107(_SiseTR):
    TRCode = "o3107"
    Name   = "해외선물 관심종목 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, symbol):
        super().__init__(token)
        self.body = {'o3107InBlock (Occurs)': {'symbol': symbol}}

    
class o3116(_SiseTR):
    TRCode = "o3116"
    Name   = "해외선물 시간대별(Tick)체결 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, shcode, readcnt, cts_seq):
        super().__init__(token)
        self.body = {'o3116InBlock': {'gubun': gubun, 'shcode': shcode, 'readcnt': readcnt, 'cts_seq': cts_seq}}

    
class o3121(_SiseTR):
    TRCode = "o3121"
    Name   = "해외선물옵션 마스터 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, MktGb, BscGdsCd):
        super().__init__(token)
        self.body = {'o3121InBlock': {'MktGb': MktGb, 'BscGdsCd': BscGdsCd}}

    
class o3123(_SiseTR):
    TRCode = "o3123"
    Name   = "해외선물옵션 차트 분봉 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, mktgb, shcode, ncnt, readcnt, cts_date, cts_time):
        super().__init__(token)
        self.body = {'o3123InBlock': {'mktgb': mktgb, 'shcode': shcode, 'ncnt': ncnt, 'readcnt': readcnt, 'cts_date': cts_date, 'cts_time': cts_time}}

    
class o3125(_SiseTR):
    TRCode = "o3125"
    Name   = "해외선물옵션 현재가(종목정보) 조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, mktgb, symbol):
        super().__init__(token)
        self.body = {'o3125InBlock': {'mktgb': mktgb, 'symbol': symbol}}

    
class o3126(_SiseTR):
    TRCode = "o3126"
    Name   = "해외선물옵션 현재가호가 조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, mktgb, symbol):
        super().__init__(token)
        self.body = {'o3126InBlock': {'mktgb': mktgb, 'symbol': symbol}}

    
class o3127(_SiseTR):
    TRCode = "o3127"
    Name   = "해외선물옵션 관심종목 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, nrec):
        super().__init__(token)
        self.body = {'o3127InBlock': {'nrec': nrec}}

    
class o3128(_SiseTR):
    TRCode = "o3128"
    Name   = "해외선물옵션 차트 일주월 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, mktgb, shcode, gubun, qrycnt, sdate, edate, cts_date):
        super().__init__(token)
        self.body = {'o3128InBlock': {'mktgb': mktgb, 'shcode': shcode, 'gubun': gubun, 'qrycnt': qrycnt, 'sdate': sdate, 'edate': edate, 'cts_date': cts_date}}

    
class o3136(_SiseTR):
    TRCode = "o3136"
    Name   = "해외선물옵션 시간대별 Tick 체결 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, mktgb, shcode, readcnt, cts_seq):
        super().__init__(token)
        self.body = {'o3136InBlock': {'gubun': gubun, 'mktgb': mktgb, 'shcode': shcode, 'readcnt': readcnt, 'cts_seq': cts_seq}}

    
class o3137(_SiseTR):
    TRCode = "o3137"
    Name   = "해외선물옵션 차트 NTick 체결 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, mktgb, shcode, ncnt, qrycnt, cts_seq, cts_daygb):
        super().__init__(token)
        self.body = {'o3137InBlock': {'mktgb': mktgb, 'shcode': shcode, 'ncnt': ncnt, 'qrycnt': qrycnt, 'cts_seq': cts_seq, 'cts_daygb': cts_daygb}}

    