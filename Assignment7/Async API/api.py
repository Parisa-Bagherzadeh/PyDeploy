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
    

def get_states():
    
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url) 

    print("List of satets --------------------")
    states = response.json()
    print(states)


    name = "گلستان"

    for state in states:
        if state['name'] == name:
            print(state['id'])
            state_id = state['id']

    return state_id        


def get_cities(state_id):

    print("State_id : ", state_id)
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)


    cities = response.json()

    print("List of cities---------------", cities)

    name = "گرگان"

    for city in cities['cities']:

        print(city['name'])
        
        if city['name'] == name:

            print("Your city found :)")
            print("Latitude : ", cities['latitude'])
            print("Longitude : ", cities['longitude'])

            break
    else:
        print("Not found")    

                


async def get_coordinates():
    state_id = get_states()
    get_cities(state_id)
    




async def main():
    await asyncio.gather(rhyme_finder(), get_coordinates() )
    print("main ended")




if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Total time : {total_time} seconds")   