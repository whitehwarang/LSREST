
from ..Base import BaseWSAcc, BaseWSSise


"""""
25.04.03. 공지사항
1) 스마트 주문은 별도 제공하지 않습니다.
2) 신규 실시간 등록시 InBlock필드의 사이즈에 맞춰 입력하셔야 합니다.  ex) US3의 ex_shcode 크기가 10인 경우 'U078020   '으로 입력
"""


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


class NS3(BaseWSSise):
    TRCode = "NS3"
    Name   = "(NXT)체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NH1(BaseWSSise):
    TRCode = "NH1"
    Name   = "(NXT)호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NS2(BaseWSSise):
    TRCode = "NS2"
    Name   = "(NXT)우선호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NYS(BaseWSSise):
    TRCode = "NYS"
    Name   = "(NXT)예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NVI(BaseWSSise):
    TRCode = "NVI"
    Name   = "VI 발동 해제"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NK1(BaseWSSise):
    TRCode = "NK1"
    Name   = "(NXT)거래원"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NPH(BaseWSSise):
    TRCode = "NPH"
    Name   = "(NXT)프로그램매매종목별"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NPM(BaseWSSise):
    TRCode = "NPM"
    Name   = "(NXT)프로그램매매전체집계"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NBT(BaseWSSise):
    TRCode = "NBT"
    Name   = "(NXT)시간대별투자자매매추이"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NBM(BaseWSSise):
    TRCode = "NBM"
    Name   = "(NXT)업종별투자자별매매현황"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class US3(BaseWSSise):
    TRCode = "US3"
    Name   = "(통합)체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UH1(BaseWSSise):
    TRCode = "UH1"
    Name   = "(통합)호가잔량"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class US2(BaseWSSise):
    TRCode = "US2"
    Name   = "(통합)우선호가"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UYS(BaseWSSise):
    TRCode = "UYS"
    Name   = "(통합)예상체결"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UPH(BaseWSSise):
    TRCode = "UPH"
    Name   = "(통합)프로그램매매종목별"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UK1(BaseWSSise):
    TRCode = "UK1"
    Name   = "(통합)거래원"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UBT(BaseWSSise):
    TRCode = "UBT"
    Name   = "(통합)시간대별투자자매매추이"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UBM(BaseWSSise):
    TRCode = "UBM"
    Name   = "업종별투자자별매매현황"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UPM(BaseWSSise):
    TRCode = "UPM"
    Name   = "(통합)프로그램매매전체집계"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UVI(BaseWSSise):
    TRCode = "UVI"
    Name   = "(통합)VI발동해제"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AFR(BaseWSSise):
    TRCode = 'AFR'
    Name   = 'API사용자조건검색실시간'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

