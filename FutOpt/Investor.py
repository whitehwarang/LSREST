
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


# 25.06.07.  KRX 야간파생 도입에 따라 아래와 같이 사용 TR 추가
class t8462(_InvestorTR):
    TRCode = "t8462"
    Name   = "KRX야간파생 투자자기간별(API용)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, tm_rng, fot_clsf_cd, bsc_asts_id, gubun2, gubun3, from_date, to_date):
        super().__init__(token)
        self.body = {
            't8462InBlock': {
                'tm_rng': tm_rng, 
                'fot_clsf_cd': fot_clsf_cd, 
                'bsc_asts_id': bsc_asts_id, 
                'gubun2': gubun2, 
                'gubun3': gubun3, 
                'from_date': from_date, 
                'to_date': to_date, 
            }
        }


# 25.06.07.  KRX 야간파생 도입에 따라 아래와 같이 사용 TR 추가
class t8463(_InvestorTR):
    TRCode = "t8463"
    Name   = "KRX야간파생 투자자시간대별(API용)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, tm_rng, fot_clsf_cd, bsc_asts_id, cnt, bgubun):
        super().__init__(token)
        self.body = {
            't8463InBlock': {
                'tm_rng': tm_rng, 
                'fot_clsf_cd': fot_clsf_cd, 
                'bsc_asts_id': bsc_asts_id, 
                'cnt': cnt, 
                'bgubun': bgubun, 
            }
        }

