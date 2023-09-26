import os
import datetime
import json
import asyncio
import aiohttp
from const import BASE_URL_POST, BASE_URL_WEBSOCKET, BASE_URL_WEBSOCKET_FOR_TEST

#########################################
#RQTR_MQ = asyncio.Queue()
#RP_MQ = asyncio.Queue()
#########################################



import API
from EasyAPI import Token, Stock, Util
token_info = None
dc = None
async def main():
    global dc, token_info
    async with aiohttp.ClientSession(base_url=BASE_URL_POST) as session:
        token_info = await Token.async_issue_token(session, appkey, appsecretkey)
        token = token_info['access_token']
        dc = await Stock.daily_chart(session, token, code6='005930', cnt=1000, sdate='20200101', edate='20230921')
    #print(dc)

if __name__ == '__main__':
    asyncio.run(main())

