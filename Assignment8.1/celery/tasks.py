from celery import Celery


celery_app = Celery("tasks", broker="redis://redis:6379/0")

@celery_app.task
def add_number(a, b):
    return a + b


