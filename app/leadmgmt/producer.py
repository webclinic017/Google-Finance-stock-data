from json import dumps
from unittest import result
from kafka import KafkaProducer 
from app.leadmgmt import consumer
import yfinance as yf
import psycopg2.extras
from app.config.dbconfig import conn

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'app/leadmgmt/keys.json'

creds=None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1aeC2oZSpngHyE-3ZHS7BWBkPCMmxRaNkLKpKeqF90Eo'

service =build('sheets','v4',credentials=creds)
sheet=service.spreadsheets()

# conn = psycopg2.connect('postgresql://postgres:yuviboxer@localhost/stock_db')


producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x:dumps(x).encode('utf-8'))

# def producerGetDailyHistory(ticker_id):
#     checkid=ticker_id
#     producer.send('get-hist1', value=checkid)

# def producerGetHistory(ticker_id):
#     checkid=ticker_id
#     producer.send('get-historical2', value=checkid)

# def producerGetLive(ticker_id):
#     producer.send('get-live', value=ticker_id)

# def producerMethodHistory(request,period1):
#         if(request==1):
#             cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#             cursor.execute('select ticker_name from mst_stock_detail')

#             symbols=[]
#             for record in cursor.fetchall():
#                 symbols.append(record[0])
#             tickers = [yf.Ticker(symbol) for symbol in symbols]
#             print(symbols)
#             i=0
#             for ticker in tickers:
#                 info_data=ticker.history(period=period1)
#                 history_daya=info_data.to_json()
#                 print(symbols[i])
#                 producer.send('historical-data', value=history_daya)
#                 data=consumer.ConsumerHistory(symbols[i])
#                 i=i+1
#                 print("next")
#         return data
#         return jsonresponse("400","Fail","Only Yahoo Service is available now ","","","")


# def producerMethod(request):
#     if(request==1):
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         cursor.execute('select ticker_name from mst_stock_detail')
#         symbols=[]
#         for record in cursor.fetchall():
#             symbols.append(record[0])
#         tickers = [yf.Ticker(symbol) for symbol in symbols]
#         print(symbols)
#         for ticker in tickers:
#             info_data=ticker.info
#             producer.send('test-topic-test', value=info_data)
#             data=consumer.Consumer()
#     return data


def producergaddlive():
        # cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # cursor.execute('select ticker_name from mst_stock_detail')
        # symbols=[]
        # for record in cursor.fetchall():
        #     symbols.append(record[0])
        
        # print(symbols)
        # result=[]
        # for symbol in symbols:
            # var=input('Enter Ticker here:-')
            # aoa=[['''=GOOGLEFINANCE("{}","price")'''.format(symbol)]]
            # print(aoa)
            # update1=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="E2",valueInputOption="USER_ENTERED",
            #     body={"values":aoa}).execute()
            # add=sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="A1",valueInputOption="USER_ENTERED",
            #     insertDataOption="INSERT_ROWS",includeValuesInResponse=True,body={"values":aoa}).execute()
            # result.append(add['updates']['updatedData']['values'][0][0])
            # result=add['updates']['updatedData']['values'][0][0]
            result=sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="B:G").execute()
            values1=result.get('values',[])
            print(values1)
            producer.send('gtestfinance', value=values1)
            data=consumer.consumergaddlive()
            return data


def producergaddhistory(start,end):
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('select ticker_name from mst_stock_detail')
        symbols=[]
        for record in cursor.fetchall():
            symbols.append(record[0])
        
        print(symbols)
        # result=[]
        for symbol in symbols:
            # var=input('Enter Ticker here:-')
            aoa=[['''=GOOGLEFINANCE("{}","all","{}","{}","daily")'''.format(symbol,start,end)]]
            print(aoa)
            # update1=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="E2",valueInputOption="USER_ENTERED",
            #     body={"values":aoa}).execute()
            add=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="M1",valueInputOption="USER_ENTERED",
                includeValuesInResponse=True,body={"values":aoa}).execute()
            # result.append(add['updates']['updatedData']['values'][0][0])
            # result=add['updates']['updatedData']['values'][0][0]
            result=sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="M:R").execute()
            values1=result.get('values',[])
            print(values1)
            producer.send('ghistorical1', value=values1)
            data=consumer.consumergaddhistory(symbol)
        return data