from ..Base import BaseTR
from .Const import EXCHGUBUN


class _TopItemTR(BaseTR):
    Url     = "/stock/high-item"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1441(_TopItemTR):
    TRCode = "t1441"
    Name   = "등락율상위"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun1, gubun2, gubun3, jc_num, sprice, eprice, volume, idx, jc_num2, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1441InBlock': {
            'gubun1': gubun1, 'gubun2': gubun2, 'gubun3': gubun3, 'jc_num': jc_num, 'sprice': sprice, 
            'eprice': eprice, 'volume': volume, 'idx': idx, 'jc_num2': jc_num2, 'exchgubun': exchgubun}}

    
class t1444(_TopItemTR):
    TRCode = "t1444"
    Name   = "시가총액상위"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, upcode, idx):
        super().__init__(token)
        self.body = {'t1444InBlock': {'upcode': upcode, 'idx': idx}}

    
class t1452(_TopItemTR):
    TRCode = "t1452"
    Name   = "거래량상위"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun, jnilgubun, sdiff, ediff, jc_num, sprice, eprice, volume, idx):
        super().__init__(token)
        self.body = {'t1452InBlock': {
            'gubun': gubun, 'jnilgubun': jnilgubun, 'sdiff': sdiff, 'ediff': ediff, 'jc_num':jc_num, 
            'sprice': sprice, 'eprice': eprice, 'volume': volume, 'idx': idx}}

    
class t1463(_TopItemTR):
    TRCode = "t1463"
    Name   = "거래대금상위"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, jnilgubun, jc_num, sprice, eprice, volume, idx, jc_num2, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1463InBlock': {
            'gubun': gubun, 'jnilgubun': jnilgubun, 'jc_num': jc_num, 'sprice': sprice, 'eprice': eprice, 
            'volume': volume, 'idx': idx, 'jc_num2': jc_num2, 'exchgubun': exchgubun }}

    
class t1466(_TopItemTR):
    TRCode = "t1466"
    Name   = "전일동시간대비거래급증"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, type1, type2, jc_num, sprice, eprice, volume, idx, jc_num2, exchgubun:EXCHGUBUN=EXCHGUBUN.KRX):
        super().__init__(token)
        self.body = {'t1466InBlock': {
            'gubun': gubun, 'type1': type1, 'type2': type2, 'jc_num': jc_num, 'sprice': sprice, 'eprice': eprice, 
            'volume': volume, 'idx': idx, 'jc_num2': jc_num2, 'exchgubun': exchgubun}}

    
class t1481(_TopItemTR):
    TRCode = "t1481"
    Name   = "시간외등락율상위"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun1, gubun2, jongchk, volume, idx):
        super().__init__(token)
        self.body = {'t1481InBlock': {
            'gubun1': gubun1, 'gubun2': gubun2, 'jongchk': jongchk, 
            'volume': volume, 'idx': idx}}

    
class t1482(_TopItemTR):
    TRCode = "t1482"
    Name   = "시간외거래량상위"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class SORT_GBN:
        VOLUME    = '0'
        TRADESIZE = '1'
        거래량     = '0'
        거래대금   = '1'
    class GUBUN:
        ALL, KOSPI, KOSDAQ  = '0', '1', '2'
    class JONGCHK:
        ALL, EXCLUDE_PRIORITIES, EXCLUDE_MANAGED, EXCLUDE_PRIO_AND_MANAGED = '0', '1', '2', '3'
    def __init__(self, token, sort_gbn:SORT_GBN, gubun:GUBUN, jongchk:JONGCHK, idx:int):
        super().__init__(token)
        self.body = {'t1482InBlock': {'sort_gbn': sort_gbn, 'gubun': gubun, 'jongchk': jongchk, 'idx': idx}}

    
class t1489(_TopItemTR):
    TRCode = "t1489"
    Name   = "예상체결량상위조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, jgubun, jongchk, idx, yesprice, yeeprice, yevolume):
        super().__init__(token)
        self.body = {'t1489InBlock': {
            'gubun': gubun, 'jgubun': jgubun, 'jongchk': jongchk, 'idx': idx, 
            'yesprice': yesprice, 'yeeprice': yeeprice, 'yevolume': yevolume}}

    
class t1492(_TopItemTR):
    TRCode = "t1492"
    Name   = "단일가예상등락율상위"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun1, gubun2, jongchk, volume, idx):
        super().__init__(token)
        self.body = {'t1492InBlock': {
            'gubun1': gubun1, 'gubun2': gubun2, 'jongchk': jongchk, 
            'volume': volume, 'idx': idx}}

    