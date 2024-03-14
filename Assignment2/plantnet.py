import os
import requests
import urllib.request 
import matplotlib.pyplot as plt
import dotenv 
import cv2
from argparse import ArgumentParser



def text2image(flower_name):
    
    ILLUSION_DIFFUSION_KEY = os.getenv("ILLUSION_DIFFUSION_KEY")
    url = "https://fal.run/fal-ai/illusion-diffusion"

    headers = {
          "Authorization" : f"Key {ILLUSION_DIFFUSION_KEY}",
          "Content-Type" : "application/json"
          }

    payload = {
        "image_url":"https://storage.googleapis.com/falserverless/illusion-examples/checkers.png",
        "prompt" : f"(masterpiece:1.4), (best quality), (detailed),A pink, purple and white {flower_name} flower in a white vase on a wooden coffee table",
        "negetive_prompt" : "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"

    }
    try:
        response = requests.post(url, headers = headers, json = payload)
        response.raise_for_status
    
    except requests.exceptions.HTTPError as errh:   
        return errh
    except requests.exceptions.RequestException as err:
        return err    
    else:    
        return response.json()

def plantnet():

    PLANT_API_KEY = os.getenv("PLANT_API_KEY")

    url = "https://my-api.plantnet.org/v2/identify/all"
    headers = {}
    payload = {
        "api-key" : PLANT_API_KEY
        }

    files = {
        "images" : open("IllusionDiffusion_output/flower.jpg", "rb")
    }
    try:
        response = requests.post(url, headers = headers, params = payload, files = files)
        response.raise_for_status
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error occurred: {errh}")     
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")        
    else:    
        # print(response.status_code)
        flower_name = response.json().get('results')[0]
        flower_name = flower_name['species']['commonNames']
        return flower_name

if __name__ == "__main__" : 

    parser = ArgumentParser()
    parser.add_argument("--flower_name", type = str, default = "orchid")
    args = parser.parse_args()

    result = text2image(args.flower_name)

    if result:
        image = result["image"]
        image_url = image['url']
        # print(image_url)
     
        response = requests.get(image_url)
        if response.status_code == 200:
            with open("IllusionDiffusion_output/flower.jpg", "wb") as file:
                file.write(response.content)
                print("Image downloaded successfully")
                flower_name = plantnet()
                print(flower_name)
        else:
            print("Failed to download image")

        
        
    
        

