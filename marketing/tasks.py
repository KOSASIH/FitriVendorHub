from app import celery
from models import Campaign, Channel, Customer
from schemas import CampaignSchema, ChannelSchema, CustomerSchema

@celery.task
def send_campaign\_email(campaign\_id):
    campaign = Campaign.query.get(campaign\_id)
    customers = Customer.query.join(customer\_campaign).filter(customer\_campaign.c.campaign\_id == campaign\_id).all()
    # send email to each customer

@celery.task
def update\_campaign\_stats():
    campaigns = Campaign.query.all()
    for campaign in campaigns:
        # update campaign stats
