
from API.Base import BaseTR


class _DealSourceTR(BaseTR):
    Url     = "/stock/exchange"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1752(_DealSourceTR):
    TRCode = "t1752"
    Name   = "종목별상위회원사"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, traddate1, traddate2, fwgubun1, cts_idx):
        super().__init__(token)
        self.body = {'t1752InBlock': {'shcode': shcode, 'traddate1': traddate1, 'traddate2': traddate2, 'fwgubun1': fwgubun1, 'cts_idx': cts_idx}}

    
class t1764(_DealSourceTR):
    TRCode = "t1764"
    Name   = "회원사리스트"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun1):
        super().__init__(token)
        self.body = {'t1764InBlock': {'shcode': shcode, 'gubun1': gubun1}}

    
class t1771(_DealSourceTR):
    TRCode = "t1771"
    Name   = "종목별회원사추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, tradno, gubun1, traddate1, traddate2, cts_idx, cnt):
        super().__init__(token)
        self.body = {'t1771InBlock': {'shcode': shcode, 'tradno': tradno, 'gubun1': gubun1, 'traddate1': traddate1, 'traddate2': traddate2, 'cts_idx': cts_idx, 'cnt': cnt}}

    