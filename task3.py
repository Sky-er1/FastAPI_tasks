import asyncio
import aiohttp

from const import URL, PARAMS
from fetch_data import fetch_data


async def task3():
    async with aiohttp.ClientSession() as session:
        requests = [asyncio.create_task(fetch_data(session, URL, **params)) for
                    params in PARAMS]

        completed_requests = []
        while True:

            for future in asyncio.as_completed(requests):
                result = await future
                completed_requests.append(result)
                if len(completed_requests) == 3 and "Error" in result:
                    print(f"Первый и второй запросы: {completed_requests[0]}, {completed_requests[1]}")
                    [task.cancel() for task in requests if not task.done()]
                    return
            print(f"Ошибок нет, последние два запроса: {completed_requests[-2]}, {completed_requests[-1]}")
            return


if __name__ == "__main__":
    asyncio.run(task3())
