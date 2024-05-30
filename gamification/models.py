from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Badge(Base):
    __tablename__ = 'badges'
    badge_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class Achievement(Base):
    __tablename__ = 'achievements'
    achievement_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    badge_id = Column(Integer, ForeignKey("badges.badge_id"))
    earned_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="achievements")
    badge = relationship("Badge", backref="achievements")

class Leaderboard(Base):
    __tablename__ = 'leaderboards'
    leaderboard_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class LeaderboardEntry(Base):
    __tablename__ = 'leaderboard_entries'
    leaderboard_entry_id = Column(Integer, primary_key=True)
    leaderboard_id = Column(Integer, ForeignKey("leaderboards.leaderboard_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    score = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    leaderboard = relationship("Leaderboard", backref="entries")
    user = relationship("User", backref="leaderboard_entries")
