#!/usr/bin/env python3
import aiohttp
import asyncio


async def fetch(client):
    async with client.get('http://127.0.0.1:8000') as response:
        print([cookie for cookie in response.cookies])
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
