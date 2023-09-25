import datetime
from ..Base import BaseTR


TODAY_STR = datetime.datetime.today().strftime("%Y%m%d")

class _ChartTR(BaseTR):
    Url     = "/stock/chart"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1665(_ChartTR):
    TRCode = "t1665"
    Name   = "기간별투자자매매추이(챠트)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token):
        super().__init__(token)
        self.body = {'t1665InBlock': {'market': '', 'upcode': '', 'gubun2': '', 'gubun3': '', 'from_date': '', 'to_date': ''}}

    
class t8410(_ChartTR):
    TRCode = "t8410"
    Name   = "API전용주식챠트(일주월년)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class GUBUN:
        DAILY, WEEKLY, MONTHLY, YEARLY = tuple(str(i) for i in range(2, 5+1))

    def __init__(self, 
                 token:str, 
                 shcode:str,
                 gubun:GUBUN=GUBUN.DAILY,
                 qrycnt:int=500,   # 압축:2000, 비압축:500
                 sdate:str=" ", 
                 edate:str=TODAY_STR, 
                 cts_date:str=" ", 
                 comp_yn:str="N",  # "Y": 압축, "N": 비압축
                 sujung:str="Y"):  # 수정주가여부 "Y", "N"
        super().__init__(token)
        qrycnt = max(1, min(500, qrycnt))
        self.body = {'t8410InBlock': 
            {
                'shcode':   shcode,  
                'gubun':    gubun, 
                'qrycnt':   qrycnt, 
                'sdate':    sdate, 
                'edate':    edate, 
                'cts_date': cts_date, 
                'comp_yn':  comp_yn, 
                'sujung':   sujung,
            }
        }

    
class t8411(_ChartTR):
    TRCode = "t8411"
    Name   = "주식챠트(틱/n틱)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, 
                 token: str, 
                 code6: str, 
                 ncnt: int=60,  # 단위 n틱
                 qrycnt: int=500,
                 nday: str="1",  # 조회영업일수 ('0': 미사용, '1': 사용)
                 sdate: str=' ',
                 stime: str=" ",
                 edate: str=TODAY_STR,
                 etime: str=" ",
                 cts_date: str=" ",
                 cts_time: str=" ",
                 comp_yn: str="N"):
        super().__init__(token)
        qrycnt = max(1, min(500, qrycnt))
        self.body = {'t8411InBlock': {
            'shcode': code6, 
            'ncnt': ncnt, 
            'qrycnt': qrycnt, 
            'nday': nday, 
            'sdate': sdate, 
            'stime': stime, 
            'edate': edate, 
            'etime': etime, 
            'cts_date': cts_date, 
            'cts_time': cts_time, 
            'comp_yn': comp_yn,
            }
        }

    
class t8412(_ChartTR):
    TRCode = "t8412"
    Name   = "주식챠트(N분)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, 
                 token: str, 
                 shcode: str, 
                 ncnt: int=1,  # 단위 n분
                 qrycnt: int=500,
                 nday: str="1",  # 조회영업일수 ('0': 미사용, '1': 사용)
                 sdate: str=' ',
                 stime: str=" ",
                 edate: str=TODAY_STR,
                 etime: str=" ",
                 cts_date: str=" ",
                 cts_time: str=" ",
                 comp_yn: str="N"):
        super().__init__(token)
        qrycnt = max(1, min(500, qrycnt))
        self.body = {'t8412InBlock': {
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
            'comp_yn': comp_yn,
            }
        }


    