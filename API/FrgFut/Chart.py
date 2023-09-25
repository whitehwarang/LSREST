
from API.Base import BaseTR


class _ChartTR(BaseTR):
    Url     = "/overseas-futureoption/chart"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class o3103(_ChartTR):
    TRCode = "o3103"
    Name   = "해외선물차트 분봉 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, ncnt, readcnt, cts_date, cts_time):
        super().__init__(token)
        self.body = {'o3103InBlock': {'shcode': shcode, 'ncnt': ncnt, 'readcnt': readcnt, 'cts_date': cts_date, 'cts_time': cts_time}}

    
class o3108(_ChartTR):
    TRCode = "o3108"
    Name   = "해외선물차트(일주월) 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun, qrycnt, sdate, edate, cts_date):
        super().__init__(token)
        self.body = {'o3108InBlock': {'shcode': shcode, 'gubun': gubun, 'qrycnt': qrycnt, 'sdate': sdate, 'edate': edate, 'cts_date': cts_date}}

    
class o3117(_ChartTR):
    TRCode = "o3117"
    Name   = "해외선물 차트 NTick 체결 조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, ncnt, qrycnt, cts_seq, cts_daygb):
        super().__init__(token)
        self.body = {'o3117InBlock': {'shcode': shcode, 'ncnt': ncnt, 'qrycnt': qrycnt, 'cts_seq': cts_seq, 'cts_daygb': cts_daygb}}

    
class o3139(_ChartTR):
    TRCode = "o3139"
    Name   = "해외선물옵션차트용NTick(고정형)-API용"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, token, mktgb, shcode, ncnt, qrycnt, cts_seq, cts_daygb):
        super().__init__(token)
        self.body = {'o3139InBlock': {'mktgb': mktgb, 'shcode': shcode, 'ncnt': ncnt, 'qrycnt': qrycnt, 'cts_seq': cts_seq, 'cts_daygb': cts_daygb}}

    