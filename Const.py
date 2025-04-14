"""
LS - OPEN API 고정값을 저장하는 파일
"""

# 24.06.01. EBEST 투자증권 --(명칭변경)--> LS투자증권
# BASE_URL_POST = "https://openapi.ebestsec.co.kr:8080"
# BASE_URL_WEBSOCKET = "wss://openapi.ebestsec.co.kr:9443"
# BASE_URL_WEBSOCKET_FOR_TEST = "wss://openapi.ebestsec.co.kr:29443"

BASE_URL_POST = "https://openapi.ls-sec.co.kr:8080"
BASE_URL_WEBSOCKET = "wss://openapi.ls-sec.co.kr:9443"
BASE_URL_WEBSOCKET_FOR_TEST = "wss://openapi.ls-sec.co.kr:29443"

# ACCESS_TOKEN을 파일에 임시 저장
RECENT_ACCESS_TOKEN_FILEPATH = "_recent_access_token.json"


