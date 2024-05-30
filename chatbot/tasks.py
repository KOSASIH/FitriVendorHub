from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def process_message(message_id):
    # implement message processing logic here
    pass
