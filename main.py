from fastapi import FastAPI
import uvicorn
from app.leadmgmt.livestock import post_route
from app.config import app_config

app = FastAPI()

app.include_router(post_route)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)