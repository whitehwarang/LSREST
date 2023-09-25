
from ..Base import BaseTR


class _AccountTR(BaseTR):
    Url     = "/futureoption/accno"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CFOAQ00600(_AccountTR):
    TRCode = "CFOAQ00600"
    Name   = "선물옵션 계좌 주문체결내역 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QrySrtDt, QryEndDt, FnoClssCode, PrdgrpCode, PrdtExecTpCode, StnlnSeqTp, CommdaCode):
        super().__init__(token)
        self.body = {'CFOAQ00600InBlock1': {'QrySrtDt': QrySrtDt, 'QryEndDt': QryEndDt, 'FnoClssCode': FnoClssCode, 'PrdgrpCode': PrdgrpCode, 'PrdtExecTpCode': PrdtExecTpCode, 'StnlnSeqTp': StnlnSeqTp, 'CommdaCode': CommdaCode}}

    
class CFOAQ10100(_AccountTR):
    TRCode = "CFOAQ10100"
    Name   = "선물옵션 주문가능수량조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QryTp, OrdAmt, RatVal, FnoIsuNo, BnsTpCode, FnoOrdPrc, FnoOrdprcPtnCode):
        super().__init__(token)
        self.body = {'CFOAQ10100InBlock1': {'QryTp': QryTp, 'OrdAmt': OrdAmt, 'RatVal': RatVal, 'FnoIsuNo': FnoIsuNo, 'BnsTpCode': BnsTpCode, 'FnoOrdPrc': FnoOrdPrc, 'FnoOrdprcPtnCode': FnoOrdprcPtnCode}}

    
class CFOBQ10500(_AccountTR):
    TRCode = "CFOBQ10500"
    Name   = "선물옵션 계좌예탁금증거금조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, ):
        super().__init__(token)
        self.body = {'CFOBQ10500InBlock1': {}}

    
class CFOEQ11100(_AccountTR):
    TRCode = "CFOEQ11100"
    Name   = "선물옵션가정산예탁금상세"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, BnsDt):
        super().__init__(token)
        self.body = {'CFOEQ11100InBlock1': {'BnsDt': BnsDt}}

    
class CFOEQ82600(_AccountTR):
    TRCode = "CFOEQ82600"
    Name   = "선물옵션 일별 계좌손익내역"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QrySrtDt, QryEndDt, QryTp, StnlnSeqTp, FnoBalEvalTpCode):
        super().__init__(token)
        self.body = {'CFOEQ82600InBlock1': {'QrySrtDt': QrySrtDt, 'QryEndDt': QryEndDt, 'QryTp': QryTp, 'StnlnSeqTp': StnlnSeqTp, 'FnoBalEvalTpCode': FnoBalEvalTpCode}}

    
class CFOFQ02400(_AccountTR):
    TRCode = "CFOFQ02400"
    Name   = "계좌 미결제 약정현황(평균가)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, RegMktCode, BuyDt):
        super().__init__(token)
        self.body = {'CFOFQ02400InBlock1': {'RegMktCode': RegMktCode, 'BuyDt': BuyDt}}

    
class t0434(_AccountTR):
    TRCode = "t0434"
    Name   = "선물/옵션체결/미체결"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, expcode, chegb, sortgb, cts_ordno):
        super().__init__(token)
        self.body = {'t0434InBlock': {'expcode': expcode, 'chegb': chegb, 'sortgb': sortgb, 'cts_ordno': cts_ordno}}

    
class t0441(_AccountTR):
    TRCode = "t0441"
    Name   = "선물/옵션잔고평가(이동평균)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, cts_expcode, cts_medocd):
        super().__init__(token)
        self.body = {'t0441InBlock': {'cts_expcode': cts_expcode, 'cts_medocd': cts_medocd}}

    
class CEXAQ21100(_AccountTR):
    TRCode = "CEXAQ21100"
    Name   = "EUREX 주문체결내역조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, ChoicInptTpCode, PrdtExecTpCode, StnlnSeqTp):
        super().__init__(token)
        self.body = {'CEXAQ21100InBlock1': {'ChoicInptTpCode': ChoicInptTpCode, 'PrdtExecTpCode': PrdtExecTpCode, 'StnlnSeqTp': StnlnSeqTp}}

    
class CEXAQ21200(_AccountTR):
    TRCode = "CEXAQ21200"
    Name   = "EUREX 주문가능 수량/금액 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QryTp, OrdAmt, RatVal, FnoIsuNo, BnsTpCode, OrdPrc, ErxPrcCndiTpCode):
        super().__init__(token)
        self.body = {'CEXAQ21200InBlock1': {'QryTp': QryTp, 'OrdAmt': OrdAmt, 'RatVal': RatVal, 'FnoIsuNo': FnoIsuNo, 'BnsTpCode': BnsTpCode, 'OrdPrc': OrdPrc, 'ErxPrcCndiTpCode': ErxPrcCndiTpCode}}

    
class CEXAQ31100(_AccountTR):
    TRCode = "CEXAQ31100"
    Name   = "EUREX 야간장잔고및 평가현황"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, IsuCode, BalEvalTp, FutsPrcEvalTp):
        super().__init__(token)
        self.body = {'CEXAQ31100InBlock1': {'IsuCode': IsuCode, 'BalEvalTp': BalEvalTp, 'FutsPrcEvalTp': FutsPrcEvalTp}}

    
class CEXAQ31200(_AccountTR):
    TRCode = "CEXAQ31200"
    Name   = "EUREX 예탁금 및 통합잔고조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, BalEvalTp, FutsPrcEvalTp):
        super().__init__(token)
        self.body = {'CEXAQ31200InBlock1': {'BalEvalTp': BalEvalTp, 'FutsPrcEvalTp': FutsPrcEvalTp}}

    
class CEXAQ44200(_AccountTR):
    TRCode = "CEXAQ44200"
    Name   = "EUREX 야간옵션 기간주문체결조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QrySrtDt, QryEndDt, PrdtExecTpCode, FnoTrdPtnCode, SrtOrdNo2, StnlnSeqTp):
        super().__init__(token)
        self.body = {'CEXAQ44200InBlock1': {'QrySrtDt': QrySrtDt, 'QryEndDt': QryEndDt, 'PrdtExecTpCode': PrdtExecTpCode, 'FnoTrdPtnCode': FnoTrdPtnCode, 'SrtOrdNo2': SrtOrdNo2, 'StnlnSeqTp': StnlnSeqTp}}

    
class FOCCQ33700(_AccountTR):
    TRCode = "FOCCQ33700"
    Name   = "선물옵션 기간별 계좌 수익률 현황"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QrySrtDt, QryEndDt, QryTp, BaseAmtTp, QryTermTp, PnlCalcTpCode):
        super().__init__(token)
        self.body = {'FOCCQ33700InBlock1': {'QrySrtDt': QrySrtDt, 'QryEndDt': QryEndDt, 'QryTp': QryTp, 'BaseAmtTp': BaseAmtTp, 'QryTermTp': QryTermTp, 'PnlCalcTpCode': PnlCalcTpCode}}

    