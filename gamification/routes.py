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

@api.route('/users/<int:user_id>/achievements', methods=['GET'])
def get_user_achievements(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    achievements = user.achievements
    return jsonify([AchievementSchema().dump(achievement) for achievement in achievements])

@api.route('/leaderboards/<int:leaderboard_id>/entries', methods=['GET'])
def get_leaderboard_entries_by_leaderboard(leaderboard_id):
    leaderboard = Leaderboard.query.get(leaderboard_id)
    if not leaderboard:
        return jsonify({'error': 'Leaderboard not found'}), 404
    entries = leaderboard.entries
    return jsonify([LeaderboardEntrySchema().dump(entry) for entry in entries])

@api.route('/achievements/<int:achievement_id>', methods=['GET'])
def get_achievement(achievement_id):
    achievement = Achievement.query.get(achievement_id)
    if not achievement:
        return jsonify({'error': 'Achievement not found'}), 404
    return jsonify(AchievementSchema().dump(achievement))

@api.route('/leaderboard_entries/<int:leaderboard_entry_id>', methods=['GET'])
def get_leaderboard_entry(leaderboard_entry_id):
    leaderboard_entry = LeaderboardEntry.query.get(leaderboard_entry_id)
    if not leaderboard_entry:
        return jsonify({'error': 'Leaderboard entry not found'}), 404
    return jsonify(LeaderboardEntrySchema().dump(leaderboard_entry))
