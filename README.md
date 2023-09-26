# eBREST
eBest 투자증권의 RESTful OpenAPI 이용 코드

## example code
### how to request tr asyncronously
```python
import aiohttp
import eBREST as eb

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."

async def main():
    async with aiohttp.ClientSession(base_url=BASE_URL_POST) as session:
        # tr 생성
        tr_inst = eb.IssueToken(appkey, appsecretkey)
        # 비동기로 tr 요청
        token_info = await eb.Async.rq_tr(session=session, tr_inst=tr_inst)
        # 토큰 추출
        my_token = token_info['access_token']

        # tr 생성
        tr_inst = eb.t8410(token=my_token, shcode='005930', qrycnt=1000, sdate='20200101', edate='20230926')
        # 비동기로 tr 요청
        daily_chart = await eb.Async.rq_tr(session=session, tr_inst=tr_inst)
        # 수신한 데이터 출력
        print(daily_chart)
```


### how to request tr syncronously

```python
import eBREST as eb

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."

def main():
    # tr 생성
    tr_inst = eb.IssueToken(appkey, appsecretkey)
    # 동기로 tr 요청
    token_info = eb.Sync.rq_tr(tr_inst)
    # 토큰 추출
    my_token = token_info['access_token']

    # tr 생성
    tr_inst = eb.t8410(token=my_token, shcode='005930', qrycnt=1000, sdate='20200101', edate='20230926')
    # 동기로 tr 요청
    daily_chart = eb.Sync.rq_tr(tr_inst)
    # 수신한 데이터 출력
    print(daily_chart)
```
