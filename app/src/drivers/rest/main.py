from fastapi import FastAPI
from app.src.drivers.rest.routes import task_router
from app.src.drivers.rest.exception_handlers import exception_container

app = FastAPI()

exception_container(app)

app.include_router(task_router.router)