
from ..Base import BaseTR


class _TokenManagerTR(BaseTR):
    ContentType = "application/x-www-form-urlencoded"
    def __init__(self):
        self.header = {'content-type': self.ContentType}


class IssueToken(_TokenManagerTR):
    TRCode = "token"
    Url    = "/oauth2/token"
    Name   = "접근토큰 발급"
    TRLimitPerSecond = None
    TRCnt  = 0
    def __init__(self, appkey, appsecretkey):
        super().__init__()
        self.params = {
            'grant_type': "client_credentials", 
            'appkey': appkey, 
            'appsecretkey': appsecretkey, 
            'scope': "oob",
        }


class TOKEN_TYPE_HINT:
    ACCESS_TOKEN  = "access_token"
    REFRESH_TOKEN = "refresh_token"


class RevokeToken(_TokenManagerTR):
    TRCode = "revoke"
    Url    = "/oauth2/revoke"
    Name   = "접근토큰 폐기"
    TRLimitPerSecond = None
    TRCnt  = 0
    def __init__(self, 
                 appkey:str, 
                 appsecretkey:str, 
                 token:str, 
                 token_type_hint:TOKEN_TYPE_HINT=TOKEN_TYPE_HINT.ACCESS_TOKEN):
        super().__init__()
        self.params = {
            'appkey': appkey, 
            'appsecretkey': appsecretkey, 
            'token_type_hint': token_type_hint, 
            'token': token
        }

