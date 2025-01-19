import asyncio
import aiohttp
import aiofiles

async def fetch_data():
  async with aiohttp.ClientSession() as session:
    async with session.get('https://backend.profilesme.site') as response:
      data = await response.json()
      print(data)

# asyncio.run(fetch_data())


async def read_file():
  async with aiofiles.open('02poly.p' , mode="w+t") as file:
    content = await file.write('write')
    print(content)

asyncio.run(read_file())
