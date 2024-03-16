import os
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from api.routers import users, token

app = FastAPI()

app.include_router(users.router)
app.include_router(token.router)


@app.get("/")
async def index():
    return {"message": "Hello, from aws lambda"}


handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    uvicorn_app = f"{os.path.basename(__file__).removesuffix('.py')}:app"
    uvicorn.run(uvicorn_app, host="0.0.0.0", port=800, reload=True)

# # https://github.com/robhowley/lambda-warmer-py
