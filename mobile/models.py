from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Device(Base):
    __tablename__ = 'devices'
    device_id = Column(Integer, primary_key=True)
    platform = Column(String, nullable=False)
    model = Column(String, nullable=False)
    os_version = Column(String, nullable=False)

class MobileUser(Base):
    __tablename__ = 'mobile_users'
    mobile_user_id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("devices.device_id"))
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    device = relationship("Device", backref="mobile_users")

class Notification(Base):
    __tablename__ = 'notifications'
    notification_id = Column(Integer, primary_key=True)
    mobile_user_id = Column(Integer, ForeignKey("mobile_users.mobile_user_id"))
    message = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    mobile_user = relationship("MobileUser", backref="notifications")
