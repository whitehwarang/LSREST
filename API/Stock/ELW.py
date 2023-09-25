
from API.Base import BaseTR


class _ELWTR(BaseTR):
    Url     = "/stock/elw"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1950(_ELWTR):
    TRCode = "t1950"
    Name   = "ELW현재가(시세)조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1950InBlock': {'shcode': shcode}}

    
class t1951(_ELWTR):
    TRCode = "t1951"
    Name   = "ELW시간대별체결조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode, cvolume, starttime, endtime, cts_time):
        super().__init__(token)
        self.body = {'t1951InBlock': {'shcode': shcode, 'cvolume': cvolume, 'starttime': starttime, 'endtime': endtime, 'cts_time': cts_time}}

    
class t1954(_ELWTR):
    TRCode = "t1954"
    Name   = "ELW일별주가"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode, date, cnt):
        super().__init__(token)
        self.body = {'t1954InBlock': {'shcode': shcode, 'date': date, 'cnt': cnt}}

    
class t1956(_ELWTR):
    TRCode = "t1956"
    Name   = "ELW현재가(확정지급액)조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1956InBlock': {'shcode': shcode}}

    
class t1958(_ELWTR):
    TRCode = "t1958"
    Name   = "ELW종목비교"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode1, shcode2):
        super().__init__(token)
        self.body = {'t1958InBlock': {'shcode1': shcode1, 'shcode2': shcode2}}

    
class t1959(_ELWTR):
    TRCode = "t1959"
    Name   = "LP대상종목정보조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1959InBlock': {'shcode': shcode}}

    
class t1960(_ELWTR):
    TRCode = "t1960"
    Name   = "ELW등락율상위"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun, ggubun, itemcode, lastdate, exgubun, sprice, eprice, volume, sjanday, ejanday, idx):
        super().__init__(token)
        self.body = {'t1960InBlock': {'gubun': gubun, 'ggubun': ggubun, 'itemcode': itemcode, 'lastdate': lastdate, 'exgubun': exgubun, 'sprice': sprice, 'eprice': eprice, 'volume': volume, 'sjanday': sjanday, 'ejanday': ejanday, 'idx': idx}}

    
class t1961(_ELWTR):
    TRCode = "t1961"
    Name   = "ELW거래량상위"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun, ggubun, itemcode, lastdate, exgubun, sprice, eprice, volume, sjanday, ejanday, idx):
        super().__init__(token)
        self.body = {'t1961InBlock': {'gubun': gubun, 'ggubun': ggubun, 'itemcode': itemcode, 'lastdate': lastdate, 'exgubun': exgubun, 'sprice': sprice, 'eprice': eprice, 'volume': volume, 'sjanday': sjanday, 'ejanday': ejanday, 'idx': idx}}

    
class t1964(_ELWTR):
    TRCode = "t1964"
    Name   = "ELW전광판"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, item, issuercd, lastmonth, elwopt, atmgubun, elwtype, settletype, elwexecgubun, fromrat, torat, volume):
        super().__init__(token)
        self.body = {'t1964InBlock': {'item': item, 'issuercd': issuercd, 'lastmonth': lastmonth, 'elwopt': elwopt, 'atmgubun': atmgubun, 'elwtype': elwtype, 'settletype': settletype, 'elwexecgubun': elwexecgubun, 'fromrat': fromrat, 'torat': torat, 'volume': volume}}

    
class t1966(_ELWTR):
    TRCode = "t1966"
    Name   = "ELW거래대금상위"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, gubun, ggubun, itemcode, lastdate, exgubun, sprice, eprice, volume, sjanday, ejanday, idx):
        super().__init__(token)
        self.body = {'t1966InBlock': {'gubun': gubun, 'ggubun': ggubun, 'itemcode': itemcode, 'lastdate': lastdate, 'exgubun': exgubun, 'sprice': sprice, 'eprice': eprice, 'volume': volume, 'sjanday': sjanday, 'ejanday': ejanday, 'idx': idx}}

    
class t1969(_ELWTR):
    TRCode = "t1969"
    Name   = "ELW지표검색"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, chkitem, cbitem, chkissuer, cbissuer, chkcallput, cbcallput, chkexec, cbexec, chktype, cbtype, chksettle, cbsettle, chklast, cblast, chkelwexec, elwexecs, elwexece, chkvolume, volumes, volumee, chkrate, rates, ratee, chkpremium, premiums, premiume, chkparity, paritys, paritye, chkberate, berates, beratee, chkcapt, capts, capte, chkegearing, egearings, egearinge, chkgearing, gearings, gearinge, chkdelta, deltas, deltae, chktheta, thetas, thetae, chkduedate, duedates, duedatee, onetickgubun, lp_liquidity, chklp_code, lp_code, chkkoba, cbkoba):
        super().__init__(token)
        self.body = {'t1969InBlock': {'chkitem': chkitem, 'cbitem': cbitem, 'chkissuer': chkissuer, 'cbissuer': cbissuer, 'chkcallput': chkcallput, 'cbcallput': cbcallput, 'chkexec': chkexec, 'cbexec': cbexec, 'chktype': chktype, 'cbtype': cbtype, 'chksettle': chksettle, 'cbsettle': cbsettle, 'chklast': chklast, 'cblast': cblast, 'chkelwexec': chkelwexec, 'elwexecs': elwexecs, 'elwexece': elwexece, 'chkvolume': chkvolume, 'volumes': volumes, 'volumee': volumee, 'chkrate': chkrate, 'rates': rates, 'ratee': ratee, 'chkpremium': chkpremium, 'premiums': premiums, 'premiume': premiume, 'chkparity': chkparity, 'paritys': paritys, 'paritye': paritye, 'chkberate': chkberate, 'berates': berates, 'beratee': beratee, 'chkcapt': chkcapt, 'capts': capts, 'capte': capte, 'chkegearing': chkegearing, 'egearings': egearings, 'egearinge': egearinge, 'chkgearing': chkgearing, 'gearings': gearings, 'gearinge': gearinge, 'chkdelta': chkdelta, 'deltas': deltas, 'deltae': deltae, 'chktheta': chktheta, 'thetas': thetas, 'thetae': thetae, 'chkduedate': chkduedate, 'duedates': duedates, 'duedatee': duedatee, 'onetickgubun': onetickgubun, 'lp_liquidity': lp_liquidity, 'chklp_code': chklp_code, 'lp_code': lp_code, 'chkkoba': chkkoba, 'cbkoba': cbkoba}}

    
class t1971(_ELWTR):
    TRCode = "t1971"
    Name   = "ELW현재가호가조회"
    TRLimitPerSecond = 3
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1971InBlock': {'shcode': shcode}}

    
class t1972(_ELWTR):
    TRCode = "t1972"
    Name   = "ELW현재가(거래원)조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1972InBlock': {'shcode': shcode}}

    
class t1973(_ELWTR):
    TRCode = "t1973"
    Name   = "ELW시간대별예상체결조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode, cts_time):
        super().__init__(token)
        self.body = {'t1973InBlock': {'shcode': shcode, 'cts_time': cts_time}}

    
class t1974(_ELWTR):
    TRCode = "t1974"
    Name   = "ELW기초자산동일종목"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1974InBlock': {'shcode': shcode}}

    
class t1988(_ELWTR):
    TRCode = "t1988"
    Name   = "기초자산리스트조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, mkt_gb, chk_price, from_price, to_price, chk_vol, from_vol, to_vol, chk_rate, from_rate, to_rate, chk_amt, from_amt, to_amt, chk_up, chk_down):
        super().__init__(token)
        self.body = {'t1988InBlock': {'mkt_gb': mkt_gb, 'chk_price': chk_price, 'from_price': from_price, 'to_price': to_price, 'chk_vol': chk_vol, 'from_vol': from_vol, 'to_vol': to_vol, 'chk_rate': chk_rate, 'from_rate': from_rate, 'to_rate': to_rate, 'chk_amt': chk_amt, 'from_amt': from_amt, 'to_amt': to_amt, 'chk_up': chk_up, 'chk_down': chk_down}}

    
class t8431(_ELWTR):
    TRCode = "t8431"
    Name   = "ELW종목조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t8431InBlock': {'dummy': dummy}}

    
class t9905(_ELWTR):
    TRCode = "t9905"
    Name   = "기초자산리스트조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t9905InBlock': {'dummy': dummy}}

    
class t9907(_ELWTR):
    TRCode = "t9907"
    Name   = "만기월조회"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t9907InBlock': {'dummy': dummy}}

    
class t9942(_ELWTR):
    TRCode = "t9942"
    Name   = "ELW마스터조회API용"
    TRLimitPerSecond = 2
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t9942InBlock': {'dummy': dummy}}

    