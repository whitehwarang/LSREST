
from API.Base import BaseTR


class _AccountTR(BaseTR):
    Url     = "/overseas-futureoption/accno"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CIDBQ01400(_AccountTR):
    TRCode = "CIDBQ01400"
    Name   = "해외선물 체결내역개별 조회(주문가능수량)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QryTpCode, IsuCodeVal, BnsTpCode, OvrsDrvtOrdPrc, AbrdFutsOrdPtnCode):
        super().__init__(token)
        self.body = {'CIDBQ01400InBlock1': {
            'QryTpCode': QryTpCode, 'IsuCodeVal': IsuCodeVal, 'BnsTpCode': BnsTpCode, 
            'OvrsDrvtOrdPrc': OvrsDrvtOrdPrc, 'AbrdFutsOrdPtnCode': AbrdFutsOrdPtnCode}}

    
class CIDBQ01500(_AccountTR):
    TRCode = "CIDBQ01500"
    Name   = "해외선물 미결제잔고내역 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, AcntTpCode, QryDt, BalTpCode):
        super().__init__(token)
        self.body = {'CIDBQ01500InBlock1': {'AcntTpCode': AcntTpCode, 'QryDt': QryDt, 'BalTpCode': BalTpCode}}

    
class CIDBQ01800(_AccountTR):
    TRCode = "CIDBQ01800"
    Name   = "해외선물 주문내역 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, IsuCodeVal, OrdDt, ThdayTpCode, OrdStatCode, BnsTpCode, QryTpCode, OrdPtnCode, OvrsDrvtFnoTpCode):
        super().__init__(token)
        self.body = {'CIDBQ01800InBlock1': {
            'IsuCodeVal': IsuCodeVal, 'OrdDt': OrdDt, 'ThdayTpCode': ThdayTpCode, 'OrdStatCode': OrdStatCode, 
            'BnsTpCode': BnsTpCode, 'QryTpCode': QryTpCode, 'OrdPtnCode': OrdPtnCode, 'OvrsDrvtFnoTpCode': OvrsDrvtFnoTpCode}}

    
class CIDBQ02400(_AccountTR):
    TRCode = "CIDBQ02400"
    Name   = "해외선물 주문체결내역 상세 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, IsuCodeVal, QrySrtDt, QryEndDt, ThdayTpCode, OrdStatCode, BnsTpCode, QryTpCode, OrdPtnCode, OvrsDrvtFnoTpCode):
        super().__init__(token)
        self.body = {'CIDBQ02400InBlock1': {'IsuCodeVal': IsuCodeVal, 'QrySrtDt': QrySrtDt, 'QryEndDt': QryEndDt, 'ThdayTpCode': ThdayTpCode, 'OrdStatCode': OrdStatCode, 'BnsTpCode': BnsTpCode, 'QryTpCode': QryTpCode, 'OrdPtnCode': OrdPtnCode, 'OvrsDrvtFnoTpCode': OvrsDrvtFnoTpCode}}

    
class CIDBQ03000(_AccountTR):
    TRCode = "CIDBQ03000"
    Name   = "해외선물 예수금/잔고현황"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, AcntTpCode, TrdDt):
        super().__init__(token)
        self.body = {'CIDBQ03000InBlock1': {'AcntTpCode': AcntTpCode, 'TrdDt': TrdDt}}

    
class CIDBQ05300(_AccountTR):
    TRCode = "CIDBQ05300"
    Name   = "해외선물 예탁자산 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, OvrsAcntTpCode, CrcyCode):
        super().__init__(token)
        self.body = {'CIDBQ05300InBlock1': {'OvrsAcntTpCode': OvrsAcntTpCode, 'CrcyCode': CrcyCode}}

    
class CIDEQ00800(_AccountTR):
    TRCode = "CIDEQ00800"
    Name   = "일자별 미결제 잔고내역"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, TrdDt):
        super().__init__(token)
        self.body = {'CIDEQ00800InBlock1': {'TrdDt': TrdDt}}

    