from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models import Vendor, Product, Review, Recommendation, Inventory, Shipping, Loyalty, Analytics, Social, Chatbot, Verification, Mobile, Gamification, Marketing
from schemas import VendorSchema, ProductSchema, ReviewSchema, RecommendationSchema, InventorySchema, ShippingSchema, LoyaltySchema, AnalyticsSchema, SocialSchema, ChatbotSchema, VerificationSchema, MobileSchema, GamificationSchema, MarketingSchema

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    vendor = Vendor.query.filter_by(email=email).first()

    if not vendor or vendor.password != password:
        return jsonify({'error': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=vendor.id)
    return jsonify({'access_token': access_token})

@auth.route('/register', methods=['POST'])
def register():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')

    vendor = Vendor(name=name, email=email, password=password)
    db.session.add(vendor)
    db.session.commit()

    return jsonify({'message': 'Vendor registered successfully'})

@auth.route('/me', methods=['GET'])
@jwt_required
def me():
    vendor_id = get_jwt_identity()
    vendor = Vendor.query.get(vendor_id)

    return jsonify(VendorSchema().dump(vendor))
