import asyncio
from websockets.server import serve

async def recieve(websocket):
    async for message in websocket:
        print (message)

async def main():
    async with serve(recieve, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())