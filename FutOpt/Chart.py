
from ..Base import BaseTR


class _ChartTR(BaseTR):
    Url     = "/futureoption/chart"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t2209(_ChartTR):
    TRCode = "t2209"
    Name   = "선물옵션틱분별체결조회챠트"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, focode, cgubun, bgubun, cnt):
        super().__init__(token)
        self.body = {'t2209InBlock': {'focode': focode, 'cgubun': cgubun, 'bgubun': bgubun, 'cnt': cnt}}

    
class t8414(_ChartTR):
    TRCode = "t8414"
    Name   = "선물옵션차트(틱/n틱)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, ncnt, qrycnt, nday, sdate, stime, edate, etime, cts_date, cts_time, comp_yn):
        super().__init__(token)
        self.body = {'t8414InBlock': {'shcode': shcode, 'ncnt': ncnt, 'qrycnt': qrycnt, 'nday': nday, 'sdate': sdate, 'stime': stime, 'edate': edate, 'etime': etime, 'cts_date': cts_date, 'cts_time': cts_time, 'comp_yn': comp_yn}}

    
class t8415(_ChartTR):
    TRCode = "t8415"
    Name   = "선물/옵션챠트(N분)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, ncnt, qrycnt, nday, sdate, stime, edate, etime, cts_date, cts_time, comp_yn):
        super().__init__(token)
        self.body = {'t8415InBlock': {'shcode': shcode, 'ncnt': ncnt, 'qrycnt': qrycnt, 'nday': nday, 'sdate': sdate, 'stime': stime, 'edate': edate, 'etime': etime, 'cts_date': cts_date, 'cts_time': cts_time, 'comp_yn': comp_yn}}

    
class t8416(_ChartTR):
    TRCode = "t8416"
    Name   = "선물/옵션챠트(일주월)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun, qrycnt, sdate, edate, cts_date, comp_yn):
        super().__init__(token)
        self.body = {'t8416InBlock': {'shcode': shcode, 'gubun': gubun, 'qrycnt': qrycnt, 'sdate': sdate, 'edate': edate, 'cts_date': cts_date, 'comp_yn': comp_yn}}

    
class t8429(_ChartTR):
    TRCode = "t8429"
    Name   = "EUREX야간옵션선물틱분별체결조회챠트"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, focode, cgubun, bgubun, cnt):
        super().__init__(token)
        self.body = {'t8429InBlock': {'focode': focode, 'cgubun': cgubun, 'bgubun': bgubun, 'cnt': cnt}}

    