import asyncio
import aiohttp

from const import URL, PARAMS
from fetch_data import fetch_data


async def task2():
    async with aiohttp.ClientSession() as session:
        requests = [asyncio.create_task(fetch_data(session, URL, **params)) for
                    params in PARAMS]

        completed_requests = []
        while True:

            for future in asyncio.as_completed(requests):
                result = await future
                completed_requests.append(result)
                if len(completed_requests) == 2:
                    print(f"Второй по времени выполнения запрос: {result}")
                    [task.cancel() for task in requests if not task.done()]
                    return


if __name__ == "__main__":
    asyncio.run(task2())
