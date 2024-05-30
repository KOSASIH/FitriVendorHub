from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

class BadgeSchema(Schema):
    badge_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

class AchievementSchema(Schema):
    achievement_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    badge_id = fields.Int(required=True)
    earned_at = fields.DateTime(required=True)

class LeaderboardSchema(Schema):
    leaderboard_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

class LeaderboardEntrySchema(Schema):
    leaderboard_entry_id = fields.Int(dump_only=True)
    leaderboard_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    score = fields.Int(required=True)
    created_at = fields.DateTime(required=True)
