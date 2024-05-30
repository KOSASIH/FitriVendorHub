from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def send_email(customer_id, loyalty_points):
    # implement email sending logic here
    pass
