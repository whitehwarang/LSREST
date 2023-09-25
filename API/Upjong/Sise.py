
from API.Base import BaseTR


class _SiseTR(BaseTR):
    Url     = "/indtp/market-data"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UPCODE: 
    KOSPI, KOSDAQ, KRX100, KOSPI200, SRI = "001", "301", "501", "101", "515"
    KOSDAQ_PREMIER, KRX_INSURANCE, KRX_TRANSPORT = "404", "516", "517"
    

class t1514(_SiseTR):
    TRCode = "t1514"
    Name   = "업종기간별추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class GUBUN2 : DAILY, WEEKLY, MONTHLY = "1", "2", "3"
    class RATE_GBN : VOLUME, TRADESIZE = "1", "2"
    def __init__(self, 
                 token:str, 
                 upcode:str, 
                 gubun1:str=" ", 
                 gubun2:str=GUBUN2.DAILY, 
                 cts_date:str=" ", 
                 cnt:int=300, 
                 rate_gbn:str=RATE_GBN.TRADESIZE):
        super().__init__(token)
        self.body = {'t1514InBlock': {
                        'upcode': upcode, 
                        'gubun1': gubun1, 
                        'gubun2': gubun2, 
                        'cts_date': cts_date, 
                        'cnt': cnt, 
                        'rate_gbn': rate_gbn,
                        }
                    }


class t8424(_SiseTR):
    TRCode = "t8424"
    Name   = "전체업종"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun1):
        super().__init__(token)
        self.body = {'t8424InBlock': {'gubun1': gubun1}}


class t1485(_SiseTR):
    TRCode = "t1485"
    Name   = "예상지수"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class GUBUN: BEFORE_MARKET, AFTER_MARKET = "1", "2"
    def __init__(self, token, upcode, gubun):
        super().__init__(token)
        self.body = {'t1485InBlock': {'upcode': upcode, 'gubun': gubun}}

    
class t1511(_SiseTR):
    TRCode = "t1511"
    Name   = "업종현재가"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token:str, upcode:str):
        super().__init__(token)
        self.body = {'t1511InBlock': {'upcode': upcode}}


class t1516(_SiseTR):
    TRCode = "t1516"
    Name   = "업종별종목시세"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class GUBUN: KOSPI, KOADAQ, SECTOR = "1", "2", "3"
    def __init__(self, token, upcode, gubun, shcode=" "):
        super().__init__(token)
        self.body = {'t1516InBlock': {'upcode': upcode, 'gubun': gubun, 'shcode': shcode}}

