import asyncio
import aiohttp

async def async_real_download_file(url, filename):
    print(f"  Downloading file : {url}")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()

    with open(filename, "wb") as file:
        file.write(data)

    print(f"    Done : {url}")

async def async_download_file(file_name, delay):
    print(f"  Downloading file : {file_name}")
    await asyncio.sleep(delay)
    print(f"    Done : {file_name}")


async def main():

    ## Synchronous version : 

    # await async_download_file("big file.txt", 3)
    # await async_download_file("smallfile.txt", 1)
    # await async_real_download_file("https://examplefile.com/file-download/19", "one_mb.txt")

    ## Async version :
    t1 = asyncio.create_task(async_download_file("big file.txt", 3))
    t2 = asyncio.create_task(async_download_file("smallfile.txt", 1))
    t3 = asyncio.create_task(async_real_download_file("https://examplefile.com/file-download/19", "one_mb.txt"))

    await t3
    await t1
    await t2



if __name__ == "__main__":
    asyncio.run(main())