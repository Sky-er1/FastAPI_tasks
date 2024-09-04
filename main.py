from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from exceptions import validation_exception_handler
from router import router as task_router

app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(task_router)

