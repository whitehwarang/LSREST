
from ..Base import BaseTR


class _OrderTR(BaseTR):
    Url     = "/overseas-stock/order"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class COSAT00301(_OrderTR):
    TRCode = "COSAT00301"
    Name   = "미국시장주문 API"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, token, RecCnt, OrdPtnCode, OrgOrdNo, OrdMktCode, IsuNo, OrdQty, OvrsOrdPrc, OrdprcPtnCode, BrkTpCode):
        super().__init__(token)
        self.body = {'COSAT00301InBlock1': {'RecCnt': RecCnt, 'OrdPtnCode': OrdPtnCode, 'OrgOrdNo': OrgOrdNo, 'OrdMktCode': OrdMktCode, 'IsuNo': IsuNo, 'OrdQty': OrdQty, 'OvrsOrdPrc': OvrsOrdPrc, 'OrdprcPtnCode': OrdprcPtnCode, 'BrkTpCode': BrkTpCode}}

            
class COSAT00311(_OrderTR):
    TRCode = "COSAT00311"
    Name   = "미국시장정정주문 API"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, token, RecCnt, OrdPtnCode, OrgOrdNo, OrdMktCode, IsuNo, OrdQty, OvrsOrdPrc, OrdprcPtnCode, BrkTpCode):
        super().__init__(token)
        self.body = {'COSAT00311InBlock1': {'RecCnt': RecCnt, 'OrdPtnCode': OrdPtnCode, 'OrgOrdNo': OrgOrdNo, 'OrdMktCode': OrdMktCode, 'IsuNo': IsuNo, 'OrdQty': OrdQty, 'OvrsOrdPrc': OvrsOrdPrc, 'OrdprcPtnCode': OrdprcPtnCode, 'BrkTpCode': BrkTpCode}}

            
class COSMT00300(_OrderTR):
    TRCode = "COSMT00300"
    Name   = "해외증권 매도상환주문(미국)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, RecCnt, OrdPtnCode, OrgOrdNo, AcntNo, InptPwd, OrdMktCode, IsuNo, OrdQty, OvrsOrdPrc, OrdprcPtnCode, BrkTpCode, MgntrnCode, LoanDt):
        super().__init__(token)
        self.body = {'COSMT00300InBlock1': {'RecCnt': RecCnt, 'OrdPtnCode': OrdPtnCode, 'OrgOrdNo': OrgOrdNo, 'AcntNo': AcntNo, 'InptPwd': InptPwd, 'OrdMktCode': OrdMktCode, 'IsuNo': IsuNo, 'OrdQty': OrdQty, 'OvrsOrdPrc': OvrsOrdPrc, 'OrdprcPtnCode': OrdprcPtnCode, 'BrkTpCode': BrkTpCode, 'MgntrnCode': MgntrnCode, 'LoanDt': LoanDt}}

            
class COSAT00400(_OrderTR):
    TRCode = "COSAT00400"
    Name   = "해외주식 예약주문 등록 및 취소"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, RecCnt, TrxTpCode, CntryCode, RsvOrdInptDt, RsvOrdNo, BnsTpCode, AcntNo, Pwd, FcurrMktCode, IsuNo, OrdQty, OvrsOrdPrc, OrdprcPtnCode, RsvOrdSrtDt, RsvOrdEndDt, RsvOrdCndiCode, MgntrnCode, LoanDt, LoanDtlClssCode):
        super().__init__(token)
        self.body = {'COSAT00400InBlock1': {'RecCnt': RecCnt, 'TrxTpCode': TrxTpCode, 'CntryCode': CntryCode, 'RsvOrdInptDt': RsvOrdInptDt, 'RsvOrdNo': RsvOrdNo, 'BnsTpCode': BnsTpCode, 'AcntNo': AcntNo, 'Pwd': Pwd, 'FcurrMktCode': FcurrMktCode, 'IsuNo': IsuNo, 'OrdQty': OrdQty, 'OvrsOrdPrc': OvrsOrdPrc, 'OrdprcPtnCode': OrdprcPtnCode, 'RsvOrdSrtDt': RsvOrdSrtDt, 'RsvOrdEndDt': RsvOrdEndDt, 'RsvOrdCndiCode': RsvOrdCndiCode, 'MgntrnCode': MgntrnCode, 'LoanDt': LoanDt, 'LoanDtlClssCode': LoanDtlClssCode}}

            