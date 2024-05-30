from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def send_notification(post_id):
    # implement notification logic here
    pass
