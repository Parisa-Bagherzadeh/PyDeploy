## University System (Expert mode) 🧑🏻‍🎓  
This is an API you can get and post students and courses.  
You can run the API on your own system by doing the following steps :  
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
