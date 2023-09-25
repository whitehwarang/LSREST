
from ..Base import BaseTR


class _OrderTR(BaseTR):
    Url     = "/futureoption/order"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CFOAT00100(_OrderTR):
    TRCode = "CFOAT00100"
    Name   = "선물옵션 정상주문"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, token, FnoIsuNo, BnsTpCode, FnoOrdprcPtnCode, FnoOrdPrc, OrdQty):
        super().__init__(token)
        self.body = {'CFOAT00100InBlock1': {'FnoIsuNo': FnoIsuNo, 'BnsTpCode': BnsTpCode, 'FnoOrdprcPtnCode': FnoOrdprcPtnCode, 'FnoOrdPrc': FnoOrdPrc, 'OrdQty': OrdQty}}

    
class CFOAT00200(_OrderTR):
    TRCode = "CFOAT00200"
    Name   = "선물옵션 정정주문"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, token, FnoIsuNo, OrgOrdNo, FnoOrdprcPtnCode, FnoOrdPrc, MdfyQty):
        super().__init__(token)
        self.body = {'CFOAT00200InBlock1': {'FnoIsuNo': FnoIsuNo, 'OrgOrdNo': OrgOrdNo, 'FnoOrdprcPtnCode': FnoOrdprcPtnCode, 'FnoOrdPrc': FnoOrdPrc, 'MdfyQty': MdfyQty}}

    
class CFOAT00300(_OrderTR):
    TRCode = "CFOAT00300"
    Name   = "선물옵션 취소주문"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, token, FnoIsuNo, OrgOrdNo, CancQty):
        super().__init__(token)
        self.body = {'CFOAT00300InBlock1': {'FnoIsuNo': FnoIsuNo, 'OrgOrdNo': OrgOrdNo, 'CancQty': CancQty}}

    
class CFOBQ10800(_OrderTR):
    TRCode = "CFOBQ10800"
    Name   = "선물옵션 옵션매도시 주문증거금조회(옵션매도시 1계약당 주문증거금)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, SpclDtPtnCode, SettWklyCnt, DueYymm, IsuSmclssCode, IsuMdclssCode):
        super().__init__(token)
        self.body = {'CFOBQ10800InBlock1': {'SpclDtPtnCode': SpclDtPtnCode, 'SettWklyCnt': SettWklyCnt, 'DueYymm': DueYymm, 'IsuSmclssCode': IsuSmclssCode, 'IsuMdclssCode': IsuMdclssCode}}

    
class CEXAT11100(_OrderTR):
    TRCode = "CEXAT11100"
    Name   = "EUREX 매수/매도주문"
    TRLimitPerSecond = 5
    TRCnt  = 0
    def __init__(self, token, FnoIsuNo, BnsTpCode, ErxPrcCndiTpCode, OrdPrc, OrdQty):
        super().__init__(token)
        self.body = {'CEXAT11100InBlock1': {'FnoIsuNo': FnoIsuNo, 'BnsTpCode': BnsTpCode, 'ErxPrcCndiTpCode': ErxPrcCndiTpCode, 'OrdPrc': OrdPrc, 'OrdQty': OrdQty}}

    
class CEXAT11200(_OrderTR):
    TRCode = "CEXAT11200"
    Name   = "EUREX 정정주문"
    TRLimitPerSecond = 5
    TRCnt  = 0
    def __init__(self, token, OrgOrdNo, FnoIsuNo, OrdPrc):
        super().__init__(token)
        self.body = {'CEXAT11200InBlock1': {'OrgOrdNo': OrgOrdNo, 'FnoIsuNo': FnoIsuNo, 'OrdPrc': OrdPrc}}

    
class CEXAT11300(_OrderTR):
    TRCode = "CEXAT11300"
    Name   = "EUREX 취소주문"
    TRLimitPerSecond = 5
    TRCnt  = 0
    def __init__(self, token, OrgOrdNo, FnoIsuNo):
        super().__init__(token)
        self.body = {'CEXAT11300InBlock1': {'OrgOrdNo': OrgOrdNo, 'FnoIsuNo': FnoIsuNo}}

    