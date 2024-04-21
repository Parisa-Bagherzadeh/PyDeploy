## University System (Expert mode) 🧑🏻‍🎓  
This API allows you to manage students and courses within a university system.With this API, you can perform CRUD (Create, Read, Update, Delete) operations on students and courses, enabling you to maintain accurate records of enrolled students and available courses. 

You can run the API on your own system.  
    

1 - Set SQLALCHEMY_DATABASE_URL : 
```
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/database"
```
2 - Run the following command
```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=username -e POSTGRES_DB=database_name -d postgres
```  
3 - And run the following command
```
uvicorn main:app --relaod
```  
Or you can run the API on liara.ir :  
1 - Set SQLALCHEMY_DATABASE_URL variable  
2 - Run the following commnad :  
```
liara deploy --platform docker --port 80
```
