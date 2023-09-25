
from ..Base import BaseTR


class _SectorTR(BaseTR):
    Url     = "/stock/sector"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1531(_SectorTR):
    TRCode = "t1531"
    Name   = "테마별종목"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, tmname, tmcode):
        super().__init__(token)
        self.body = {'t1531InBlock': {'tmname': tmname, 'tmcode': tmcode}}

    
class t1532(_SectorTR):
    TRCode = "t1532"
    Name   = "종목별테마"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, shcode):
        super().__init__(token)
        self.body = {'t1532InBlock': {'shcode': shcode}}

    
class t1533(_SectorTR):
    TRCode = "t1533"
    Name   = "특이테마"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, chgdate):
        super().__init__(token)
        self.body = {'t1533InBlock': {'gubun': gubun, 'chgdate': chgdate}}

    
class t1537(_SectorTR):
    TRCode = "t1537"
    Name   = "테마종목별시세조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, tmcode):
        super().__init__(token)
        self.body = {'t1537InBlock': {'tmcode': tmcode}}

    
class t8425(_SectorTR):
    TRCode = "t8425"
    Name   = "전체테마"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, dummy):
        super().__init__(token)
        self.body = {'t8425InBlock': {'dummy': dummy}}

    