
from ..Base import BaseTR


class _InvestorTR(BaseTR):
    Url     = "/futureoption/investor"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t2541(_InvestorTR):
    TRCode = "t2541"
    Name   = "상품선물투자자매매동향(실시간)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, eitem, market, upcode, gubun1, gubun2, cts_time, cts_idx, cnt):
        super().__init__(token)
        self.body = {'t2541InBlock': {'eitem': eitem, 'market': market, 'upcode': upcode, 'gubun1': gubun1, 'gubun2': gubun2, 'cts_time': cts_time, 'cts_idx': cts_idx, 'cnt': cnt}}

    
class t2545(_InvestorTR):
    TRCode = "t2545"
    Name   = "상품선물투자자매매동향(챠트용)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, eitem, sgubun, upcode, nmin, cnt, bgubun):
        super().__init__(token)
        self.body = {'t2545InBlock': {'eitem': eitem, 'sgubun': sgubun, 'upcode': upcode, 'nmin': nmin, 'cnt': cnt, 'bgubun': bgubun}}

    