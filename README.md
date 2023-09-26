# eBREST
eBest 투자증권의 RESTful OpenAPI 이용 코드

## example code
### how to request tr asyncronously
```python
import datetime
import aiohttp
import eBREST as eb

appkey = "abcdefg..."
appsecretkey = "ABCEDFG..."


async def main():
    async with aiohttp.ClientSession(base_url=BASE_URL_POST) as session:

        tr_inst = eb.IssueToken(appkey, appsecretkey)
        token_info = await eb.Async.rq_tr(session=session, tr_inst=tr_inst)
        my_token = token_info['access_token']

        tr_inst = eb.t8410(token=my_token, shcode='005930', qrycnt=1000, sdate='20200101', edate='20230926')
        daily_chart = await eb.Async.rq_tr(session=session, tr_inst=tr_inst)
        print(daily_chart)
```


### how to request tr syncronously

```python
def main():
    tr_inst = eb.IssueToken(appkey, appsecretkey)
    token_info = eb.Sync.rq_tr(tr_inst)
    my_token = token_info['access_token']

    tr_inst = eb.t8410(token=my_token, shcode='005930', qrycnt=1000, sdate='20200101', edate='20230926')
    daily_chart = eb.Sync.rq_tr(tr_inst)
    print(daily_chart)
```
