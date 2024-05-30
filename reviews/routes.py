from flask import Blueprint
from.views import ReviewView, ReviewImageView

reviews_blueprint = Blueprint('reviews', __name__)

review_view = ReviewView()
review_image_view = ReviewImageView()

@reviews_blueprint.route('/reviews', methods=['GET'])
def get_all_reviews():
    return review_view.get_all_reviews()

@reviews_blueprint.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    return review_view.get_review(review_id)

@reviews_blueprint.route('/reviews', methods=['POST'])
def create_review():
    return review_view.create_review()

@reviews_blueprint.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    return review_view.update_review(review_id)

@reviews_blueprint.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    return review_view.delete_review(review_id)

@reviews_blueprint.route('/reviews/<int:review_id>/images', methods=['GET'])
def get_all_review_images(review_id):
    return review_image_view.get_all_review_images(review_id)

@reviews_blueprint.route('/reviews/<int:review_id>/images/<int:image_id>', methods=['GET'])
def get_review_image(review_id, image_id):
    return review_image_view.get_review_image(review_id, image_id)

@reviews_blueprint.route('/reviews/<int:review_id>/images', methods=['POST'])
def create_review_image(review_id):
    return review_image_view.create_review_image(review_id)

@reviews_blueprint.route('/reviews/<int:review_id>/images/<int:image_id>', methods=['PUT'])
def update_review_image(review_id, image_id):
    return review_image_view.update_review_image(review_id, image_id)

@reviews_blueprint.route('/reviews/<int:review_id>/images/<int:image_id>', methods=['DELETE'])
def delete_review_image(review_id, image_id):
    return review_image_view.delete_review_image(review_id, image_id)
