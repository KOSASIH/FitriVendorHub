from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Conversation(Base):
    __tablename__ = 'conversations'
    conversation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="conversations")

class Message(Base):
    __tablename__ = 'essages'
    message_id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey("conversations.conversation_id"))
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    conversation = relationship("Conversation", backref="messages")
