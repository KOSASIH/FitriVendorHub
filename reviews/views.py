from flask import request, jsonify
from app import db
from.models import Review, ReviewImage
from.schemas import ReviewSchema, ReviewImageSchema

class ReviewView:
    def get_all_reviews(self):
        reviews = Review.query.all()
        return jsonify(ReviewSchema(many=True).dump(reviews))

    def get_review(self, review_id):
        review = Review.query.get(review_id)
        if review is None:
            return jsonify({'error': 'Review not found'}), 404
        return jsonify(ReviewSchema().dump(review))

    def create_review(self):
        data = request.get_json()
        review = Review(**data)
        db.session.add(review)
        db.session.commit()
        return jsonify(ReviewSchema().dump(review)), 201

    def update_review(self, review_id):
        review = Review.query.get(review_id)
        if review is None:
            return jsonify({'error': 'Review not found'}), 404
        data = request.get_json()
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return jsonify(ReviewSchema().dump(review))

    def delete_review(self, review_id):
        review = Review.query.get(review_id)
        if review is None:
            return jsonify({'error': 'Review not found'}), 404
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'Review deleted successfully'})

class ReviewImageView:
    def get_all_review_images(self, review_id):
        review_images = ReviewImage.query.filter_by(review_id=review_id).all()
        return jsonify(ReviewImageSchema(many=True).dump(review_images))

    def get_review_image(self, review_id, image_id):
        review_image = ReviewImage.query.filter_by(review_id=review_id, id=image_id).first()
        if review_image is None:
            return jsonify({'error': 'Review image not found'}), 404
        return jsonify(ReviewImageSchema().dump(review_image))

    def create_review_image(self, review_id):
        data = request.get_json()
        review_image = ReviewImage(review_id=review_id, **data)
        db.session.add(review_image)
        db.session.commit()
        return jsonify(ReviewImageSchema().dump(review_image)), 201

    def update_review_image(self, review_id, image_id):
        review_image = ReviewImage.query.filter_by(review_id=review_id, id=image_id).first()
        if review_image is None:
            return jsonify({'error': 'Review image not found'}), 404
        data = request.get_json()
        for key, valuein data.items():
            setattr(review_image, key, value)
        db.session.commit()
        return jsonify(ReviewImageSchema().dump(review_image))

    def delete_review_image(self, review_id, image_id):
        review_image = ReviewImage.query.filter_by(review_id=review_id, id=image_id).first()
        if review_image is None:
            return jsonify({'error': 'Review image not found'}), 404
        db.session.delete(review_image)
        db.session.commit()
        return jsonify({'message': 'Review image deleted successfully'})
