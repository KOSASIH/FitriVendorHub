from flask import Blueprint, jsonify, request
from.models import User, Conversation, Message
from.schemas import UserSchema, ConversationSchema, MessageSchema

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([UserSchema().dump(user) for user in users])

@api.route('/conversations', methods=['GET'])
def get_conversations():
    conversations = Conversation.query.all()
    return jsonify([ConversationSchema().dump(conversation) for conversation in conversations])

@api.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([MessageSchema().dump(message) for message in messages])

@api.route('/users/<int:user_id>/conversations', methods=['GET'])
def get_user_conversations(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    conversations = user.conversations
    return jsonify([ConversationSchema().dump(conversation) for conversation in conversations])

@api.route('/conversations/<int:conversation_id>/messages', methods=['GET'])
def get_conversation_messages(conversation_id):
    conversation = Conversation.query.get(conversation_id)
    if not conversation:
        return jsonify({'error': 'Conversation not found'}), 404
    messages = conversation.messages
    return jsonify([MessageSchema().dump(message) for message in messages])
