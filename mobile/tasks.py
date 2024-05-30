from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def send_notification(mobile_user_id, message):
    # implement sending notification logic here
    pass
