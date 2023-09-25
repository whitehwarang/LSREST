
from API.Base import BaseTR


class _ETCTR(BaseTR):
    Url     = "/futureoption/etc"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MMDAQ91200(_ETCTR):
    TRCode = "MMDAQ91200"
    Name   = "파생상품증거금율조회"
    TRLimitPerSecond = 1
    TRCnt  = 0
    def __init__(self, token, IsuLgclssCode, IsuMdclssCode):
        super().__init__(token)
        self.body = {'MMDAQ91200InBlock1': {'IsuLgclssCode': IsuLgclssCode, 'IsuMdclssCode': IsuMdclssCode}}

    