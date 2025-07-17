import time
import asyncio
from .Const import BASE_URL_WEBSOCKET


class _TimeLimit:
    TRLimitPerSecond = 0
    TRCnt = 0
    PrevTime = time.time()
    _lock = asyncio.Lock()

    @classmethod
    def reset_limit(cls):
        """ 그동안 카운트한 요청횟수(TRCnt)를 초기화 """
        cls.PrevTime = time.time()
        cls.TRCnt = 0

    @classmethod
    def incr_cnt(cls):
        """ (동기) 그 간의 요청횟수에 1을 더함 """
        print('incr_cnt')
        cls.TRCnt += 1

    @classmethod
    async def async_incr_cnt(cls):
        """ (비동기) 그 간의 요청횟수에 1을 더함 """
        async with cls._lock:
            cls.TRCnt += 1
    
    @classmethod
    def keep_limit(cls):
        """ (동기) 요청제한을 준수하기 위한 체크메서드 """
        if not cls.TRLimitPerSecond or not cls.TRCnt: 
            return 
        now = time.time()
        if now - cls.PrevTime >= 1.0:
            cls.reset_limit()
        elif cls.TRCnt >= cls.TRLimitPerSecond:
            time.sleep(cls.PrevTime + 1.0 - now + 0.001)
            cls.reset_limit()
        return

    @classmethod
    async def async_keep_limit(cls):
        """ (비동기) 요청제한을 준수하기 위한 체크메서드 """
        if not cls.TRLimitPerSecond or not cls.TRCnt:
            return
        async with cls._lock:
            now = time.time()
            if now - cls.PrevTime >= 1.0:
                cls.reset_limit()
            elif cls.TRCnt >= cls.TRLimitPerSecond:
                await asyncio.sleep(cls.PrevTime + 1.0 - now + 0.001)
                cls.reset_limit()
        return


class BaseTR(_TimeLimit):
    """TR을 요청(request-post) 하기 위한 Base Class """
    TRCode = ""
    Url = ""
    ContentType = "application/json; charset=UTF-8"
    TRLimitPerSecond = 0
    # 25.04.03. 
    # TR : TR 코드별로 요청횟수를 카운트하므로, 
    # BaseTR 상속 클래스 생성 시 공유변수로 선언 O ( TRCnt = 0 기재 O )
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


class BaseWS(_TimeLimit):
    """웹 소켓 연결을 위한 Base Class """
    TRCode = ""
    Name   = ""
    Url    = f"{BASE_URL_WEBSOCKET}/websocket"
    class TR_TYPE:
        REG_ACCOUNT, UNREG_ACCOUNT, REG_RT_SISE, UNREG_RT_SISE = '1', '2', '3', '4'
    TRType: TR_TYPE = ""
    # 25.04.03. 공지사항(2025-03-17)에 따라 
    # WebSocket : TR 코드 구분 없이 요청횟수를 합산하므로, 
    # BaseWS 상속 클래스 생성 시 공유변수로 선언 X ( TRLimitPerSecond = 0, TRCnt = 0 기재 X )
    TRLimitPerSecond = 100
    TRCnt  = 0
    PrevTime = time.time()

    def __init__(self, token: str, tr_key: str, unreg: bool=False):
        """
        <header>
        token : ACCESS_TOKEN
        tr_type : TR타입 (1:계좌등록, 2계좌해제, 3:실시간 시세등록, 4:실시간 시세해제)
        <Body>
        tr_cd : 실시간 TR 코드 
        tr_key : 실시간 TR 코드 값 (계좌등록/해제 일경우 필수값 아님)
        """
        self.tr_key = tr_key
        self.unreg = unreg
        self.connection = False
        trtype = self._switch_unreg() if unreg else self.TRType
        self.header = {'token': token, 'tr_type': trtype}
        self.body = {'tr_cd': self.TRCode, 'tr_key': tr_key}
    
    def __repr__(self):
        return f"<Realtime instance:: tr_type: '{self.TRType}', tr_cd: '{self.TRCode}', name: '{self.Name}', tr_key: '{self.tr_key}', unreg: {self.unreg}>"
    
    def into_dict(self):
        """ websocket_instance 정보를 보내기(send) 위한 형태로 변환 """
        return {"header": self.header, "body": self.body}
    
    def disconnect(self):
        """ websocket_instance.connection = False로 셋팅 """
        self.connection = False
    
    def connect(self):
        """ websocket_instance.connection = True로 셋팅 """
        self.connection = True
    
    def _switch_unreg(self):
        if self.TRType == self.TR_TYPE.REG_ACCOUNT:
            trtype = self.TR_TYPE.UNREG_ACCOUNT
        elif self.TRType == self.TR_TYPE.REG_RT_SISE:
            trtype = self.TR_TYPE.UNREG_RT_SISE
        else:
            trtype = self.TRType
        return trtype

    def switch_unreg(self):
        """ 등록을 위한 websocket instance에서 등록해제(unregister)를 위한 websocket instance로 전환 """
        self.unreg = True
        trtype = self._switch_unreg()
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

