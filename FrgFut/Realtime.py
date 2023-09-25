
from ..Base import BaseWSAcc, BaseWSSise


class OVC(BaseWSSise):
    TRCode = "OVC"
    Name   = "해외선물 체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class OVH(BaseWSSise):
    TRCode = "OVH"
    Name   = "해외선물 호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class WOC(BaseWSSise):
    TRCode = "WOC"
    Name   = "해외옵션 체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class WOH(BaseWSSise):
    TRCode = "WOH"
    Name   = "해외옵션 호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class TC1(BaseWSAcc):
    TRCode = "TC1"
    Name   = "해외선물 주문접수"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class TC2(BaseWSAcc):
    TRCode = "TC2"
    Name   = "해외선물 주문응답"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class TC3(BaseWSAcc):
    TRCode = "TC3"
    Name   = "해외선물 주문체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    