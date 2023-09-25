
from ..Base import BaseTR


class _ProgramTR(BaseTR):
    Url     = "/stock/program"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1631(_ProgramTR):
    TRCode = "t1631"
    Name   = "프로그램매매종합조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, dgubun, sdate, edate):
        super().__init__(token)
        self.body = {'t1631InBlock': {'gubun': gubun, 'dgubun': dgubun, 'sdate': sdate, 'edate': edate}}

    
class t1632(_ProgramTR):
    TRCode = "t1632"
    Name   = "시간대별프로그램매매추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, gubun1, gubun2, gubun3, date, time):
        super().__init__(token)
        self.body = {'t1632InBlock': {'gubun': gubun, 'gubun1': gubun1, 'gubun2': gubun2, 'gubun3': gubun3, 'date': date, 'time': time}}

    
class t1633(_ProgramTR):
    TRCode = "t1633"
    Name   = "기간별프로그램매매추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, gubun1, gubun2, gubun3, fdate, tdate, gubun4, date):
        super().__init__(token)
        self.body = {'t1633InBlock': {'gubun': gubun, 'gubun1': gubun1, 'gubun2': gubun2, 'gubun3': gubun3, 'fdate': fdate, 'tdate': tdate, 'gubun4': gubun4, 'date': date}}

    
class t1636(_ProgramTR):
    TRCode = "t1636"
    Name   = "종목별프로그램매매동향"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, gubun1, gubun2, shcode, cts_idx):
        super().__init__(token)
        self.body = {'t1636InBlock': {'gubun': gubun, 'gubun1': gubun1, 'gubun2': gubun2, 'shcode': shcode, 'cts_idx': cts_idx}}

    
class t1637(_ProgramTR):
    TRCode = "t1637"
    Name   = "종목별프로그램매매추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun1, gubun2, shcode, date, time, cts_idx):
        super().__init__(token)
        self.body = {'t1637InBlock': {'gubun1': gubun1, 'gubun2': gubun2, 'shcode': shcode, 'date': date, 'time': time, 'cts_idx': cts_idx}}

    
class t1640(_ProgramTR):
    TRCode = "t1640"
    Name   = "프로그램매매종합조회(미니)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'t1640InBlock': {'gubun': gubun}}

    
class t1662(_ProgramTR):
    TRCode = "t1662"
    Name   = "시간대별프로그램매매추이(차트)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, gubun1, gubun3):
        super().__init__(token)
        self.body = {'t1662InBlock': {'gubun': gubun, 'gubun1': gubun1, 'gubun3': gubun3}}

    