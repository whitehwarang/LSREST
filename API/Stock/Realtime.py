
from .API.base import BaseWSAcc, BaseWSSise


class B7_(BaseWSSise):
    TRCode = "B7_"
    Name   = "ETF호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DH1(BaseWSSise):
    TRCode = "DH1"
    Name   = "KOSPI시간외단일가호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DHA(BaseWSSise):
    TRCode = "DHA"
    Name   = "KOSDAQ시간외단일가호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DK3(BaseWSSise):
    TRCode = "DK3"
    Name   = "KOSDAQ시간외단일가체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DS3(BaseWSSise):
    TRCode = "DS3"
    Name   = "KOSPI시간외단일가체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DVI(BaseWSSise):
    TRCode = "DVI"
    Name   = "시간외단일가VI발동해제"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class H1_(BaseWSSise):
    TRCode = "H1_"
    Name   = "KOSPI호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class H2_(BaseWSSise):
    TRCode = "H2_"
    Name   = "KOSPI장전시간외호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HA_(BaseWSSise):
    TRCode = "HA_"
    Name   = "KOSDAQ호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HB_(BaseWSSise):
    TRCode = "HB_"
    Name   = "KOSDAQ장전시간외호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class I5_(BaseWSSise):
    TRCode = "I5_"
    Name   = "코스피ETF종목실시간NAV"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class IJ_(BaseWSSise):
    TRCode = "IJ_"
    Name   = "지수"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class K1_(BaseWSSise):
    TRCode = "K1_"
    Name   = "KOSPI거래원"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class K3_(BaseWSSise):
    TRCode = "K3_"
    Name   = "KOSDAQ체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class KH_(BaseWSSise):
    TRCode = "KH_"
    Name   = "KOSDAQ프로그램매매종목별"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class KM_(BaseWSSise):
    TRCode = "KM_"
    Name   = "KOSDAQ프로그램매매전체집계"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class KS_(BaseWSSise):
    TRCode = "KS_"
    Name   = "KOSDAQ우선호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class OK_(BaseWSSise):
    TRCode = "OK_"
    Name   = "KOSDAQ거래원"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PH_(BaseWSSise):
    TRCode = "PH_"
    Name   = "KOSPI프로그램매매종목별"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PM_(BaseWSSise):
    TRCode = "PM_"
    Name   = "KOSPI프로그램매매전체집계"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S2_(BaseWSSise):
    TRCode = "S2_"
    Name   = "KOSPI우선호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S3_(BaseWSSise):
    TRCode = "S3_"
    Name   = "KOSPI체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S4_(BaseWSSise):
    TRCode = "S4_"
    Name   = "KOSPI기세"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SC0(BaseWSAcc):
    TRCode = "SC0"
    Name   = "주식주문접수"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SC1(BaseWSAcc):
    TRCode = "SC1"
    Name   = "주식주문체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SC2(BaseWSAcc):
    TRCode = "SC2"
    Name   = "주식주문정정"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SC3(BaseWSAcc):
    TRCode = "SC3"
    Name   = "주식주문취소"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SC4(BaseWSAcc):
    TRCode = "SC4"
    Name   = "주식주문거부"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SHC(BaseWSSise):
    TRCode = "SHC"
    Name   = "상/하한가근접진입"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SHD(BaseWSSise):
    TRCode = "SHD"
    Name   = "상/하한가근접이탈"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SHI(BaseWSSise):
    TRCode = "SHI"
    Name   = "상/하한가진입"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SHO(BaseWSSise):
    TRCode = "SHO"
    Name   = "상/하한가이탈"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class VI_(BaseWSSise):
    TRCode = "VI_"
    Name   = "VI발동해제"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class YJ_(BaseWSSise):
    TRCode = "YJ_"
    Name   = "예상지수"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class YK3(BaseWSSise):
    TRCode = "YK3"
    Name   = "KOSDAQ예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class YS3(BaseWSSise):
    TRCode = "YS3"
    Name   = "KOSPI예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ESN(BaseWSSise):
    TRCode = "ESN"
    Name   = "뉴ELW투자지표민감도"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class h2_(BaseWSSise):
    TRCode = "h2_"
    Name   = "ELW장전시간외호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class h3_(BaseWSSise):
    TRCode = "h3_"
    Name   = "ELW호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class k1_(BaseWSSise):
    TRCode = "k1_"
    Name   = "ELW거래원"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class s2_(BaseWSSise):
    TRCode = "s2_"
    Name   = "ELW우선호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class s3_(BaseWSSise):
    TRCode = "s3_"
    Name   = "ELW체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class s4_(BaseWSSise):
    TRCode = "s4_"
    Name   = "ELW기세"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Ys3(BaseWSSise):
    TRCode = "Ys3"
    Name   = "ELW예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


