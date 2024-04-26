import asyncio



async def fn():
    print("one")
    await asyncio.sleep(1)
    await asyncio.gather(fn2(), fn3())
    # await fn2() #await means wait for fn2 to run completely
    # asyncio.create_task(fn2()) #for calling an async function we use create_task()
    #asyncio.create_task() runs fn2 but does not wait for fn2 to run completely
    # await asyncio.sleep(1)
    print("four")
    await asyncio.sleep(1)
    print("five")
    await asyncio.sleep(1)



async def fn2():
    print("two")
    await asyncio.sleep(1) #One second sleep
    print("three")

async def fn3():
    print("six")
    await asyncio.sleep(1)
    print("seven")


#asyncio.run(...) is used to run the main function of the program
asyncio.run(fn())    


# We use asyncio.create_task for other functions except the main function
# asyncio.create_task is used for calling just one function 
# asyncio.gather() is used for multiple function running simultaneously
# asyncio.gather() does not wait for the calls to run completely, it runs the next functions too
# If await is used, it waits for the command to run completely(e.g. await asyncio.sleep(1))
# We just can use await for calling a function that is async
#فقط در صورتی میتونیم از اویت استفاده کنیم که تابع جلوی اویت آسینک باشد و همچنین دستور اویت را فقط ذرون بک تابع آسینک میتوانیم استفاده کنیم