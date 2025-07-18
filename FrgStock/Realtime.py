
from ..Base import BaseWSAcc, BaseWSSise


class AS0(BaseWSAcc):
    TRCode = "AS0"
    Name   = "해외주식주문접수(미국)"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class AS1(BaseWSAcc):
    TRCode = "AS1"
    Name   = "해외주식주문체결(미국)"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class AS2(BaseWSAcc):
    TRCode = "AS2"
    Name   = "해외주식주문정정(미국)"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


class AS3(BaseWSAcc):
    TRCode = "AS3"
    Name   = "해외주식주문취소(미국)"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


class AS4(BaseWSAcc):
    TRCode = "AS4"
    Name   = "해외주식주문거부(미국)"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


class AS0(BaseWSSise):
    TRCode = "AS0"
    Name   = "해외주식 호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


class AS0(BaseWSSise):
    TRCode = "AS0"
    Name   = "해외주식 체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)