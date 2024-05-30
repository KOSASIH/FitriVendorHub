from flask import Blueprint, jsonify
from .models import User
from .schemas import user_schema, users_schema

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

@api.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return user_schema.jsonify(user)

@api.route('/users', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201

@api.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    username = request.json['username']
    email = request.json['email']

    user.username = username
    user.email = email

    db.session.commit()

    return user_schema.jsonify(user)

@api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return '', 204
