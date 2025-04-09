# Update History
- (25.04.03) 추가된 TR 반영(NXT 등), 초당 실시간(Realtime;WebSocket) 등록제한 설정, 일부 코드 정리
- (25.04.09) 주석(comment) 수정 및 dependancy 정의istory
- (25.04.03) 추가된 TR 반영(NXT 등), 초당 실시간(Realtime;WebSocket) 등록제한 설정, 일부 코드 정리
- (25.04.09) 주석(comment) 수정 및 dependancy 명시

# LSREST
LS(구.eBest) 투자증권의 RESTful OpenAPI(https://openapi.ls-sec.co.kr/intro)를 쉽게 이용할수 있게끔 하는 python-package 입니다.
비동기식(Asynchronously) 및 동기식(Synchronously) 모두 이용 가능하며, 
아래 예제 코드(example code)를 참고하여 사용할 수 있습니다.

## Requirement 참고
- **Python Version:** Python 3.9에서 테스트하였습니다.
- **Dependencies:** 이 프로젝트를 실행하기 위해서는 다음 Python 패키지들이 필요하며, 파이썬 환경에서 아래 명령어로 설치 가능합니다.
 - requests
 - aiohttp
 - websockets  
```bash
  pip install requests aiohttp websockets

## 이용 방법
일반적인 순서는 다음과 같습니다.
1. 요청하고자 하는 tr instance를 생성한다.
2. tr을 동기식/비동기식으로 요청한다.
3. 데이터를 수신받아 처리한다.

## 동기/비동기
동기식 요청(request)은 함수 parameter로 session이 필요치 않으나, 
비동기식 요청(request)은 반드시 session이 함수 parameter로 전달되어야 합니다.

## 웹소켓(websocket)을 이용한 실시간조회
웹소켓은 동기식 요청이 불가하며, 비동기식으로만 요청할 수 있습니다.

## 연속조회 관련사항
'cts_'로 시작하는 attribute가 있는 tr만 연속조회가 가능하게 구현되어 있으며,
cts_로 시작하지 않는 attribute로 연속조회가 구현된 경우, 별도로 로직을 구현하셔야 합니다. (Base.py 파일 참조)

## EasyAPI 디렉토리
EasyAPI 디렉토리 API를 빠르고 쉽게 꺼내쓸 수 있도록 개인적으로 작성해둔 공간입니다.
API를 custum으로 사용하고 싶으신 경우, EasyAPI에 작성하셔서 쓰시면 됩니다.


## example code
### how to request tr asynchronously
```python
import aiohttp
import LSREST as api

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."

async def main():
    async with aiohttp.ClientSession(base_url=BASE_URL_POST) as session:
        # 1. tr 생성
        tr_inst = api.IssueToken(appkey, appsecretkey)
        # 2. 비동기로 tr 요청
        token_info = await api.Async.rq_tr(session=session, tr_inst=tr_inst)
        # 3. 토큰 추출
        my_token = token_info['access_token']

        # 1. tr 생성
        tr_inst = api.t8410(token=my_token, shcode='005930', qrycnt=1000, sdate='20200101', edate='20230926')
        # 2. 비동기로 tr 요청
        daily_chart = await api.Async.rq_tr(session=session, tr_inst=tr_inst)
        # 3. 수신한 데이터 출력
        print(daily_chart)
```


### how to request tr synchronously

```python
import LSREST as api

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."

def main():
    # 1. tr 생성
    tr_inst = api.IssueToken(appkey, appsecretkey)
    # 2. 동기로 tr 요청
    token_info = api.Sync.rq_tr(tr_inst)
    # 3. 토큰 추출
    my_token = token_info['access_token']

    # 1. tr 생성
    tr_inst = api.t8410(token=my_token, shcode='005930', qrycnt=1000, sdate='20200101', edate='20230926')
    # 2. 동기로 tr 요청
    daily_chart = api.Sync.rq_tr(tr_inst)
    # 3. 수신한 데이터 출력
    print(daily_chart)
```

### how to use websocket

```python
import json
import websockets
import LSREST as api

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."

def main():
    tr_inst = api.IssueToken(appkey, appsecretkey)
    token_info = api.Sync.rq_tr(tr_inst)
    my_token = token_info['access_token']

    # 1. websocket tr 생성
    ws_inst = api.NWS(token=my_token, ty_key='NWS001')
    # 2. websocket 연결
    await api.Async.connect_ws(ws_inst=ws_inst, callback=print)
    api.Async.connect_ws(ws_inst=ws_inst, callback=print).send(None)
    ws_inst.disconnect() # for disconnect the websocket.


```
