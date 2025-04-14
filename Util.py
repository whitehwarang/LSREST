from typing import Optional
import os
import datetime
import json
import asyncio
import aiohttp

from . import OAuth
from . import Async, Sync
from . import Const


def get_now_as_timestamp():  return datetime.datetime.today().timestamp()


class AccessTokenManager:
    """
    AccessToken 관리하는 Context Manager Class.
    사용 예시 - 주식 차트 데이터 요청
        # 아래와 같이 with절로 Access Token에 대한 자원관리 가능
        with api.Util.AccessTokenManager(appkey=appkey, appsecretkey=appsecretkey, session=None, if_save=False) as access_token:
            tr_inst = api.t8410(token=my_token, shcode='005930', qrycnt=100, sdate='20230901', edate='20230926')
            daily_chart = api.Sync.rq_tr(tr_inst)
            print(daily_chart)
        # with 절 종료 시, access_token 자동 폐기(RevokeToken) 수행
    """
    def __init__(self, appkey:str, appsecretkey:str, session:Optional[aiohttp.ClientSession]=None, if_save:bool=False):
        self.__appkey = appkey
        self.__appsecretkey = appsecretkey
        self.__session = session
        self.__if_save = if_save
        self.token_info = {}
    #
    def __enter__(self) -> str:
        """ AccessTokenManager 진입 (동기) """
        # 최근 TOKEN 정보를 저장한 파일을 읽기
        self.token_info = self._read_token_info() if self.__if_save else {}
        # 기존 토큰정보에 이상이 있거나, 만료된 경우 새로 토큰 정보 요청
        if self.__need_to_reissue():
            self.__sync_issue_token()
        return self.token_info['access_token']
    #
    async def __aenter__(self) -> str:
        """ AccessTokenManager 진입 (비동기) """
        # 최근 TOKEN 정보를 저장한 파일을 읽기
        self.token_info = self._read_token_info() if self.__if_save else {}
        if self.__need_to_reissue():
            await self.__async_issue_token()
        return self.token_info['access_token']
    #
    def __exit__(self, exc_type, exc_value, traceback):
        """ AccessTokenManager 닫기 (동기) """  
        self.__sync_revoke_token()
        if exc_type:
            print(exc_type, exc_value, traceback)
    #
    async def __aexit__(self, exc_type, exc_value, traceback):
        """ AccessTokenManager 닫기 (비동기) """
        await self.__async_revoke_token()
        if exc_type:
            print(exc_type, exc_value, traceback)
    #
    def __need_to_reissue(self) -> bool:
        """ 토큰 새발행이 필요한지 여부 확인 """
        return  self.token_info.get("access_token") is None or \
                self.is_token_expired
    #
    def __reset_token_info(self) -> None:
        """ self.token_info을 리셋하고 저장된 파일을 삭제"""
        self.token_info = {}
        if os.path.isfile(Const.RECENT_ACCESS_TOKEN_FILEPATH):
            os.remove(Const.RECENT_ACCESS_TOKEN_FILEPATH)
    #
    def __sync_issue_token(self) -> None:
        """토큰 발행 요청 (동기)"""
        tr_inst = OAuth.IssueToken(self.__appkey, self.__appsecretkey)
        self.token_info: dict = Sync.rq_tr(tr_inst)
        self.token_info['timestamp'] = get_now_as_timestamp()
        print('토큰 발행\t', 'timestamp : ', self.token_info['timestamp'])
        if self.__if_save:  # 저장 flag에 따라 저장
            self._write_token_info()
    #
    async def __async_issue_token(self) -> None:
        """토큰 발행 요청 (비동기)"""
        assert self.__session is not None, "비동기 모드에서는 session을 반드시 설정해야 합니다."
        tr_inst = OAuth.IssueToken(self.__appkey, self.__appsecretkey)
        self.token_info: dict = await Async.rq_tr(session=self.__session, tr_inst=tr_inst)
        self.token_info['timestamp'] = get_now_as_timestamp()
        if self.__if_save:  # 저장 flag에 따라 저장
            with asyncio.Lock():
                self._write_token_info()
    #
    def __sync_revoke_token(self) -> None:
        """ 토큰 폐기 (동기) """
        tr_inst = OAuth.RevokeToken(self.__appkey, self.__appsecretkey, token=self.token_info['access_token'])
        rp = Sync.rq_tr(tr_inst)
        print(rp)
        self.__reset_token_info()
    #
    async def __async_revoke_token(self) -> None:
        """ 토큰 폐기 (비동기) """
        assert self.__session is not None, "비동기 모드에서는 session을 반드시 설정해야 합니다."
        tr_inst = OAuth.RevokeToken(self.__appkey, self.__appsecretkey, token=self.token_info['access_token'])
        rp = await Async.rq_tr(session=self.__session, tr_inst=tr_inst)
        print(rp)
        with asyncio.Lock():
            self.__reset_token_info()
    #
    @property
    def is_token_expired(self) -> bool:
        """ token 만료 여부 확인 """
        if  self.token_info.get('timestamp') is None or \
            self.token_info.get('expires_in') is None:
            return False
        else:
            now = get_now_as_timestamp()
            return now >= self.token_info.get("timestamp") + self.token_info.get('expires_in')
    #
    def _read_token_info(self, filepath=Const.RECENT_ACCESS_TOKEN_FILEPATH) -> dict:
        """  token_info 읽기 """
        if not self.__if_save: return {}
        print("기존 token 파일 읽기 ")
        # Const.RECENT_ACCESS_TOKEN_FILE 주소에 파일 없으면 생성
        if not os.path.isfile(filepath):
            with open(filepath, mode='w', encoding='utf8') as f:
                f.write("{}")
        # dict 타입으로 읽기
        with open(filepath) as f:
            res = json.load(f)
        return res
    #
    def _write_token_info(self, filepath:str=Const.RECENT_ACCESS_TOKEN_FILEPATH) -> None:
        """ token_info 저장 """
        with open(filepath, encoding='utf8', mode='w') as f:
            json.dump(self.token_info, f)


