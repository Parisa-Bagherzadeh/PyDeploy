## Image base API  
This API allows you to submit an image and detects faces within the image using the InsightFace framework.  

### How to install  
```
pip install -r requirements.txt
```  
### Getting Started  
1 - Put your images in seperate folders in face_bank folder.  
2 - run the following command :  
```
python create_face_bank.py
```
It will create a vector for each detected face in the image and save the vectors in face_bank.npy file.  

3 - You need to run this commnad in terminal to start the api 
```
uvicorn main:app
```  
The base URL of the API endpoints is : 127.0.0.1:8000  
#### Endpoints  
* POST /deepface: Detects faces in the submitted image and attempts to identify individuals.  

![img](output/result.jpg)