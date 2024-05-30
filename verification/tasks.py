from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def send_verification_code(user_id):
    # implement sending verification code logic here
    pass
