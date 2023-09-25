
from .API.base import BaseWSAcc, BaseWSSise


class BM_(BaseWSSise):
    TRCode = "BM_"
    Name   = "업종별투자자별매매현황"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    