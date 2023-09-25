
from ..Base import BaseWSSise


class BMT(BaseWSSise):
    TRCode = "BMT"
    Name   = "시간대별투자자매매추이"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class CUR(BaseWSSise):
    TRCode = "CUR"
    Name   = "현물정보USD실시간"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class MK2(BaseWSSise):
    TRCode = "MK2"
    Name   = "US지수"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    