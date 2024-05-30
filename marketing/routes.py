from flask import Blueprint, jsonify, request
from models import Campaign, Channel, Customer
from schemas import CampaignSchema, ChannelSchema, CustomerSchema
from tasks import send_campaign_email, update_campaign_stats

api = Blueprint('api', __name__)

campaign\_schema = CampaignSchema()
campaigns\_schema = CampaignSchema(many=True)
channel\_schema = ChannelSchema()
channel
