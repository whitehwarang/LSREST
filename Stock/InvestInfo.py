
from ..Base import BaseTR


class _InvestInfoTR(BaseTR):
    Url     = "/stock/investinfo"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t3102(_InvestInfoTR):
    TRCode = "t3102"
    Name   = "뉴스본문"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, sNewsno):
        super().__init__(token)
        self.body = {'t3102InBlock': {'sNewsno': sNewsno}}

    
class t3202(_InvestInfoTR):
    TRCode = "t3202"
    Name   = "종목별증시일정"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, date):
        super().__init__(token)
        self.body = {'t3202InBlock': {'shcode': shcode, 'date': date}}

    
class t3320(_InvestInfoTR):
    TRCode = "t3320"
    Name   = "FNG_요약"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gicode):
        super().__init__(token)
        self.body = {'t3320InBlock': {'gicode': gicode}}

    
class t3341(_InvestInfoTR):
    TRCode = "t3341"
    Name   = "재무순위종합"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, gubun1, gubun2, idx):
        super().__init__(token)
        self.body = {'t3341InBlock': {'gubun': gubun, 'gubun1': gubun1, 'gubun2': gubun2, 'idx': idx}}

    
class t3401(_InvestInfoTR):
    TRCode = "t3401"
    Name   = "투자의견"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun1, tradno, cts_date):
        super().__init__(token)
        self.body = {'t3401InBlock': {'shcode': shcode, 'gubun1': gubun1, 'tradno': tradno, 'cts_date': cts_date}}

    
class t3518(_InvestInfoTR):
    TRCode = "t3518"
    Name   = "해외실시간지수"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, kind, symbol, cnt, jgbn, nmin, cts_date, cts_time):
        super().__init__(token)
        self.body = {'t3518InBlock': {'kind': kind, 'symbol': symbol, 'cnt': cnt, 'jgbn': jgbn, 'nmin': nmin, 'cts_date': cts_date, 'cts_time': cts_time}}

    
class t3521(_InvestInfoTR):
    TRCode = "t3521"
    Name   = "해외지수조회(API용)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, kind, symbol):
        super().__init__(token)
        self.body = {'t3521InBlock': {'kind': kind, 'symbol': symbol}}

    
class t8428(_InvestInfoTR):
    TRCode = "t8428"
    Name   = "증시주변자금추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, fdate, tdate, gubun, key_date, upcode, cnt):
        super().__init__(token)
        self.body = {'t8428InBlock': {'fdate': fdate, 'tdate': tdate, 'gubun': gubun, 'key_date': key_date, 'upcode': upcode, 'cnt': cnt}}

    