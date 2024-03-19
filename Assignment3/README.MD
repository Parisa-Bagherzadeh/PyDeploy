
## 🍎Haftsin API 
Welcome to the Haftsin API documentation! This API celebrates the rich cultural tradition of Nowruz, the Persian New Year, through the symbolic items of the Haftsin table. Haftsin, meaning "seven S's" in Persian, is a tabletop arrangement of seven symbolic items, each starting with the letter 'S' in the Persian alphabet, representing various elements of life and nature.

Through this API, you can explore and learn about these items, accompanied by images for a visual representation.  
The API has been deployed here https://pydeploy-70jp.onrender.com  
  
### How to install  
```
pip install -r requirements.txt
```  

### Getting Started  
First you need to run this commnad in terminal to start the api 
```
uvicorn main:app
```  
The base URL of the API endpoints is : 127.0.0.1:8000  
#### Endpoints  
##### 1 - 127.0.0.1:8000/sins  
This endpoint provides a list of all seven symbolic items of Haftsin  

##### 2 - 127.0.0.1:8000/sins/{sin_name}
Instead of sin_name you can type any of haftsin symbols, it will return the description of the symbol  
Example :  
```
127.0.0.1:8000/sins/سیب
```
##### 3 - 127.0.0.1:8000/pieces/{piece_name}/image  
  Instead of piece_name you can type any of haftsin symbols and it will return the image of that symbol  
Example : 
```
127.0.0.1:8000/pieces/سیب/image
```  
<img src="images/sib.jpg" alt="Sample Image" style="width:300px;height:300px;">  

```
127.0.0.1:8000/pieces/سنبل/image
```  
<img src="images/sonbol.jpg" alt="Sample Image" style="width:300px;height:300px;">  

```
127.0.0.1:8000/pieces/سکه/image
```  
<img src="images/seke.jpg" alt="Sample Image" style="width:300px;height:300px;">  


#### All images have been created by fal.ai website :)
