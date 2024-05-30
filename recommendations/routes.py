from flask import Blueprint, request, jsonify
from app import db
from models import Recommendation, RecommendationFeature
from schemas import RecommendationSchema, RecommendationFeatureSchema
from tasks import generate_recommendations, update_recommendation_features

recommendations_blueprint = Blueprint('recommendations', __name__)

@recommendations_blueprint.route('/recommendations', methods=['GET'])
def get_recommendations(customer_id):
    recommendations = Recommendation.query.filter_by(customer_id=customer_id).all()
    return jsonify(RecommendationSchema(many=True).dump(recommendations))

@recommendations_blueprint.route('/recommendations/<int:recommendation_id>', methods=['GET'])
def get_recommendation(recommendation_id):
    recommendation = Recommendation.query.get(recommendation_id)
    if recommendation is None:
        return jsonify({'error': 'Recommendation not found'}), 404
    return jsonify(RecommendationSchema().dump(recommendation))

@recommendations_blueprint.route('/recommendations', methods=['POST'])
def create_recommendation():
    data = request.get_json()
    recommendation = Recommendation(**data)
    db.session.add(recommendation)
    db.session.commit()
    return jsonify(RecommendationSchema().dump(recommendation)), 201

@recommendations_blueprint.route('/recommendations/<int:recommendation_id>', methods=['PUT'])
def update_recommendation(recommendation_id):
    recommendation = Recommendation.query.get(recommendation_id)
    if recommendation is None:
        return jsonify({'error': 'Recommendation not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(recommendation, key, value)
    db.session.commit()
    return jsonify(RecommendationSchema().dump(recommendation))

@recommendations_blueprint.route('/recommendations/<int:recommendation_id>', methods=['DELETE'])
def delete_recommendation(recommendation_id):
    recommendation = Recommendation.query.get(recommendation_id)
    if recommendation is None:
        return jsonify({'error': 'Recommendation not found'}), 404
    db.session.delete(recommendation)
    db.session.commit()
    return jsonify({'message': 'Recommendation deleted successfully'})

@recommendations_blueprint.route('/recommendations/generate', methods=['POST'])
def generate_recommendations_route():
    data = request.get_json()
    customer_id = data.get('customer_id')
    return generate_recommendations.delay(customer_id)

@recommendations_blueprint.route('/recommendations/update-features/<int:recommendation_id>', methods=['POST'])
def update_recommendation_features_route(recommendation_id):
    return update_recommendation_features.delay(recommendation_id)
