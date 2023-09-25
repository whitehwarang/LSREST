
from API.Base import BaseTR


class _OrderTR(BaseTR):
    Url     = "/stock/order"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ORDPRCPTNCODE:
    SPECIFIC = "00"                         # 지정가
    MARKET = "03"                           # 시장가
    CONDITIONAL_SPECIFIC = "05"             # 조건부지정가
    MOST_ADVENTAGEOUS_SPECIFIC = "06"       # 최유리지정가
    MOST_PRIORITY_SPECIFIC = "07"           # 최우선지정가
    OVERTIME_PRICE_BEFORE_OPENING = "61"    # 장개시전시간외종가
    OUT_OF_HOURS_CLOSING_PRICE = "81"       # 시간외종가
    OUT_OF_HOURS_SINGLE_PRICE = "82"        # 시간외단일가


class MGNTRNCODE:
    NORMAL = "000"                          # 보통
    NEW_LOAN = "003"                        # 유통/자기융자신규
    NEW_DIST_STOCK_LOAN = "005"             # 유통대주신규
    NEW_SELF_STOCK_LOAN = "007"             # 자기대주신규
    DIST_LOAN_REDEMPTION = "101"            # 유통융자상환
    SELF_LOAN_REDEMPTION = "103"            # 자기융자상환
    DIST_STOCK_LOAN_REDEMPTION = "105"      # 유통대주상환
    SELF_STOCK_LOAN_REDEMPTION = "107"      # 자기대주상환
    REDEMPTION_DEPOSITED_MORTGAGE = "180"   # 예탁담보대출상환(신용)


class ORDCNDITPCODE:
    NONE = "0"
    IOC = "1"
    FOK = "2"


class BNSTPCODE:
    SELL, BUY = "1", "2"


class CSPAT00601(_OrderTR):
    TRCode = "CSPAT00601"
    Name   = "현물주문"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, 
                 token:str, 
                 IsuNo:str, 
                 OrdQty:int, 
                 OrdPrc:float,
                 BnsTpCode:BNSTPCODE, 
                 OrdprcPtnCode:ORDPRCPTNCODE=ORDPRCPTNCODE.MARKET,
                 MgntrnCode:MGNTRNCODE=MGNTRNCODE.NORMAL,
                 LoanDt:str="",
                 OrdCndiTpCode:ORDCNDITPCODE=ORDCNDITPCODE.NONE,
                 ):
        super().__init__(token)
        self.body = {
            'CSPAT00601InBlock1': {
                'IsuNo': IsuNo, 
                'OrdQty': OrdQty, 
                'OrdPrc': OrdPrc, 
                'BnsTpCode': BnsTpCode, 
                'OrdprcPtnCode': OrdprcPtnCode, 
                'MgntrnCode': MgntrnCode, 
                'LoanDt': LoanDt, 
                'OrdCndiTpCode': OrdCndiTpCode
            }
        }

    
class CSPAT00701(_OrderTR):
    TRCode = "CSPAT00701"
    Name   = "현물정정주문"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, 
                 token:str, 
                 OrgOrdNo:str,
                 IsuNo:str,
                 OrdQty:int,
                 OrdPrc:float,
                 OrdprcPtnCode:ORDPRCPTNCODE=ORDPRCPTNCODE.MARKET,
                 ):
        super().__init__(token)
        self.body = {
            'CSPAT00701InBlock1': {
                'OrgOrdNo': OrgOrdNo, 
                'IsuNo': IsuNo, 
                'OrdQty': OrdQty, 
                'OrdprcPtnCode': OrdprcPtnCode, 
                'OrdCndiTpCode': ORDCNDITPCODE.NONE, 
                'OrdPrc': OrdPrc,
            }
        }

    
class CSPAT00801(_OrderTR):
    TRCode = "CSPAT00801"
    Name   = "현물취소주문"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, 
                 token:str, 
                 OrgOrdNo:str,
                 IsuNo:str,
                 OrdQty:int,
                 ):
        super().__init__(token)
        self.body = {
            'CSPAT00801InBlock1': {
                'OrgOrdNo': OrgOrdNo, 
                'IsuNo': IsuNo, 
                'OrdQty': OrdQty,
            }
        }

    