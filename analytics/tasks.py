from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def process_event(event_id):
    # implement event processing logic here
    pass
