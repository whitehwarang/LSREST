
from ..Base import BaseTR
from .Const import EXCHGUBUN


class _ETCTR(BaseTR):
    Url     = "/stock/etc"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CLNAQ00100(_ETCTR):
    TRCode = "CLNAQ00100"
    Name   = "예탁담보융자가능종목현황조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QryTp, IsuNo, SecTpCode, LoanIntrstGrdCode, LoanTp):
        super().__init__(token)
        self.body = {'CLNAQ00100InBlock1': {'QryTp': QryTp, 'IsuNo': IsuNo, 'SecTpCode': SecTpCode, 'LoanIntrstGrdCode': LoanIntrstGrdCode, 'LoanTp': LoanTp}}

    
class t1403(_ETCTR):
    TRCode = "t1403"
    Name   = "신규상장종목조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, styymm, enyymm, idx):
        super().__init__(token)
        self.body = {'t1403InBlock': {'gubun': gubun, 'styymm': styymm, 'enyymm': enyymm, 'idx': idx}}

    
class t1411(_ETCTR):
    TRCode = "t1411"
    Name   = "증거금율별종목조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, jongchk, jkrate, shcode, idx):
        super().__init__(token)
        self.body = {'t1411InBlock': {'gubun': gubun, 'jongchk': jongchk, 'jkrate': jkrate, 'shcode': shcode, 'idx': idx}}

    
class t1638(_ETCTR):
    TRCode = "t1638"
    Name   = "종목별잔량/사전공시"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun1, shcode, gubun2, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1638InBlock': {'gubun1': gubun1, 'shcode': shcode, 'gubun2': gubun2, 'exchgubun': exchgubun}}

    
class t1921(_ETCTR):
    TRCode = "t1921"
    Name   = "신용거래동향"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun, date, idx):
        super().__init__(token)
        self.body = {'t1921InBlock': {'shcode': shcode, 'gubun': gubun, 'date': date, 'idx': idx}}

    
class t1926(_ETCTR):
    TRCode = "t1926"
    Name   = "종목별신용정보"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1926InBlock': {'shcode': shcode}}

    
class t1927(_ETCTR):
    TRCode = "t1927"
    Name   = "공매도일별추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, date, sdate, edate):
        super().__init__(token)
        self.body = {'t1927InBlock': {'shcode': shcode, 'date': date, 'sdate': sdate, 'edate': edate}}

    
class t1941(_ETCTR):
    TRCode = "t1941"
    Name   = "종목별대차거래일간추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, sdate, edate):
        super().__init__(token)
        self.body = {'t1941InBlock': {'shcode': shcode, 'sdate': sdate, 'edate': edate}}

    
class t8430(_ETCTR):
    TRCode = "t8430"
    Name   = "주식종목조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'t8430InBlock': {'gubun': gubun}}

    
class t8436(_ETCTR):
    TRCode = "t8436"
    Name   = "주식종목조회 API용"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'t8436InBlock': {'gubun': gubun}}

    