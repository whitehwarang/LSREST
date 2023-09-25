
from ..Base import BaseTR


class _AccountTR(BaseTR):
    Url     = "/stock/accno"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CDPCQ04700(_AccountTR):
    TRCode = "CDPCQ04700"
    Name   = "계좌 거래내역"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class QueryType:
        ALL, INOUT, STOCKINOUT, TRADE, FRGEX, ETC = "0", "1", "2", "3", "4", "9"
    class ITEM_CLASS:
        ALL, STOCK, BOND, FUND, FUTURE, FRG_STOCK, FRG_DERIV = "00", "01", "02", "04", "03", "05", "06"
    def __init__(self, 
                 token,
                 QryTp:QueryType,
                 QrySrtDt:str,
                 QryEndDt:str,
                 SrtNo:int,         # 시작번호
                 PdptnCode:str,
                 IsuLgclssCode:ITEM_CLASS,
                 IsuNo:str,        # 종목번호 12
                 ):
        super().__init__(token)
        self.body = {'CDPCQ04700InBlock1': {
                'QryTp': QryTp, 
                'QrySrtDt': QrySrtDt,
                'QryEndDt': QryEndDt, 
                'SrtNo': SrtNo, 
                'PdptnCode': PdptnCode, 
                'IsuLgclssCode': IsuLgclssCode, 
                'IsuNo': IsuNo
            }
        }

    
class CSPAQ00600(_AccountTR):
    TRCode = "CSPAQ00600"
    Name   = "계좌별신용한도조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class LOAN_CODE:
        DIST_LOAN, SELF_LOAN, DIST_LEND, SELF_LEND = "01", "03", "05", "07"
    def __init__(self, 
                 token:str, 
                 LoanDtlClssCode:LOAN_CODE,
                 IsuNo:str,
                 OrdPrc:float,
                 CommdaCode:str='41'):
        super().__init__(token)
        self.body = {'CSPAQ00600InBlock1': {
            'LoanDtlClssCode': LoanDtlClssCode, 'IsuNo': IsuNo, 
            'OrdPrc': OrdPrc, 'CommdaCode': '41'  # 41@xingAPI
            }
        } 

    
class CSPAQ12200(_AccountTR):
    TRCode = "CSPAQ12200"
    Name   = "현물계좌예수금 주문가능금액 총평가 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, BalCreTp='0'):
        super().__init__(token)
        self.body = {'CSPAQ12200InBlock1': {'BalCreTp': BalCreTp}}

    
class CSPAQ12300(_AccountTR):
    TRCode = "CSPAQ12300"
    Name   = "BEP단가조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class BALCRETP:
        ALL, STOCK, FUTURE_SUBSTITUTE = "0", "1", "9"
    class CMSNAPPTPCODE: 
        NO, YES = "0", "1"
    class D2BALBASEQRYTP:
        NO, YES = "0", "1"
    class UPRCTPCODE:
        AVG, BEP = "0", "1"
    def __init__(self, 
                 token:str,
                 BalCreTp:BALCRETP=BALCRETP.ALL,
                 CmsnAppTpCode:CMSNAPPTPCODE=CMSNAPPTPCODE.YES,
                 D2balBaseQryTp:D2BALBASEQRYTP=D2BALBASEQRYTP.NO,
                 UprcTpCode:UPRCTPCODE=UPRCTPCODE.BEP):
        super().__init__(token)
        self.body = {'CSPAQ12300InBlock1': {
            'BalCreTp': BalCreTp, 'CmsnAppTpCode': CmsnAppTpCode, 
            'D2balBaseQryTp': D2balBaseQryTp, 'UprcTpCode': UprcTpCode}
        }


    
class CSPAQ13700(_AccountTR):
    TRCode = "CSPAQ13700"
    Name   = "현물계좌 주문체결내역 조회(API)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, OrdMktCode, BnsTpCode, IsuNo, ExecYn, OrdDt, SrtOrdNo2, BkseqTpCode, OrdPtnCode):
        super().__init__(token)
        self.body = {'CSPAQ13700InBlock1': {'OrdMktCode': OrdMktCode, 'BnsTpCode': BnsTpCode, 'IsuNo': IsuNo, 'ExecYn': ExecYn, 'OrdDt': OrdDt, 'SrtOrdNo2': SrtOrdNo2, 'BkseqTpCode': BkseqTpCode, 'OrdPtnCode': OrdPtnCode}}

    
    
class CSPAQ22200(_AccountTR):
    TRCode = "CSPAQ22200"
    Name   = "현물계좌예수금 주문가능금액 총평가2"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, BalCreTp):
        super().__init__(token)
        self.body = {'CSPAQ22200InBlock1': {'BalCreTp': BalCreTp}}

    
class CSPBQ00200(_AccountTR):
    TRCode = "CSPBQ00200"
    Name   = "현물계좌증거금률별주문가능수량조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, BnsTpCode, IsuNo, OrdPrc):
        super().__init__(token)
        self.body = {'CSPBQ00200InBlock1': {'BnsTpCode': BnsTpCode, 'IsuNo': IsuNo, 'OrdPrc': OrdPrc}}

    
class FOCCQ33600(_AccountTR):
    TRCode = "FOCCQ33600"
    Name   = "주식계좌 기간별수익률 상세"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, QrySrtDt, QryEndDt, TermTp):
        super().__init__(token)
        self.body = {'FOCCQ33600InBlock1': {'QrySrtDt': QrySrtDt, 'QryEndDt': QryEndDt, 'TermTp': TermTp}}

    
class t0150(_AccountTR):
    TRCode = "t0150"
    Name   = "주식당일매매일지/수수료"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, cts_medosu, cts_expcode, cts_price, cts_middiv):
        super().__init__(token)
        self.body = {'t0150InBlock': {'cts_medosu': cts_medosu, 'cts_expcode': cts_expcode, 'cts_price': cts_price, 'cts_middiv': cts_middiv}}

    
class t0151(_AccountTR):
    TRCode = "t0151"
    Name   = "주식당일매매일지/수수료(전일)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, date, cts_medosu, cts_expcode, cts_price, cts_middiv):
        super().__init__(token)
        self.body = {'t0151InBlock': {'date': date, 'cts_medosu': cts_medosu, 'cts_expcode': cts_expcode, 'cts_price': cts_price, 'cts_middiv': cts_middiv}}

    
class t0424(_AccountTR):
    TRCode = "t0424"
    Name   = "주식잔고2"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, prcgb, chegb, dangb, charge, cts_expcode):
        super().__init__(token)
        self.body = {'t0424InBlock': {'prcgb': prcgb, 'chegb': chegb, 'dangb': dangb, 'charge': charge, 'cts_expcode': cts_expcode}}

    
class t0425(_AccountTR):
    TRCode = "t0425"
    Name   = "주식체결/미체결"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, expcode, chegb, medosu, sortgb, cts_ordno):
        super().__init__(token)
        self.body = {'t0425InBlock': {'expcode': expcode, 'chegb': chegb, 'medosu': medosu, 'sortgb': sortgb, 'cts_ordno': cts_ordno}}

    