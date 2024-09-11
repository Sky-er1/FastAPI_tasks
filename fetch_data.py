import aiohttp
from aiohttp import ClientSession

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