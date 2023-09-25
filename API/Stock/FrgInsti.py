
from API.Base import BaseTR


class _Frg_Insti_TR(BaseTR):
    Url     = "/stock/frgr-itt"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1702(_Frg_Insti_TR):
    TRCode = "t1702"
    Name   = "외인기관종목별동향"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, todt, volvalgb, msmdgb, cumulgb, cts_date, cts_idx):
        super().__init__(token)
        self.body = {'t1702InBlock': {'shcode': shcode, 'todt': todt, 'volvalgb': volvalgb, 'msmdgb': msmdgb, 'cumulgb': cumulgb, 'cts_date': cts_date, 'cts_idx': cts_idx}}

    
class t1716(_Frg_Insti_TR):
    TRCode = "t1716"
    Name   = "외인기관종목별동향"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun, fromdt, todt, prapp, prgubun, orggubun, frggubun):
        super().__init__(token)
        self.body = {'t1716InBlock': {'shcode': shcode, 'gubun': gubun, 'fromdt': fromdt, 'todt': todt, 'prapp': prapp, 'prgubun': prgubun, 'orggubun': orggubun, 'frggubun': frggubun}}

    
class t1717(_Frg_Insti_TR):
    TRCode = "t1717"
    Name   = "외인기관종목별동향"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun, fromdt, todt):
        super().__init__(token)
        self.body = {'t1717InBlock': {'shcode': shcode, 'gubun': gubun, 'fromdt': fromdt, 'todt': todt}}

    