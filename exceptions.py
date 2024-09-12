from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


class TaskException(HTTPException):
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail=None):
        super().__init__(
            status_code=status_code,
            detail=detail)


class XlesZeroException(TaskException):
    def __init__(self, x: int, y: int):
        detail = {
            "Error": "XlesZeroException",
            "ErrorMessage": "x должен быть больше нуля",
            "RequestData": f"x = {x}, y = {y}"
        }
        super().__init__(detail=detail)


class ZeroDivisionException(TaskException):
    def __init__(self, x: int, y: int):
        detail = {
            "Error": "ZeroDivisionException",
            "ErrorMessage": "y должен быть больше нуля",
            "RequestData": f"x = {x}, y = {y}"
        }
        super().__init__(detail=detail)


async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    x = request.query_params.get('x', '?')
    y = request.query_params.get('y', '?')

    error_detail = {
        "Error": "ValidationError",
        "ErrorMessage": "Ошибка валидации запроса",
        "RequestData": f"x = {x}; y = {y}"
    }

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=error_detail,
    )
