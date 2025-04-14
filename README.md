# Update History
- (25.04.03) 추가된 TR 반영(NXT 등), 초당 실시간(Realtime;WebSocket) 등록제한 설정, 일부 코드 정리
- (25.04.09) 주석(comment) 수정 및 dependancy 명시
- (25.04.14) Sync.py & Async.py에서 연속조회 시 오류 해결 / 경로 충돌 문제 해결 / Util.py 파일 추가(Access Token Manager 추가) / README.md의 예제코드 수정
- (25.04.15) README.md 예제 변경

# LSREST
LS(구.eBest) 투자증권의 RESTful OpenAPI(https://openapi.ls-sec.co.kr/intro)를 쉽게 이용할수 있게끔 하는 python-package 입니다.
비동기식(Asynchronously) 및 동기식(Synchronously) 모두 이용 가능하며, 
아래 예제 코드(example code)를 참고하여 사용할 수 있습니다.
1. Base.py : TR 및 websocket의 기본 뼈대 클래스(BaseTR, BaseWS)가 선언되어 있습니다.
2. 디렉토리(ETC, FrgFut, FutOpt, OAuth 등) : 개별 TR 및 Websocket가 클래스로 선언되어 있습니다.
3. Util.py : access_token을 요청하고 자동폐기하는 ContextManagerClass가 선언되어 있습니다.
4. Sync.py, Async.py : 동기식/비동기식으로 tr 또는 websocket연결을 요청하는 함수가 작성되어 있습니다.
 
## 이용 방법
일반적인 순서는 다음과 같습니다.
1. 요청하고자 하는 tr(또는 ws(webscket)) instance를 생성한다.
2. tr(또는 ws)을 동기식/비동기식으로 요청한다.
3. 데이터를 수신받아 처리한다.

## 동기/비동기
동기식 요청(request)은 함수 parameter로 session이 필요치 않으나, 
비동기식 요청(request)은 반드시 session이 함수 parameter로 전달되어야 합니다.

## 웹소켓(websocket)을 이용한 실시간조회
웹소켓은 동기식 요청이 불가하며, 비동기식으로만 요청할 수 있습니다.

## 연속조회 관련사항
'cts_'로 시작하는 attribute가 있는 tr만 연속조회가 가능하게 구현되어 있으며,
cts_로 시작하지 않는 attribute로 연속조회가 구현된 경우, 별도로 로직을 구현하셔야 합니다. (Base.py 파일 참조)


## example code

### (예제) tr 요청 - 동기식(sync)

```python
import LSREST as api

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."

def main():
    # 동기식으로 토큰 요청 및 with절 종료 시 토큰 자동 폐기
    with api.Util.AccessTokenManager(appkey, appsecretkey) as token:
        # 1. tr 생성
        tr_inst = api.Stock.t8410(token=token, shcode='005930', qrycnt=1000, sdate='20200101', edate='20230926')
        # 2. 동기로 tr 요청
        daily_chart = api.Sync.rq_tr(tr_inst)
        # 3. 수신한 데이터 출력
        print(daily_chart)
```

### (예제) tr 요청 - 비동기식(async)
```python
import LSREST as api

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."

async def main():
    # 비동기식으로 세션 연결 및 토큰 요청 -> with절 종료 시 토큰 자동 폐기
    async with api.Util.AsyncSessionAccessTokenManager(appkey, appsecretkey) as (session, token):
        # 1. tr 생성
        tr_inst = api.Stock.t8410(token=token, shcode='005930', qrycnt=1000, sdate='20200101', edate='20230926')
        # 2. 비동기로 tr 요청 (session이 함께 전달되어야 함)
        daily_chart = await api.Async.rq_tr(session=session, tr_inst=tr_inst)
        # 3. 수신한 데이터 출력
        print(daily_chart)

if __name__ == "__main__":
    asyncio.run(main())

```

### (예제) 웹소켓(websocket) 사용

```python
import json
import websockets
import asyncio
import LSREST as api

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."

async def main():
    async with api.Util.AsyncSessionAccessTokenManager(appkey, appsecretkey) as (session, token):
        # task로 실행
        ws_inst = api.ETC.NWS(token=token, ty_key='NWS001')
        asyncio.create_task(api.Async.connect_ws(ws_inst=ws_inst, callback=print))
        await asyncio.sleep(600)        
        ws_inst.disconnect() # 600초(10분) 대기 후 연결 해제

if __name__ == "__main__":
    asyncio.run(main())
```
