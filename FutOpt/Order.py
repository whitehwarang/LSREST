
from ..Base import BaseTR


class _OrderTR(BaseTR):
    Url     = "/futureoption/order"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FNOORDPRCPTNCODE:
    SPECIFIC = "00"                         # 지정가 
    SPECIFIC_IOC = '10'                     # 지정가 (IOC)
    SPECIFIC_FOK = '20'                     # 지정가 (FOK)
    MARKET = "03"                           # 시장가 
    MARKET_IOC = '13'                       # 시장가 (IOC)
    MARKET_FOK = '23'                       # 시장가 (FOK)
    CONDITIONAL_SPECIFIC = "05"             # 조건부지정가
    MOST_ADVENTAGEOUS_SPECIFIC = "06"       # 최유리지정가
    MOST_ADVENTAGEOUS_SPECIFIC_IOC = "16"       # 최유리지정가(IOC)
    MOST_ADVENTAGEOUS_SPECIFIC_FOK = "26"       # 최유리지정가(FOK)


class CFOAT00100(_OrderTR):
    TRCode = "CFOAT00100"
    Name   = "선물옵션 정상주문"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, token, FnoIsuNo, BnsTpCode, FnoOrdprcPtnCode:FNOORDPRCPTNCODE, FnoOrdPrc, OrdQty):
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

"""
25.06.07. KRX 야간파생 도입에 따라 아래 TR이 삭제됨

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
"""
    
