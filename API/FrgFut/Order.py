
from API.Base import BaseTR


class _OrderTR(BaseTR):
    Url     = "/overseas-futureoption/order"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CIDBT00100(_OrderTR):
    TRCode = "CIDBT00100"
    Name   = "해외선물 신규주문"
    TRLimitPerSecond = 5
    TRCnt  = 0
    def __init__(self, token, OrdDt, IsuCodeVal, FutsOrdTpCode, BnsTpCode, AbrdFutsOrdPtnCode, CrcyCode, OvrsDrvtOrdPrc, CndiOrdPrc, OrdQty, PrdtCode, DueYymm, ExchCode):
        super().__init__(token)
        self.body = {'CIDBT00100InBlock1': {'OrdDt': OrdDt, 'IsuCodeVal': IsuCodeVal, 'FutsOrdTpCode': FutsOrdTpCode, 'BnsTpCode': BnsTpCode, 'AbrdFutsOrdPtnCode': AbrdFutsOrdPtnCode, 'CrcyCode': CrcyCode, 'OvrsDrvtOrdPrc': OvrsDrvtOrdPrc, 'CndiOrdPrc': CndiOrdPrc, 'OrdQty': OrdQty, 'PrdtCode': PrdtCode, 'DueYymm': DueYymm, 'ExchCode': ExchCode}}

    
class CIDBT00900(_OrderTR):
    TRCode = "CIDBT00900"
    Name   = "해외선물 정정주문"
    TRLimitPerSecond = 5
    TRCnt  = 0
    def __init__(self, token, OrdDt, OvrsFutsOrgOrdNo, IsuCodeVal, FutsOrdTpCode, BnsTpCode, FutsOrdPtnCode, CrcyCodeVal, OvrsDrvtOrdPrc, CndiOrdPrc, OrdQty, OvrsDrvtPrdtCode, DueYymm, ExchCode):
        super().__init__(token)
        self.body = {'CIDBT00900InBlock1': {'OrdDt': OrdDt, 'OvrsFutsOrgOrdNo': OvrsFutsOrgOrdNo, 'IsuCodeVal': IsuCodeVal, 'FutsOrdTpCode': FutsOrdTpCode, 'BnsTpCode': BnsTpCode, 'FutsOrdPtnCode': FutsOrdPtnCode, 'CrcyCodeVal': CrcyCodeVal, 'OvrsDrvtOrdPrc': OvrsDrvtOrdPrc, 'CndiOrdPrc': CndiOrdPrc, 'OrdQty': OrdQty, 'OvrsDrvtPrdtCode': OvrsDrvtPrdtCode, 'DueYymm': DueYymm, 'ExchCode': ExchCode}}

    
class CIDBT01000(_OrderTR):
    TRCode = "CIDBT01000"
    Name   = "해외선물 취소주문"
    TRLimitPerSecond = 5
    TRCnt  = 0
    def __init__(self, token, OrdDt, IsuCodeVal, OvrsFutsOrgOrdNo, FutsOrdTpCode, PrdtTpCode, ExchCode):
        super().__init__(token)
        self.body = {'CIDBT01000InBlock1': {'OrdDt': OrdDt, 'IsuCodeVal': IsuCodeVal, 'OvrsFutsOrgOrdNo': OvrsFutsOrgOrdNo, 'FutsOrdTpCode': FutsOrdTpCode, 'PrdtTpCode': PrdtTpCode, 'ExchCode': ExchCode}}

    