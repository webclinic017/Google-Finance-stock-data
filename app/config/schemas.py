from typing import Optional
from pydantic import BaseModel
from app.config import model


class TickersLiveData(BaseModel):
    tool_type : int
    
    class Config:
        orm_mode=True

class TickersHistoricalData(BaseModel):
    start_date:str
    end_date : str
    
    class Config:
        orm_mode=True

class getPayload(BaseModel):
    ticker_id:str

    class Config:
        orm_mode=True
