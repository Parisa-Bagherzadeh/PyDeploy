import time
import random
import asyncio



async def get():
    print("Get started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"Get ended in {r} seconds")


def extract(): 
    print("Extract started")
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"Extract ended in {r} seconds")   


async def downlaod():
    print("Download started")
    await get()
    extract()
    # print(f"Download ended in {r} seconds")



async def printer():
    print("Printer started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"Printer ended in {r} seconds")



async def ai_video():
    print("AI video started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"AI video ended in {r} seconds")

async def ai_audio():
    print("AI audio started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"AI audio ended in {r} seconds")



def mix():
    print("AI Mix started")
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"AI Mix ended in {r} seconds")




async def ai():
    print("AI started")
    # r = random.randint(0, 10)
    # await asyncio.sleep(r)
    await asyncio.gather(ai_video(), ai_audio())
    mix()
    print(f"AI ended")


async def main():
    await asyncio.gather(downlaod(), printer(), ai())
    print("Main ended")



if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")    