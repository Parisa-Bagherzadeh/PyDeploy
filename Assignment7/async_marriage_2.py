import time
import random
import asyncio




async def marraige(name):
    global counter
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    


async def main():
   await asyncio.gather(marraige("mamad"), marraige("gholi"), marraige("goli"),marraige("alex"))
 

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")