from celery import Celery
from app import db
from models import Recommendation, RecommendationFeature
from schemas import RecommendationSchema, RecommendationFeatureSchema

celery = Celery(__name__)

@celery.task
def generate_recommendations(customer_id):
    # generate recommendations using machine learning algorithms
    recommendations = []
    for product in Product.query.all():
        score = calculate_score(customer_id, product.id)
        recommendation = Recommendation(customer_id=customer_id, product_id=product.id, score=score)
        db.session.add(recommendation)
        db.session.commit()
        recommendations.append(recommendation)
    return jsonify(RecommendationSchema(many=True).dump(recommendations))

@celery.task
def update_recommendation_features(recommendation_id):
    # update recommendation features using machine learning algorithms
    recommendation = Recommendation.query.get(recommendation_id)
    features = []
    for feature in RecommendationFeature.query.filter_by(recommendation_id=recommendation_id).all():
        feature_value = calculate_feature_value(recommendation.product_id, feature.feature_name)
        feature.feature_value = feature_value
        db.session.commit()
        features.append(feature)
    return jsonify(RecommendationFeatureSchema(many=True).dump(features))
