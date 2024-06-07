import requests



response = requests.post("http://127.0.0.1:5000/blog")
print(response.text)