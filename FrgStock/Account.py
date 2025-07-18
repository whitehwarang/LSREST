
from ..Base import BaseTR


class _AccountTR(BaseTR):
    Url     = "/overseas-stock/accno"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class COSAQ00102(_AccountTR):
    TRCode = "COSAQ00102"
    Name   = "해외주식 계좌주문체결내역조회 API"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, RecCnt, QryTpCode, BkseqTpCode, OrdMktCode, BnsTpCode, IsuNo, SrtOrdNo, OrdDt, ExecYn, CrcyCode, ThdayBnsAppYn, LoanBalHldYn):
        super().__init__(token)
        self.body = {'COSAQ00102InBlock1': {'RecCnt': RecCnt, 'QryTpCode': QryTpCode, 'BkseqTpCode': BkseqTpCode, 'OrdMktCode': OrdMktCode, 'BnsTpCode': BnsTpCode, 'IsuNo': IsuNo, 'SrtOrdNo': SrtOrdNo, 'OrdDt': OrdDt, 'ExecYn': ExecYn, 'CrcyCode': CrcyCode, 'ThdayBnsAppYn': ThdayBnsAppYn, 'LoanBalHldYn': LoanBalHldYn}}

            
class COSAQ01400(_AccountTR):
    TRCode = "COSAQ01400"
    Name   = "예약주문 처리결과 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, RecCnt, QryTpCode, CntryCode, AcntNo, Pwd, SrtDt, EndDt, BnsTpCode, RsvOrdCndiCode, RsvOrdStatCode):
        super().__init__(token)
        self.body = {'COSAQ01400InBlock1': {'RecCnt': RecCnt, 'QryTpCode': QryTpCode, 'CntryCode': CntryCode, 'AcntNo': AcntNo, 'Pwd': Pwd, 'SrtDt': SrtDt, 'EndDt': EndDt, 'BnsTpCode': BnsTpCode, 'RsvOrdCndiCode': RsvOrdCndiCode, 'RsvOrdStatCode': RsvOrdStatCode}}

            
class COSOQ00201(_AccountTR):
    TRCode = "COSOQ00201"
    Name   = "해외주식 종합잔고평가 API"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, RecCnt, BaseDt, CrcyCode, AstkBalTpCode):
        super().__init__(token)
        self.body = {'COSOQ00201InBlock1': {'RecCnt': RecCnt, 'BaseDt': BaseDt, 'CrcyCode': CrcyCode, 'AstkBalTpCode': AstkBalTpCode}}


class COSOQ02701(_AccountTR):
    TRCode = "COSOQ02701"
    Name   = "해외주식 예수금 조회 API"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, RecCnt, CrcyCode):
        super().__init__(token)
        self.body = {'COSOQ02701InBlock1': {'RecCnt': RecCnt, 'CrcyCode': CrcyCode}}

