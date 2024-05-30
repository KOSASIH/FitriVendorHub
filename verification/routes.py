from flask import Blueprint, jsonify, request
from.models import User, Verification
from.schemas import UserSchema, VerificationSchema

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([UserSchema().dump(user) for user in users])

@api.route('/verifications', methods=['GET'])
def get_verifications():
    verifications = Verification.query.all()
    return jsonify([VerificationSchema().dump(verification) for verification in verifications])

@api.route('/users/<int:user_id>/verifications', methods=['GET'])
def get_user_verifications(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    verifications = user.verifications
    return jsonify([VerificationSchema().dump(verification) for verification in verifications])

@api.route('/verifications/<int:verification_id>', methods=['GET'])
def get_verification(verification_id):
    verification = Verification.query.get(verification_id)
    if not verification:
        return jsonify({'error': 'Verification not found'}), 404
    return jsonify(VerificationSchema().dump(verification))
