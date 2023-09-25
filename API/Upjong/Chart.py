
from API.Base import BaseTR


class _ChartTR(BaseTR):
    Url     = "/indtp/chart"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t4203(_ChartTR):
    TRCode = "t4203"
    Name   = "업종챠트(종합)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode, gubun, ncnt, qrycnt, tdgb, sdate, edate, cts_date, cts_time, cts_daygb):
        super().__init__(token)
        self.body = {'t4203InBlock': {
            'shcode': shcode, 
            'gubun': gubun, 
            'ncnt': ncnt, 
            'qrycnt': qrycnt, 
            'tdgb': tdgb, 
            'sdate': sdate, 
            'edate': edate, 
            'cts_date': cts_date, 
            'cts_time': cts_time, 
            'cts_daygb': cts_daygb
            }
        }

    
class t8417(_ChartTR):
    TRCode = "t8417"
    Name   = "업종차트(틱/n틱)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, ncnt, qrycnt, nday, sdate, stime, edate, etime, cts_date, cts_time, comp_yn):
        super().__init__(token)
        self.body = {'t8417InBlock': {
            'shcode': shcode, 
            'ncnt': ncnt, 
            'qrycnt': qrycnt, 
            'nday': nday, 
            'sdate': sdate, 
            'stime': stime, 
            'edate': edate, 
            'etime': etime, 
            'cts_date': cts_date, 
            'cts_time': cts_time, 
            'comp_yn': comp_yn
            }
        }

    
class t8418(_ChartTR):
    TRCode = "t8418"
    Name   = "업종챠트(N분)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, ncnt, qrycnt, nday, sdate, stime, edate, etime, cts_date, cts_time, comp_yn):
        super().__init__(token)
        self.body = {'t8418InBlock': {
            'shcode': shcode, 
            'ncnt': ncnt, 
            'qrycnt': qrycnt, 
            'nday': nday, 
            'sdate': sdate, 
            'stime': stime, 
            'edate': edate, 
            'etime': etime, 
            'cts_date': cts_date, 
            'cts_time': cts_time, 
            'comp_yn': comp_yn
            }
        }
    
class t8419(_ChartTR):
    TRCode = "t8419"
    Name   = "업종챠트(일주월)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun, qrycnt, sdate, edate, cts_date, comp_yn):
        super().__init__(token)
        self.body = {'t8419InBlock': {
            'shcode': shcode, 
            'gubun': gubun, 
            'qrycnt': qrycnt, 
            'sdate': sdate, 
            'edate': edate, 
            'cts_date': cts_date, 
            'comp_yn': comp_yn
            }
        }

    