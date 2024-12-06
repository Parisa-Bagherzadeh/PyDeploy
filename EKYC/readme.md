#eKYC


## How to run


1. Run redis container
```
docker pull redis
docker run --name some-redis -d -p 6379:6379 redis
```

2. Run celery tasks
```
celery -A celery_tasks worker --loglevel=ERROR
```

3. Run main API
```
fastapi dev app.py or uvicorn app:app
```