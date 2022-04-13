from app.leadmgmt.utils import *
from app.config import model
from app.config.dbconfig import sessionLocal,conn
from kafka import KafkaConsumer
from json import loads
from datetime import datetime
import pandas as pd
from app.config.dbconfig import engine
import psycopg2.extras
from kafka.errors import KafkaError


db=sessionLocal()

# def consumerGetDailyHistory():
#     try:
#         consumer = KafkaConsumer(
#         'get-hist1',
#         bootstrap_servers=['localhost:9092'],
#         auto_offset_reset='earliest',
#         enable_auto_commit=True,
#         group_id='my-group',
#         value_deserializer=lambda x: loads(x.decode('utf-8')))
#     except KafkaError as exc:
#             print("Exception during subscribing to topics - {}".format(exc))
#             return


#     for message in consumer:
#         message=message.value
#         print(message)
#         new_data1 = message
#         if message=="" or message==None:
#             new_data2 = db.query(model.TickersHistoricalData).all() 
#             counts=len(new_data2)

#         else:
#             new_data2=db.query(model.TickersHistoricalData).filter(model.TickersHistoricalData.ticker_id==message).order_by(model.TickersHistoricalData.stock_price_historical_id.desc()).first() 
#             counts=1
#         # new_data2 = db.query(model.TickersHistoricalData).all() 
#         # counts=len(new_data2)
#         consumer.commit(offsets=None)
#         consumer.close()
#         return counts,new_data2

# def consumerGetHistory():
#     try:
#         consumer = KafkaConsumer(
#         'get-historical2',
#         bootstrap_servers=['localhost:9092'],
#         auto_offset_reset='earliest',
#         enable_auto_commit=True,
#         group_id='my-group',
#         value_deserializer=lambda x: loads(x.decode('utf-8')))
#     except KafkaError as exc:
#             print("Exception during subscribing to topics - {}".format(exc))
#             return

#     for message in consumer:
#         message=message.value
#         print(message)
#         new_data1 = message
#         if message=="" or message==None:
#             new_data2 = db.query(model.TickersHistoricalData).all() 
#             counts=len(new_data2)

#         else:
#             new_data2=db.query(model.TickersHistoricalData).filter(model.TickersHistoricalData.ticker_id==message).all() 
#             counts=1
#         # new_data2 = db.query(model.TickersHistoricalData).all() 
#         # counts=len(new_data2)
#         consumer.commit(offsets=None)
#         consumer.close()
#         return counts,new_data2

# def consumerGetLive():
#     try:
#         consumer = KafkaConsumer(
#         'get-live',
#         bootstrap_servers=['localhost:9092'],
#         auto_offset_reset='earliest',
#         enable_auto_commit=True,
#         group_id='my-group',
#         value_deserializer=lambda x: loads(x.decode('utf-8')))
#     except KafkaError as exc:
#             print("Exception during subscribing to topics - {}".format(exc))
#             return

#     for message in consumer:
#         message=message.value
#         print(message)
#         count1=db.query(model.MstStockDetail).count()
#         new_data1 = message
#         if message=="" or message==None:
#             new_data2 = db.query(model.TickersCurrentData).order_by(model.TickersCurrentData.stock_price_live_id.desc()).limit(count1).all() 
#             counts=len(new_data2)

#         else:
#             new_data2=db.query(model.TickersCurrentData).filter(model.TickersCurrentData.ticker_id==message).order_by(model.TickersCurrentData.stock_price_live_id.desc()).first() 
#             counts=1
#         consumer.commit(offsets=None)
#         consumer.close()
#         return counts,new_data2


# def ConsumerHistory(symbol1):
#     try:
#         consumer = KafkaConsumer(
#         'historical-data',
#         bootstrap_servers=['localhost:9092'],
#         auto_offset_reset='earliest',
#         enable_auto_commit=True,
#         group_id='my-group',
#         value_deserializer=lambda x: loads(x.decode('utf-8')))
#     except KafkaError as exc:
#             print("Exception during subscribing to topics - {}".format(exc))
#             return


#     for message in consumer:
#         time1=datetime.now()
#         message=message.value
#         message=pd.read_json(message)
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         cursor.execute('select isin_code from mst_stock_detail where ticker_name=%s',[symbol1,])
#         isin=cursor.fetchall()
#         # isin=db.query(model.MstStockDetail).filter(model.MstStockDetail.ticker_name==symbol1).filter(model.MstStockDetail.isin_code).first()
#         print(isin)
#         db_data = db.query(model.TickersHistoricalData.stock_price_historical_id).count()
        
#         df2 = pd.DataFrame(message, columns=['Open','High','Low','Close','Volume','ticker_id','bu_id','sub_bu_id','application_id','is_active','created_by','created_date','last_modified_by','last_modified_date','isin_code'])
#         df2.rename(columns = {'Open' : 'day_open_price', 'High' : 'day_high_price','Low':'day_low_price' , 'Close':'day_close_price' , 'Volume':'day_volume'}, inplace = True)
#         print(isin[0])
#         print(isin[0][0])
#         df2['bu_id']=1
#         df2['sub_bu_id']=1
#         df2['application_id']=1
#         df2['is_active']=True
#         df2['created_by']=1
#         df2['created_date']=time1
#         df2['last_modified_by']=1
#         df2['last_modified_date']=time1
#         df2.insert(0, 'stock_price_historical_id', range(db_data+1,db_data+len(df2)+1))
#         df2['ticker_id']=symbol1
#         df2['isin_code']=isin[0][0]
#         print(df2)
#         # print(message)
#         df2.to_sql('historical_stock', engine,schema=None, if_exists='append',index=True,index_label='historical_price_date_time')
#         print("done")
#         consumer.commit(offsets=None)
#         consumer.close()
#         # sys.exit("done")
#     return jsonresponse("200", "success", "Historical information Added successfully ", "", "", "1")


# def Consumer():
#         try:
#             consumer = KafkaConsumer(
#             'test-topic-test',
#             bootstrap_servers=['localhost:9092'],
#             auto_offset_reset='earliest',
#             enable_auto_commit=True,
#             group_id='my-group',
#             value_deserializer=lambda x: loads(x.decode('utf-8')))
#         except KafkaError as exc:
#             print("Exception during subscribing to topics - {}".format(exc))
#             return

    
#         for message in consumer:

#             message=message.value
#             print(message)
#             # print(consumer)
#             db_data = db.query(model.TickersCurrentData.stock_price_live_id).count()

#             cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#             cursor.execute('select isin_code from mst_stock_detail where ticker_name=%s',[message['symbol'],])
#             isin=cursor.fetchall()
#             # print(message[0])
#             print(isin)
                            
#             new_data={}
#             # print(message[0])
#             new_data=model.TickersCurrentData(
#                 ticker_id=message['symbol'],
#                 current_price=message['currentPrice'],
#                 day_high=message['dayHigh'],
#                 day_low=message['dayLow'],
#                 recommendation=message['recommendationKey'],
#                 tool_type=1,
#                 stock_price_live_id=db_data+1,
#                 bu_id=1,
#                 sub_bu_id=1,
#                 application_id=1,
#                 is_active=True,
#                 created_by=1,
#                 last_modified_by=1,
#                 isin_code=isin[0][0]
#             )
#             db.add(new_data)
#                 # i=i+1

#             db.commit()
#             db.close()
#             consumer.commit()
#         # KafkaConsumer.close()
#             consumer.close()
#         # print('Data at {} added to POSTGRESQL'.format(new_data,collections))
                
#         return new_data



def consumergaddlive():
        try:
            consumer = KafkaConsumer(
            'gtestfinance',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: loads(x.decode('utf-8')))
        except KafkaError as exc:
            print("Exception during subscribing to topics - {}".format(exc))
            return
        # i=0
        # cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # cursor.execute('select isin_code from mst_stock_detail where ticker_name=%s',[index,])
        # isin=cursor.fetchall()
        for message in consumer:
            time1=datetime.now()
            message=message.value
            message.pop(0)
            # message.pop(0)

            message=pd.DataFrame(message,columns =['ticker_id', 'current_price', 'day_open','day_high','day_low','day_volume'])
            # print(consumer)
            print(message)
            db_data = db.query(model.TickersCurrentData.stock_price_live_id).count()

            
            
            df2 = pd.DataFrame(message, columns=['current_price','current_price_date_time','day_open','day_high','day_low','day_volume','ticker_id','isin_code','bu_id','sub_bu_id','application_id','is_active','created_by','created_date','last_modified_by','last_modified_date'])
            df2['bu_id']=1
            df2['sub_bu_id']=1
            df2['application_id']=1
            df2['current_price_date_time']=time1
            df2['is_active']=True
            df2['created_by']=1
            df2['created_date']=time1
            df2['last_modified_by']=1
            df2['last_modified_date']=time1
            df2.insert(0, 'stock_price_live_id', range(db_data+1,db_data+len(df2)+1))
            # df2['ticker_id']=symbol1
            # df2['isin_code']=isin[0][0]
            print(df2)
            # print(message)



            df2.to_sql('txn_stock_price_live', engine,schema=None, if_exists='append',index=False)
            print("done")
            # new_data={}
            # # print(message[0])
            # new_data=model.TickersCurrentData(
            #     ticker_id=index,
            #     current_price=message,
            #     # day_high=message['dayHigh'],
            #     # day_low=message['dayLow'],
            #     # tool_type=1,
            #     stock_price_live_id=db_data+1,
            #     bu_id=1,
            #     sub_bu_id=1,
            #     application_id=1,
            #     is_active=True,
            #     created_by=1,
            #     last_modified_by=1,
            #     isin_code=isin[0][0]

            # )
            # db.add(new_data)
            # i=i+1

            # db.commit()
            # db.close()
            consumer.commit()
        # KafkaConsumer.close()
            consumer.close()
        # print('Data at {} added to POSTGRESQL'.format(new_data,collections))
                
        return "done"


def consumergaddhistory(symbol1):
    try:
        consumer = KafkaConsumer(
        'ghistorical1',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    except KafkaError as exc:
            print("Exception during subscribing to topics - {}".format(exc))
            return


    for message in consumer:
        time1=datetime.now()
        message=message.value
        message.pop(0)
        message.pop(0)

        message=pd.DataFrame(message,columns =['Date', 'Open', 'High','Low','Close','Volume'])

        list1=[]
        for i in message.index:
            date_time_obj = datetime.strptime(message['Date'][i], "%m/%d/%Y %H:%M:%S")
            message['Date'][i]=date_time_obj
            check= db.query(model.TickersHistoricalData).filter(model.TickersHistoricalData.historical_price_date_time==message['Date'][i]).filter( model.TickersHistoricalData.ticker_id==symbol1).first()
            print(check)
            print(message.index[i])
            if check is not None:
                # df3=df2.drop(df2.index[i])
                list1.append(message.index[i])
                # df2=df2.drop(df2.index[i])
        # res = str(list1)[1:-1]
        print(list1)
        print(message)
        if (len(list1)!=0):
            df2=message.drop(list1)
        else:
            df2=pd.DataFrame(message)
        print(df2)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('select isin_code from mst_stock_detail where ticker_name=%s',[symbol1,])
        isin=cursor.fetchall()
        # isin=db.query(model.MstStockDetail).filter(model.MstStockDetail.ticker_name==symbol1).filter(model.MstStockDetail.isin_code).first()
        print(isin)
        db_data = db.query(model.TickersHistoricalData.stock_price_historical_id).count()
        
        df2 = pd.DataFrame(df2, columns=['Date','Open','High','Low','Close','Volume','ticker_id','bu_id','sub_bu_id','application_id','is_active','created_by','created_date','last_modified_by','last_modified_date','isin_code'])
        df2.rename(columns = {'Date':'historical_price_date_time','Open' : 'day_open_price', 'High' : 'day_high_price','Low':'day_low_price' , 'Close':'day_close_price' , 'Volume':'day_volume'}, inplace = True)
        print(isin[0])
        print(isin[0][0])
        df2['bu_id']=1
        df2['sub_bu_id']=1
        df2['application_id']=1
        df2['is_active']=True
        df2['created_by']=1
        df2['created_date']=time1
        df2['last_modified_by']=1
        df2['last_modified_date']=time1
        df2.insert(0, 'stock_price_historical_id', range(db_data+1,db_data+len(df2)+1))
        df2['ticker_id']=symbol1
        df2['isin_code']=isin[0][0]
        # print(message)
        print(df2)

        df2.to_sql('txn_stock_price_historical', engine,schema=None, if_exists='append',index=False)
        print("done")
        consumer.commit(offsets=None)
        consumer.close()
        # sys.exit("done")
    return "Please Check Database"
