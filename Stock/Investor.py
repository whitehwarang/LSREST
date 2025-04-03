
from ..Base import BaseTR
from .Const import EXCHGUBUN


class _InvestorTR(BaseTR):
    Url     = "/stock/investor"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1601(_InvestorTR):
    TRCode = "t1601"
    Name   = "투자자별종합"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun1, gubun2, gubun3, gubun4, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1601InBlock': {'gubun1': gubun1, 'gubun2': gubun2, 'gubun3': gubun3, 'gubun4': gubun4, 'exchgubun': exchgubun}}

    
class t1602(_InvestorTR):
    TRCode = "t1602"
    Name   = "시간대별투자자매매추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, market, upcode, gubun1, gubun2, cts_time, cts_idx, cnt, gubun3, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1602InBlock': {'market': market, 'upcode': upcode, 'gubun1': gubun1, 'gubun2': gubun2, 'cts_time': cts_time, 'cts_idx': cts_idx, 'cnt': cnt, 'gubun3': gubun3, 'exchgubun': exchgubun}}

    
class t1603(_InvestorTR):
    TRCode = "t1603"
    Name   = "시간대별투자자매매추이상세"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, market, gubun1, gubun2, cts_time, cts_idx, cnt, upcode, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1603InBlock': {'market': market, 'gubun1': gubun1, 'gubun2': gubun2, 'cts_time': cts_time, 'cts_idx': cts_idx, 'cnt': cnt, 'upcode': upcode, 'exchgubun': exchgubun}}

    
class t1615(_InvestorTR):
    TRCode = "t1615"
    Name   = "투자자매매종합1"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun1, gubun2, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1615InBlock': {'gubun1': gubun1, 'gubun2': gubun2, 'exchgubun': exchgubun}}

    
class t1617(_InvestorTR):
    TRCode = "t1617"
    Name   = "투자자매매종합2"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun1, gubun2, gubun3, cts_date, cts_time, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1617InBlock': {'gubun1': gubun1, 'gubun2': gubun2, 'gubun3': gubun3, 'cts_date': cts_date, 'cts_time': cts_time, 'exchgubun': exchgubun}}


    
class t1621(_InvestorTR):
    TRCode = "t1621"
    Name   = "업종별분별투자자매매동향(챠트용)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, upcode, nmin, cnt, bgubun, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1621InBlock': {'upcode': upcode, 'nmin': nmin, 'cnt': cnt, 'bgubun': bgubun, 'exchgubun': exchgubun}}

    
class t1664(_InvestorTR):
    TRCode = "t1664"
    Name   = "투자자매매종합(챠트)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, mgubun, vagubun, bdgubun, cnt, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1664InBlock': {'mgubun': mgubun, 'vagubun': vagubun, 'bdgubun': bdgubun, 'cnt': cnt, 'exchgubun': exchgubun}}

    