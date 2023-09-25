import time
import asyncio
from .Const import BASE_URL_WEBSOCKET


class BaseTR:
    """TR을 요청(request-post) 하기 위한 Base Class """
    TRCode = ""
    Url = ""
    ContentType = "application/json; charset=UTF-8"
    TRLimitPerSecond = 0
    TRCnt = 0
    PrevTime = time.time()
    def __init__(self, token, tr_cont="N", tr_cont_key="", *args, **kwargs):
        self.header = {
            'content-type':     self.ContentType, 
            'authorization':    f"Bearer {token}",
            'tr_cd':            self.TRCode,
            "tr_cont":          tr_cont,
            "tr_cont_key":      tr_cont_key,
            #"mac_address":      "",  # 법인인 경우에만 사용
        }
    @classmethod
    def reset_limit(cls):
        cls.PrevTime = time.time()
        cls.TRCnt = 0

    @classmethod
    def keep_limit(cls):
        if not cls.TRLimitPerSecond or not cls.TRCnt: 
            return 
        now = time.time()
        if now - cls.PrevTime >= 1.0:
            #print("testprint :: if now - cls.PrevTime >= 1:")
            cls.reset_limit()
        elif cls.TRCnt >= cls.TRLimitPerSecond:
            #print("testprint :: elif cls.TRCnt >= cls.TRLimitPerSecond: await asyncio.sleep()")
            time.sleep(cls.PrevTime + 1.0 - now + 0.001)
            cls.reset_limit()
        return

    @classmethod
    def incr_cnt(cls):
        cls.TRCnt += 1

    @classmethod
    async def async_keep_limit(cls):
        if not cls.TRLimitPerSecond or not cls.TRCnt: 
            return 
        lock = asyncio.Lock()
        async with lock:
            now = time.time()
            if now - cls.PrevTime >= 1.0:
                #print("testprint :: if now - cls.PrevTime >= 1:")
                cls.reset_limit()
            elif cls.TRCnt >= cls.TRLimitPerSecond:
                #print("testprint :: elif cls.TRCnt >= cls.TRLimitPerSecond: asyncio.sleep()")
                await asyncio.sleep(cls.PrevTime + 1.0 - now + 0.001)
                cls.reset_limit()
        return

    @classmethod
    async def async_incr_cnt(cls):
        cls.TRCnt += 1



class BaseWS:
    """웹 소켓 연결을 위한 Base Class """
    TRCode = ""
    Url    = f"{BASE_URL_WEBSOCKET}/websocket"
    class TR_TYPE:
        REG_ACCOUNT, UNREG_ACCOUNT, REG_RT_SISE, UNREG_RT_SISE = tuple(str(i) for i in range(1, 4+1))
    TRType: TR_TYPE = ""
    def __init__(self, token, tr_key, unreg=False):
        """
        <header>
        token : ACCESS_TOKEN
        tr_type : TR타입 (1:계좌등록, 2계좌해제, 3:실시간 시세등록, 4:실시간 시세해제)
        <Body>
        tr_cd : 실시간 TR 코드 (계좌등록/해제 일경우 필수값 아님)
        tr_key : 실시간 TR 코드 값 (계좌등록/해제 일경우 필수값 아님)
        """
        self.tr_key = tr_key
        self.unreg = unreg
        self.connection = False
        if unreg:
            if self.TRType == self.TR_TYPE.REG_ACCOUNT:
                trtype = self.TR_TYPE.UNREG_ACCOUNT
            elif self.TRType == self.TR_TYPE.REG_RT_SISE:
                trtype = self.TR_TYPE.UNREG_RT_SISE
        else:
            trtype = self.TRType
        self.header = {'token': token, 'tr_type': trtype}
        self.body = {'tr_cd': self.TRCode, 'tr_key': tr_key}
    def __repr__(self):
        return f"<Realtime instance:: tr_type: '{self.TRType}', tr_cd: '{self.TRCode}', tr_key: '{self.tr_key}', unreg: {self.unreg}>"
    def into_dict(self):
        return {"header": self.header, "body": self.body}
    def disconnect(self):
        self.connection = False
    def connect(self):
        self.connection = True
    def switch_unreg(self):
        self.unreg = True
        if self.TRType == self.TR_TYPE.REG_ACCOUNT:
            trtype = self.TR_TYPE.UNREG_ACCOUNT
        elif self.TRType == self.TR_TYPE.REG_RT_SISE:
            trtype = self.TR_TYPE.UNREG_RT_SISE
        self.TRType = trtype
        self.header['tr_type'] = trtype



class BaseWSAcc(BaseWS):
    """ 계좌등록/계좌해제용 WebSocket Superclass """
    TRType: BaseWS.TR_TYPE = BaseWS.TR_TYPE.REG_ACCOUNT
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BaseWSSise(BaseWS):
    """ 시세등록/시세해제용 WebSocket Superclass """
    TRType: BaseWS.TR_TYPE = BaseWS.TR_TYPE.REG_RT_SISE
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

