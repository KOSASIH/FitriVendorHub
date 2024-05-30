from flask import Blueprint, jsonify, request
from.models import User, Post, Comment
from.schemas import UserSchema, PostSchema, CommentSchema

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([UserSchema().dump(user) for user in users])

@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([PostSchema().dump(post) for post in posts])

@api.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify([CommentSchema().dump(comment) for comment in comments])

@api.route('/users/<int:user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    posts = user.posts
    return jsonify([PostSchema().dump(post) for post in posts])

@api.route('/posts/<int:post_id>/comments', methods=['GET'])
def get_post_comments(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    comments = post.comments
    return jsonify([CommentSchema().dump(comment) for comment in comments])
