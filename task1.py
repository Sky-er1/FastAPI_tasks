import asyncio
import aiohttp

from const import URL, PARAMS
from fetch_data import fetch_data

async def task1():
    async with aiohttp.ClientSession() as session:
        requests = [asyncio.create_task(fetch_data(session, URL, **params)) for params in PARAMS]

        print("Задача 1. Вывод всех запросов в порядке запуска:\n")
        responses = await asyncio.gather(*requests)
        for i, response in enumerate(responses):
            print(f"Запрос {i + 1}: Ответ = {response}")
        print("\n")

if __name__ == "__main__":
    asyncio.run(task1())