## AI Services with Flask and Docker
This is a Repository contains code for deploying AI services using Flask within a Docker container


#### Usage  
Run the followigng commands:
```
1 - docker build -t mywebsite .
2 - docker network create my_network
3 - docker run --network my_network --name some-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=username -e POSTGRES_DB=database -d postgres
4 - docker run -v $(pwd):/myapp -p 8080:5000 --network my_network 
```

