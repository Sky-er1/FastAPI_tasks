import asyncio
import random
from fastapi import APIRouter
from exceptions import XlesZeroException

router = APIRouter(
    prefix="/task",
    tags=["Асинхронная таска"],
)


@router.get("")
async def get_two_numbers(x: int, y: int):
    if x <= 0:
        raise XlesZeroException(x, y)
    await asyncio.sleep(random.uniform(0, 3))
    result = (x / y) * random.randint(-10, 10)
    return {"x": x, "y": y, "result": result}


