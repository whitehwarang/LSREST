
from API.Base import BaseTR


class _TimeSearchTR(BaseTR):
    Url     = "/etc/time-search"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class t0167(_TimeSearchTR):
    TRCode = "t0167"
    Name   = "서버시간조회"
    TRLimitPerSecond = 10
    TRCnt  = 0
    def __init__(self, token, id=""):
        super().__init__(token)
        self.body = {'t0167InBlock': {'id': id}}

