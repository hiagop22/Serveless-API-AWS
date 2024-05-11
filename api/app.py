import os
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from api.routers import users
from api import auth

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
async def index():
    return {"message": "Hello, from aws lambda! Pipeline V3"}


handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    uvicorn_app = f"{os.path.basename(__file__).removesuffix('.py')}:app"
    uvicorn.run(uvicorn_app, host="0.0.0.0", port=800, reload=True)

# # https://github.com/robhowley/lambda-warmer-py
