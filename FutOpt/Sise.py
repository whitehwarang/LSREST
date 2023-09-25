
from ..Base import BaseTR


class _SiseTR(BaseTR):
    Url     = "/futureoption/market-data"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t2101(_SiseTR):
    TRCode = "t2101"
    Name   = "선물/옵션현재가(시세)조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, focode):
        super().__init__(token)
        self.body = {'t2101InBlock': {'focode': focode}}

    
class t2105(_SiseTR):
    TRCode = "t2105"
    Name   = "선물/옵션현재가호가조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t2105InBlock': {'shcode': shcode}}

    
class t2106(_SiseTR):
    TRCode = "t2106"
    Name   = "선물/옵션현재가시세메모"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, code, nrec):
        super().__init__(token)
        self.body = {'t2106InBlock': {'code': code, 'nrec': nrec}}

    
class t2201(_SiseTR):
    TRCode = "t2201"
    Name   = "선물옵션시간대별체결조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, focode, cvolume, stime, etime, cts_time):
        super().__init__(token)
        self.body = {'t2201InBlock': {'focode': focode, 'cvolume': cvolume, 'stime': stime, 'etime': etime, 'cts_time': cts_time}}

    
class t2203(_SiseTR):
    TRCode = "t2203"
    Name   = "기간별주가"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, futcheck, date, cts_code, lastdate, cnt):
        super().__init__(token)
        self.body = {'t2203InBlock': {'shcode': shcode, 'futcheck': futcheck, 'date': date, 'cts_code': cts_code, 'lastdate': lastdate, 'cnt': cnt}}

    
class t2210(_SiseTR):
    TRCode = "t2210"
    Name   = "선물옵션시간대별체결조회(단일출력용)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, focode, cvolume, stime, etime):
        super().__init__(token)
        self.body = {'t2210InBlock': {'focode': focode, 'cvolume': cvolume, 'stime': stime, 'etime': etime}}

    
class t2301(_SiseTR):
    TRCode = "t2301"
    Name   = "옵션전광판"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, yyyymm, gubun):
        super().__init__(token)
        self.body = {'t2301InBlock': {'yyyymm': yyyymm, 'gubun': gubun}}

    
class t2405(_SiseTR):
    TRCode = "t2405"
    Name   = "선물옵션호가잔량비율챠트"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, focode, bgubun, nmin, etime, hgubun, cnt, cts_time):
        super().__init__(token)
        self.body = {'t2405InBlock': {'focode': focode, 'bgubun': bgubun, 'nmin': nmin, 'etime': etime, 'hgubun': hgubun, 'cnt': cnt, 'cts_time': cts_time}}

    
class t2421(_SiseTR):
    TRCode = "t2421"
    Name   = "미결제약정추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, focode, bdgubun, nmin, tcgubun, cnt):
        super().__init__(token)
        self.body = {'t2421InBlock': {'focode': focode, 'bdgubun': bdgubun, 'nmin': nmin, 'tcgubun': tcgubun, 'cnt': cnt}}

    
class t2830(_SiseTR):
    TRCode = "t2830"
    Name   = "EUREXKOSPI200옵션선물현재가(시세)조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, focode):
        super().__init__(token)
        self.body = {'t2830InBlock': {'focode': focode}}

    
class t2831(_SiseTR):
    TRCode = "t2831"
    Name   = "EUREXKOSPI200옵션선물호가조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t2831InBlock': {'shcode': shcode}}

    
class t2832(_SiseTR):
    TRCode = "t2832"
    Name   = "EUREX야간옵션선물시간대별체결조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, focode, cvolume, stime, etime, cts_time):
        super().__init__(token)
        self.body = {'t2832InBlock': {'focode': focode, 'cvolume': cvolume, 'stime': stime, 'etime': etime, 'cts_time': cts_time}}

    
class t2833(_SiseTR):
    TRCode = "t2833"
    Name   = "EUREX야간옵션선물기간별추이"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, futcheck, date, cts_code, lastdate, cnt):
        super().__init__(token)
        self.body = {'t2833InBlock': {'shcode': shcode, 'futcheck': futcheck, 'date': date, 'cts_code': cts_code, 'lastdate': lastdate, 'cnt': cnt}}

    
class t2835(_SiseTR):
    TRCode = "t2835"
    Name   = "EUREX옵션선물시세전광판"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, yyyymm, gubun, gmprice, gmsign, gmchange, gmdiff, gmvolume, gmshcode):
        super().__init__(token)
        self.body = {'t2835InBlock': {'yyyymm': yyyymm, 'gubun': gubun, 'gmprice': gmprice, 'gmsign': gmsign, 'gmchange': gmchange, 'gmdiff': gmdiff, 'gmvolume': gmvolume, 'gmshcode': gmshcode}}

    
class t8401(_SiseTR):
    TRCode = "t8401"
    Name   = "주식선물마스터조회(API용)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t8401InBlock': {'dummy': dummy}}

    
class t8402(_SiseTR):
    TRCode = "t8402"
    Name   = "주식선물현재가조회(API용)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, focode):
        super().__init__(token)
        self.body = {'t8402InBlock': {'focode': focode}}

    
class t8403(_SiseTR):
    TRCode = "t8403"
    Name   = "주식선물호가조회(API용)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t8403InBlock': {'shcode': shcode}}

    
class t8404(_SiseTR):
    TRCode = "t8404"
    Name   = "주식선물시간대별체결조회(API용)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, focode, cvolume, stime, etime, cts_time):
        super().__init__(token)
        self.body = {'t8404InBlock': {'focode': focode, 'cvolume': cvolume, 'stime': stime, 'etime': etime, 'cts_time': cts_time}}

    
class t8405(_SiseTR):
    TRCode = "t8405"
    Name   = "주식선물기간별주가(API용)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, futcheck, date, cts_code, lastdate, cnt):
        super().__init__(token)
        self.body = {'t8405InBlock': {'shcode': shcode, 'futcheck': futcheck, 'date': date, 'cts_code': cts_code, 'lastdate': lastdate, 'cnt': cnt}}

    
class t8406(_SiseTR):
    TRCode = "t8406"
    Name   = "주식선물틱분별체결조회(API용)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, focode, cgubun, bgubun, cnt):
        super().__init__(token)
        self.body = {'t8406InBlock': {'focode': focode, 'cgubun': cgubun, 'bgubun': bgubun, 'cnt': cnt}}

    
class t8426(_SiseTR):
    TRCode = "t8426"
    Name   = "상품선물마스터조회(API용)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t8426InBlock': {'dummy': dummy}}

    
class t8427(_SiseTR):
    TRCode = "t8427"
    Name   = "과거데이터시간대별조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, fo_gbn, yyyy, mm, cp_gbn, actprice, focode, dt_gbn, min_term, date, time):
        super().__init__(token)
        self.body = {'t8427InBlock': {'fo_gbn': fo_gbn, 'yyyy': yyyy, 'mm': mm, 'cp_gbn': cp_gbn, 'actprice': actprice, 'focode': focode, 'dt_gbn': dt_gbn, 'min_term': min_term, 'date': date, 'time': time}}

    
class t8432(_SiseTR):
    TRCode = "t8432"
    Name   = "지수선물마스터조회API용"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'t8432InBlock': {'gubun': gubun}}

    
class t8433(_SiseTR):
    TRCode = "t8433"
    Name   = "지수옵션마스터조회API용"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t8433InBlock': {'dummy': dummy}}

    
class t8434(_SiseTR):
    TRCode = "t8434"
    Name   = "선물/옵션멀티현재가조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, qrycnt, focode):
        super().__init__(token)
        self.body = {'t8434InBlock': {'qrycnt': qrycnt, 'focode': focode}}

    
class t8435(_SiseTR):
    TRCode = "t8435"
    Name   = "파생종목마스터조회API용"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'t8435InBlock': {'gubun': gubun}}

    
class t8437(_SiseTR):
    TRCode = "t8437"
    Name   = "CME/EUREX마스터조회(API용)"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'t8437InBlock': {'gubun': gubun}}

    
class t9943(_SiseTR):
    TRCode = "t9943"
    Name   = "지수선물마스터조회API용"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun):
        super().__init__(token)
        self.body = {'t9943InBlock': {'gubun': gubun}}

    
class t9944(_SiseTR):
    TRCode = "t9944"
    Name   = "지수옵션마스터조회API용"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t9944InBlock': {'dummy': dummy}}

    