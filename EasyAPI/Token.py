import os
import datetime
import json
import API
from API import Util

RECENT_ACCESS_TOKEN_FILE = "_recent_access_token.json"


def _read_recent_token_info(filepath=RECENT_ACCESS_TOKEN_FILE):
    """ token_info 로드 """
    # RECENT_ACCESS_TOKEN_FILE 파일 없으면 생성
    if not os.path.isfile(filepath):
        with open(filepath, mode='w', encoding='utf8') as f: 
            f.write("{}")
    # read as dict
    with open(filepath, mode='r', encoding='utf8') as f:
        res = json.load(f)
    return res


def _write_recent_token_info(dict_like_obj, filepath=RECENT_ACCESS_TOKEN_FILE):
    """ token_info 저장 """
    with open(filepath, encoding='utf8', mode='w') as f:
        json.dump(dict_like_obj, f)


def issue_token(appkey, appsecretkey):
    """ 동기식 토큰 발행
        (만료되었으면) 토큰을 발행받는다. (만료되지 않았으면) 저장된 토큰을 불러온다.
    """
    # RECENT_ACCESS_TOKEN_FILE 읽기
    recent_token_info = _read_recent_token_info(RECENT_ACCESS_TOKEN_FILE)

    # 저장된 값들이 없거나, timestamp상으로 토큰이 expiration(만료)되면 새로 RQ
    now = datetime.datetime.today().timestamp()
    if  recent_token_info.get("access_token") is None   or \
        recent_token_info.get("timestamp") is None      or \
        recent_token_info.get("expires_in") is None     or \
        (now > recent_token_info.get("timestamp") + recent_token_info.get('expires_in')):
        tr_auth = API.OAuth.IssueToken(appkey, appsecretkey)
        recent_token_info = Util.rq_tr(tr_auth)
        recent_token_info['timestamp'] = datetime.datetime.today().timestamp()
        # 저장
        _write_recent_token_info(dict_like_obj=recent_token_info, filepath=RECENT_ACCESS_TOKEN_FILE)
    return recent_token_info



async def async_issue_token(session, appkey, appsecretkey):
    """ 비동기식 토큰 발행
        (만료되었으면) 토큰을 발행받는다. (만료되지 않았으면) 저장된 토큰을 불러온다.
    """

    # RECENT_ACCESS_TOKEN_FILE 읽기
    recent_token_info = _read_recent_token_info(RECENT_ACCESS_TOKEN_FILE)

    # 저장된 값들이 없거나, timestamp상으로 토큰이 expiration(만료)되면 새로 RQ
    now = datetime.datetime.today().timestamp()
    if  recent_token_info.get("access_token") is None   or \
        recent_token_info.get("timestamp") is None      or \
        recent_token_info.get("expires_in") is None     or \
        (now > recent_token_info.get("timestamp") + recent_token_info.get('expires_in')):
        tr_auth = API.OAuth.IssueToken(appkey, appsecretkey)
        recent_token_info = await Util.async_rq_tr(session, tr_auth)
        recent_token_info['timestamp'] = datetime.datetime.today().timestamp()
        # 저장
        _write_recent_token_info(dict_like_obj=recent_token_info, filepath=RECENT_ACCESS_TOKEN_FILE)
    return recent_token_info

