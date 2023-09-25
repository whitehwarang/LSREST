
from ..Base import BaseWSSise


class JIF(BaseWSSise):
    TRCode = "JIF"
    Name   = "장운영정보"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class NWS(BaseWSSise):
    TRCode = "NWS"
    Name   = "실시간뉴스제목패킷"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

