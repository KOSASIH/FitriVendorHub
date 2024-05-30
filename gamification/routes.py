from flask import Blueprint, jsonify, request
from.models import User, Badge, Achievement, Leaderboard, LeaderboardEntry
from.schemas import UserSchema, BadgeSchema, AchievementSchema, LeaderboardSchema, LeaderboardEntrySchema

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([UserSchema().dump(user) for user in users])

@api.route('/badges', methods=['GET'])
def get_badges():
    badges = Badge.query.all()
    return jsonify([BadgeSchema().dump(badge) for badge in badges])

@api.route('/achievements', methods=['GET'])
def get_achievements():
    achievements = Achievement.query.all()
    return jsonify([AchievementSchema().dump(achievement) for achievement in achievements])

@api.route('/leaderboards', methods=['GET'])
def get_leaderboards():
    leaderboards = Leaderboard.query.all()
    return jsonify([LeaderboardSchema().dump(leaderboard) for leaderboard in leaderboards])

@api.route('/leaderboard_entries', methods=['GET'])
def get_leaderboard_entries():
    leaderboard_entries = LeaderboardEntry.query.all()
    return jsonify([LeaderboardEntrySchema().dump(leaderboard_entry) for leaderboard_entry in leaderboard_entries])

@api.route('/award_badge', methods=['POST'])
def award_badge_endpoint():
    data = request.get_json()
    user_id = data['user_id']
    badge_id = data['badge_id']
    # Call celery task
    update_leaderboard.delay(badge_id, user_id)
    return jsonify({"message": "Badge awarded successfully"})

@api.route('/update_leaderboard', methods=['POST'])
def update_leaderboard_endpoint():
    data = request.get_json()
    leaderboard_id = data['leaderboard_id']
    user_id = data['user_id']
    score = data['score']
    # Call celery task
    award_badge.delay(user_id, leaderboard_id)
    return jsonify({"message": "Leaderboard updated successfully"})
