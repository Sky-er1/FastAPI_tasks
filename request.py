import asyncio
import aiohttp
from aiohttp import ClientSession


URL = 'http://127.0.0.1:8000/task'
PARAMS = [
    {"x": 1, "y": 2},
    {"x": 3, "y": 4},
    {"x": 5, "y": 1},
    {"x": -1, "y": 2},
    {"x": 0, "y": 3}
]


async def fetch_data(session: ClientSession, url: str, x: int, y: int):
    try:
        params = {'x': x, 'y': y}
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()
    except aiohttp.ClientResponseError as http_err:
        return {"Error": "HTTP error", "Detail": str(http_err)}
    except aiohttp.ClientConnectionError as conn_err:
        return {"Error": "Connection error", "Detail": str(conn_err)}
    except Exception as e:
        return {"Error": "Unknown error", "Detail": str(e)}


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [fetch_data(session, URL, **params) for params in PARAMS]
        responses = await asyncio.gather(*requests)
        for i, response in enumerate(responses):
            print(f"Запрос {i + 1}: Ответ = {response}")


asyncio.run(main())
