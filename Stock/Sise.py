from ..Base import BaseTR


class _SiseTR(BaseTR):
    Url     = "/stock/market-data"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1101(_SiseTR):
    TRCode = "t1101"
    Name   = "주식현재가호가조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, code6):
        super().__init__(token)
        self.body = {'t1101InBlock': {'shcode': code6}}

    
class t1102(_SiseTR):
    TRCode = "t1102"
    Name   = "주식현재가(시세)조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, code6):
        super().__init__(token)
        self.body = {'t1102InBlock': {'shcode': code6}}

    
class t1104(_SiseTR):
    TRCode = "t1104"
    Name   = "주식현재가시세메모"
    TRLimitPerSecond = 3
    TRCnt  = 0
    class GUBN:
        SISE, HIGHLOW, PIVOT, MA = tuple(str(i) for i in range(1, 4+1))
    class DAT1:
        OPEN, HIGH, LOW, W_AVG = tuple(str(i) for i in range(1, 4+1))
    class DAT2:
        TODAY, YESTERDAY = "1", "2"
    def __init__(self, 
                 token: str, 
                 code6: str, 
                 nrec: str, 
                 occurs_indx: str,
                 gubn: GUBN,
                 dat1: DAT1,
                 dat2: DAT2):
        super().__init__(token)
        self.body = {
            "t1104InBlock": {"code": code6, "nrec": nrec},
            "t1104InBlock1":{"indx": occurs_indx, "gubn": gubn, "dat1": dat1, "dat2": dat2}
        }
    
    
class t1105(_SiseTR):
    TRCode = "t1105"
    Name   = "주식피봇/디마크조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1105InBlock': {'shcode': shcode}}

    
class t1109(_SiseTR):
    TRCode = "t1109"
    Name   = "시간외체결량"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, code6:str, dan_chetime:str="", idx: int=0):
        super().__init__(token)
        self.body = {
            "t1109InBlock": {
                "shcode":       code6,
                "dan_chetime":  dan_chetime,  # 연속조회시 OutBlock의 동일필드 입력
                "idx":          idx           # 연속조회시 OutBlock의 동일필드 입력
            }
        }
    
class t1301(_SiseTR):
    TRCode = "t1301"
    Name   = "주식시간대별체결조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, 
                 token, 
                 shcode:str, 
                 cvolume:int, 
                 starttime:str="", 
                 endtime:str="", 
                 cts_time:str=""):
        super().__init__(token)
        self.body = {
            "t1301InBlock": {
                "shcode":   shcode,
                "cvolume":  cvolume,    # 거래량 > 특이거래량
                "starttime": starttime, # 장시작시간 이후
                "endtime":  endtime,    # 장종료시간 이전
                "cts_time": cts_time    # 연속조회시 OutBlock의 동일필드 입력
            }
        }
    
class t1302(_SiseTR):
    TRCode = "t1302"
    Name   = "주식분별주가조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class GUBUN:
        S30, M1, M3, M5, M10, M30, M60 = tuple(str(i) for i in range(7))
    def __init__(self,
                 token,
                 code6:str,
                 gubun:str,     # 0:30초 1:1분 2:3분 3:5분 4:10분 5:30분 6:60분
                 time:str=" ",  # 처음 조회시는 Space / 연속 조회시에 이전 조회한 OutBlock의 cts_time 값으로 설정
                 cnt:int=1):    # 1이상 900 이하
        super().__init__(token)
        self.body = {
            "t1302InBlock": {"shcode": code6, "gubun": gubun, "time": time, "cnt": cnt}
        }

    
class t1305(_SiseTR):
    TRCode = "t1305"
    Name   = "기간별주가"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class DWMCODE:
        DAILY, WEEKLY, MONTHLY = tuple(i for i in range(1, 3+1))
    def __init__(self, 
                 token, 
                 code6:str, 
                 dwmcode:DWMCODE,
                 date:str,
                 idx:int=0,
                 cnt:int=1):
        super().__init__(token)
        self.body = {
            "t1305InBlock": {
                "shcode": code6, "dwmcode": dwmcode, "date": date, "idx": idx, "cnt": cnt
            }
        }

    
class t1308(_SiseTR):
    TRCode = "t1308"
    Name   = "주식시간대별체결조회챠트"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, 
                 token: str,
                 code6: str,
                 starttime: str, 
                 endtime: str,
                 bun_term:str):
        super().__init__(token)
        self.body = {
            "t1308InBlock": {
                "shcode": code6, "starttime": starttime, "endtime": endtime, "bun_term": bun_term
            }
        }



class t1310(_SiseTR):
    TRCode = "t1310"
    Name   = "주식당일전일분틱조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    class DAYGB:    TODAY, YESTERDAY = '0', '1'
    class TIMEGB:   MINUTE, TICK = '0', '1'
    def __init__(self, 
                 token:str, 
                 daygb:str, 
                 timegb:str, 
                 shcode:str,
                 endtime:str,
                 cts_time:str):
        super().__init__(token)
        self.body = {'t1310InBlock': {'daygb': daygb, 'timegb': timegb, 'shcode': shcode, 'endtime': endtime, 'cts_time': cts_time}}

    
class t1404(_SiseTR):
    TRCode = "t1404"
    Name   = "관리/불성실/투자유의조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    class GUBUN:    ALL, KOSPI, KOSDAQ = "0", "1", "2"
    class JONGCHK:  관리, 불성실공시, 투자유의, 투자환기 = "1", "2", "3", "4"
    def __init__(self, token:str, gubun:str, jongchk:str, cts_shcode:str):
        super().__init__(token)
        self.body = {'t1404InBlock': {'gubun': gubun,  'jongchk': jongchk, 'cts_shcode': cts_shcode}}

    
class t1405(_SiseTR):
    TRCode = "t1405"
    Name   = "투자경고/매매정지/정리매매조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token:str, gubun:str, jongchk:str, cts_shcode:str):
        super().__init__(token)
        self.body = {'t1404InBlock': {'gubun': gubun,  'jongchk': jongchk, 'cts_shcode': cts_shcode}}

    
class t1410(_SiseTR):
    TRCode = "t1410"
    Name   = "초저유동성조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, cts_shcode):
        super().__init__(token)
        self.body = {'t1410InBlock': {'gubun': gubun, 'cts_shcode': cts_shcode}}

    
class t1422(_SiseTR):
    TRCode = "t1422"
    Name   = "상/하한"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, qrygb, gubun, jnilgubun, sign, jc_num, sprice, eprice, volume, idx):
        super().__init__(token)
        self.body = {'t1422InBlock': {'qrygb': qrygb, 'gubun': gubun, 'jnilgubun': jnilgubun, 'sign': sign, 'jc_num': jc_num, 'sprice': sprice, 'eprice': eprice, 'volume': volume, 'idx': idx}}

    
class t1427(_SiseTR):
    TRCode = "t1427"
    Name   = "상/하한가직전"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, qrygb, gubun, signgubun, diff, jc_num, sprice, eprice, volume, idx, jshex):
        super().__init__(token)
        self.body = {'t1427InBlock': {'qrygb': qrygb, 'gubun': gubun, 'signgubun': signgubun, 'diff': diff, 'jc_num': jc_num, 'sprice': sprice, 'eprice': eprice, 'volume': volume, 'idx': idx, 'jshex': jshex}}

    
class t1442(_SiseTR):
    TRCode = "t1442"
    Name   = "신고/신저가"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, type1, type2, type3, jc_num, sprice, eprice, volume, idx, jc_num2):
        super().__init__(token)
        self.body = {'t1442InBlock': {'gubun': gubun, 'type1': type1, 'type2': type2, 'type3': type3, 'jc_num': jc_num, 'sprice': sprice, 'eprice': eprice, 'volume': volume, 'idx': idx, 'jc_num2': jc_num2}}

    
class t1449(_SiseTR):
    TRCode = "t1449"
    Name   = "가격대별매매비중조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, dategb):
        super().__init__(token)
        self.body = {'t1449InBlock': {'shcode': shcode, 'dategb': dategb}}

    
class t1471(_SiseTR):
    TRCode = "t1471"
    Name   = "시간대별호가잔량추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, gubun, time, cnt):
        super().__init__(token)
        self.body = {'t1471InBlock': {'shcode': shcode, 'gubun': gubun, 'time': time, 'cnt': cnt}}

    
class t1475(_SiseTR):
    TRCode = "t1475"
    Name   = "체결강도추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, vptype, datacnt, date, time, rankcnt, gubun):
        super().__init__(token)
        self.body = {'t1475InBlock': {'shcode': shcode, 'vptype': vptype, 'datacnt': datacnt, 'date': date, 'time': time, 'rankcnt': rankcnt, 'gubun': gubun}}

    
class t1486(_SiseTR):
    TRCode = "t1486"
    Name   = "시간별예상체결가"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode, cts_time, cnt):
        super().__init__(token)
        self.body = {'t1486InBlock': {'shcode': shcode, 'cts_time': cts_time, 'cnt': cnt}}

    
class t1488(_SiseTR):
    TRCode = "t1488"
    Name   = "예상체결가등락율상위조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun, sign, jgubun, jongchk, idx, volume, yesprice, yeeprice, yevolume):
        super().__init__(token)
        self.body = {'t1488InBlock': {
            'gubun': gubun, 'sign': sign, 'jgubun': jgubun, 'jongchk': jongchk, 'idx': idx, 
            'volume': volume, 'yesprice': yesprice, 'yeeprice': yeeprice, 'yevolume': yevolume}}

    
class t8407(_SiseTR):
    TRCode = "t8407"
    Name   = "API용주식멀티현재가조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, nrec, shcode):
        super().__init__(token)
        self.body = {'t8407InBlock': {'nrec': nrec, 'shcode': shcode}}

    
class t9945(_SiseTR):
    TRCode = "t9945"
    Name   = "주식마스터조회API용"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'t9945InBlock': {'gubun': gubun}}

    