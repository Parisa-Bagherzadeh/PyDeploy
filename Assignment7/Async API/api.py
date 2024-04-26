import asyncio
import time
import requests
import os




async def rhyme_finder():

    key = os.getenv("RHYME_KEY")
    # word = input("Enter a word: ")
    word = "رفت"
    url = f"https://rhyming.ir/api/rhyme-finder?api={key}&w={word}&sb=1&mfe=2&eq=1"
    response = requests.request("GET", url)

    print(response.json())
    

async def get_states():
    
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url) 

    print("List of satets --------------------")
    print(response.json())


    results = response.json()
    # name = input("Enter state's name: ")
    name = "اصفهان"

    for result in results:
        if result['name'] == name:
            print(result['id'])




    

async def get_cities():

    # state_id = input("Enter state id: ")
    state_id = 4
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)

    print("List of cities-------------------------")
    print(response.json())

    result = response.json()




    # name = input("Enter name of your city: ")
    name = "اصفهان"

    if result['name'] == name:
        print("Your city found :)")

        print("Latitude : ", result['latitude'])
        print("Longitude : ", result['longitude'])
    else:
        print("Not found")    

            


async def get_coordinates():
    await asyncio.gather(get_states(),get_cities())




async def main():
    await asyncio.gather(rhyme_finder(), get_coordinates() )
    print("main ended")




if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Total time : {total_time} seconds")   