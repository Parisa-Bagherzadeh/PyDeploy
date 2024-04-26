import time
import random
import asyncio


counter = 0

async def marraige(name):
    global counter
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"{name} married  after {r} years")
    counter +=1


async def main():
    for child in ["mamad", "gholi", "goli", "Alex"]:
        asyncio.create_task(marraige(child))

    while counter < 4:
        await asyncio.sleep(1)

    # while True:
    #     await asyncio.sleep(1)



if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")