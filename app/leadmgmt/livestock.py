
from multiprocessing.sharedctypes import Value
from sqlite3 import Date
from fastapi import status
from sqlalchemy import null
from app.config.dbconfig import sessionLocal,conn
from app.config import model,app_config
import psycopg2.extras
from app.leadmgmt.utils import *
from app.leadmgmt import consumer
from app.leadmgmt import producer
# from app.leadmgmt.geticker import add_to_mst
from fastapi import APIRouter
from app.config import schemas
import yfinance as yf
from app.config.dbconfig import engine
from json import dumps
from ipaddress import collapse_addresses
from json import loads
from datetime import datetime
import os
import json


import time

from apscheduler.schedulers.background import BackgroundScheduler

globalvar=1

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")


post_route = APIRouter()

db=sessionLocal()



# @post_route.post("/stock/live/add")
# def addCheck(request:schemas.TickersLiveData):
#     leadpayloadresponse = leadpayloadcheckschool(request)
#     if leadpayloadresponse.status_code == status.HTTP_400_BAD_REQUEST:
#         return leadpayloadresponse
        
#     scheduler.start()
#     job=scheduler.add_job(addLiveScheduler,'cron',[request.tool_type],minute="*/2")
#     while True:
#         time.sleep(30)



# @post_route.post("/stock/kafka")
# def getKafka():
#     tickers = yf.Ticker("TCS.NS")
#     info_data=tickers.info
#     # info_data=info_data.json()
#     print(info_data)
#     # data=json.loads(info_data)
#     producer.send('test-topic', value=info_data)
#     data=consumer.Consumer()
#     return jsonresponse("200","success","Producer information sended successfully ","","",data)


# @post_route.post("/stock/5manually")
# def getKafka():
#     cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cursor.execute('select ticker_name from mst_stock_detail')

#     symbols=[]
#     for record in cursor.fetchall():
#         symbols.append(record[0])
#     tickers = [yf.Ticker(symbol) for symbol in symbols]
#     for ticker in tickers:
#         info_data=ticker.info
#         producer.send('test-topic-kafka', value=info_data)
#     data=consumer.Consumer()
#     return jsonresponse("200","success","Producer information sended successfully ","","",data)



# @post_route.post("/stock/livedata/kafka/scheduler/add")
# def addCheck(request:schemas.TickersLiveData):
#     leadpayloadresponse = leadpayloadcheckschool(request)
#     if leadpayloadresponse.status_code == status.HTTP_400_BAD_REQUEST:
#         return leadpayloadresponse
#     var1=request.tool_type

#     job=scheduler.add_job(producer.producerMethod,'cron',[var1],minute="*/2",id='my_job_id')
#     scheduler.start()

#     while True:
#         time.sleep(5)




# @post_route.post("/stock/kafka/historicaldata/add")
# def addHistory(request:schemas.TickersHistoricalData):
#     if(request.tool_type==1):
#         leadpayloadresponse = leadpayloadcheckschool(request)
#         if leadpayloadresponse.status_code == status.HTTP_400_BAD_REQUEST:
#             return leadpayloadresponse
#         var1=request.tool_type
#         p1=request.period
#         producer.producerMethodHistory(var1,p1)
#         return jsonresponse("200", "success", "Historical information Added successfully ", "", "1", "1")
#     return jsonresponse("400","Fail","Only Yahoo Service is available now ","","","")

# @post_route.post("/stock/kafka/livedata/get")
# def getLive(get:schemas.getPayload):

#     producer.producerGetLive(get.ticker_id)
#     new_data2=consumer.consumerGetLive()

#     return jsonresponse("200","success","School information Fetched successfully ","",new_data2[0],new_data2[1])

# @post_route.post("/stock/kafka/historical/get")
# def getHistory(get:schemas.getPayload):
#     producer.producerGetHistory(get.ticker_id)
#     new_data2=consumer.consumerGetHistory()

#     return jsonresponse("200","success","School information Fetched successfully ","",new_data2[0],new_data2[1])

# @post_route.post("/stock/kafka/previousday/historical/get")
# def getHistory(get:schemas.getPayload):
#     producer.producerGetDailyHistory(get.ticker_id)
#     new_data2=consumer.consumerGetDailyHistory()

#     return jsonresponse("200","success","History information Fetched successfully ","",new_data2[0],new_data2[1])


# @post_route.post('/add_to_mst')
# def add():
#     add_to_mst()
#     return jsonresponse("200","success","Added Tickers successfully ","","","")


@post_route.post("/stock/kafka/glive/gadd")
def getlive():
    new_data2=producer.producergaddlive()
    # new_data2=consumer.consumergaddlive()

    return jsonresponse("200","success","Live data added successfully ","",new_data2,new_data2)


@post_route.post("/stock/kafka/ghistory/gadd")
def getHistory(request:schemas.TickersHistoricalData):
    start=request.start_date
    end=request.end_date
    new_data2=producer.producergaddhistory(start,end)
    # new_data2=consumer.consumergaddlive()

    return jsonresponse("200","success","Historical data added successfully ","",new_data2,new_data2)

