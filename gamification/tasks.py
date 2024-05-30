from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def award_badge(user_id, badge_id):
    # implement awarding badge logic here
    pass

@celery.task
def update_leaderboard(leaderboard_id, user_id, score):
    # implement updating leaderboard logic here
    pass
