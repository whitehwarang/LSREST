
from ..Base import BaseWSAcc, BaseWSSise


class C01(BaseWSSise):  # BaseWSAcc??
    TRCode = "C01"
    Name   = "선물주문체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class CD0(BaseWSSise):
    TRCode = "CD0"
    Name   = "상품선물실시간상하한가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


"""
25.06.07. KRX 야간파생 도입에 따라 일부 TR이 삭제됨

class EC0(BaseWSSise):
    TRCode = "EC0"
    Name   = "EUREX연계KP200지수옵션선물체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class EH0(BaseWSSise):
    TRCode = "EH0"
    Name   = "EUREX연계KP200지수옵션선물호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class EU0(BaseWSAcc):
    TRCode = "EU0"
    Name   = "EUX접수"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class EU1(BaseWSAcc):
    TRCode = "EU1"
    Name   = "EUX체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class EU2(BaseWSAcc):
    TRCode = "EU2"
    Name   = "EUX확인"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
"""

    
class FC0(BaseWSSise):
    TRCode = "FC0"
    Name   = "KOSPI200선물체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class FD0(BaseWSSise):
    TRCode = "FD0"
    Name   = "KOSPI200선물실시간상하한가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class FH0(BaseWSSise):
    TRCode = "FH0"
    Name   = "KOSPI200선물호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class FX0(BaseWSSise):
    TRCode = "FX0"
    Name   = "KOSPI200선물가격제한폭확대"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class H01(BaseWSAcc):
    TRCode = "H01"
    Name   = "선물주문정정취소"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class JC0(BaseWSSise):
    TRCode = "JC0"
    Name   = "주식선물체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class JD0(BaseWSSise):
    TRCode = "JD0"
    Name   = "주식선물실시간상하한가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class JH0(BaseWSSise):
    TRCode = "JH0"
    Name   = "주식선물호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class JX0(BaseWSSise):
    TRCode = "JX0"
    Name   = "주식선물가격제한폭확대"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class O01(BaseWSAcc):
    TRCode = "O01"
    Name   = "선물접수"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class OC0(BaseWSSise):
    TRCode = "OC0"
    Name   = "KOSPI200옵션체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class OD0(BaseWSSise):
    TRCode = "OD0"
    Name   = "KOSPI200옵션실시간상하한가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class OH0(BaseWSSise):
    TRCode = "OH0"
    Name   = "KOSPI200옵션호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class OMG(BaseWSSise):
    TRCode = "OMG"
    Name   = "KOSPI200옵션민감도"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class OX0(BaseWSSise):
    TRCode = "OX0"
    Name   = "KOSPI200옵션가격제한폭확대"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class YC3(BaseWSSise):
    TRCode = "YC3"
    Name   = "상품선물예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class YFC(BaseWSSise):
    TRCode = "YFC"
    Name   = "지수선물예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class YJC(BaseWSSise):
    TRCode = "YJC"
    Name   = "주식선물예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class YOC(BaseWSSise):
    TRCode = "YOC"
    Name   = "지수옵션예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class DC0(BaseWSSise):
    TRCode = "DC0"
    Name   = "KRX야간파생 체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class O02(BaseWSSise):
    TRCode = "O02"
    Name   = "KRX야간파생 선물접수"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class C02(BaseWSSise):
    TRCode = "C02"
    Name   = "KRX야간파생 선물체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class DH0(BaseWSSise):
    TRCode = "DH0"
    Name   = "KRX야간파생 호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class H02(BaseWSSise):
    TRCode = "H02"
    Name   = "KRX야간파생 선물정정취소"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class DD0(BaseWSSise):
    TRCode = "DD0"
    Name   = "KRX야간파생 실시간상하한가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class DX0(BaseWSSise):
    TRCode = "DX0"
    Name   = "KRX야간파생 가격제한폭확대"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class DYC(BaseWSSise):
    TRCode = "DYC"
    Name   = "KRX야간파생 예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class DBM(BaseWSSise):
    TRCode = "DBM"
    Name   = "KRX야간파생 투자자매매현황"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#25.06.07. KRX 야간파생 도입에 따라 추가
class DBT(BaseWSSise):
    TRCode = "DBT"
    Name   = "KRX야간파생 투자자별현황"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

