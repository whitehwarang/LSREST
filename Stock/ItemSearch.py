
from ..Base import BaseTR


class _ItemSearchTR(BaseTR):
    Url     = "/stock/item-search"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t1809(_ItemSearchTR):
    TRCode = "t1809"
    Name   = "신호조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, gubun, jmGb, jmcode, cts):
        super().__init__(token)
        self.body = {'t1809InBlock': {'gubun': gubun, 'jmGb': jmGb, 'jmcode': jmcode, 'cts': cts}}

    
class t1825(_ItemSearchTR):
    TRCode = "t1825"
    Name   = "종목Q클릭검색(씽큐스마트)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, search_cd, gubun):
        super().__init__(token)
        self.body = {'t1825InBlock': {'search_cd': search_cd, 'gubun': gubun}}

    
class t1826(_ItemSearchTR):
    TRCode = "t1826"
    Name   = "종목Q클릭검색리스트조회(씽큐스마트)"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, search_gb):
        super().__init__(token)
        self.body = {'t1826InBlock': {'search_gb': search_gb}}

    