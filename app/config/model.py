# database table structure is here
from tkinter.filedialog import Open
from xmlrpc.client import Boolean
from sqlalchemy.sql.expression import null
from app.config.dbconfig import Base
from sqlalchemy import  String,Integer,Column,DateTime, BigInteger
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION,BOOLEAN



class TickersCurrentData(Base):
    __tablename__ = "txn_stock_price_live"
    stock_price_live_id=Column(Integer,primary_key=True,autoincrement=True)
    # tool_type=Column(Integer)
    current_price=Column(DOUBLE_PRECISION)
    current_price_date_time=Column(DateTime,default=datetime.datetime.utcnow)
    day_open=Column(DOUBLE_PRECISION)
    day_high=Column(DOUBLE_PRECISION)
    day_low=Column(DOUBLE_PRECISION)
    day_volume=Column(BigInteger)
    # recommendation=Column(String(100))
    ticker_id= Column(String(100))
    isin_code=Column(String(100))
    bu_id=Column(Integer)
    sub_bu_id=Column(Integer)
    application_id=Column(Integer)
    is_active=Column(BOOLEAN)
    created_by=Column(BigInteger)
    created_date=Column(DateTime,default=datetime.datetime.utcnow)
    last_modified_by=Column(BigInteger)
    last_modified_date=Column(DateTime,default=datetime.datetime.utcnow)


class MstStockDetail(Base):
    __tablename__ = "mst_stock_detail"
    stock_detail_id = Column(Integer,primary_key=True)
    ticker_name=Column(String(100),nullable=False)
    isin_code=Column(String(100))

class TickersHistoricalData(Base):
    __tablename__ = "txn_stock_price_historical"
    stock_price_historical_id = Column(Integer,primary_key=True,autoincrement=True)
    historical_price_date_time=Column(String)
    day_open_price= Column(DOUBLE_PRECISION)
    day_high_price= Column(DOUBLE_PRECISION)
    day_low_price= Column(DOUBLE_PRECISION)
    day_close_price= Column(DOUBLE_PRECISION)
    day_volume= Column(BigInteger)
    ticker_id= Column(String(100))
    isin_code=Column(String(100))
    bu_id=Column(Integer,default=1)
    sub_bu_id=Column(Integer,default=1)
    application_id=Column(Integer,default=1)
    is_active=Column(BOOLEAN,default=True)
    created_by=Column(Integer,default=1)
    created_date=Column(DateTime,default=datetime.datetime.utcnow)
    last_modified_by=Column(Integer,default=1)
    last_modified_date=Column(DateTime,default=datetime.datetime.utcnow)


