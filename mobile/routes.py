from flask import Blueprint, jsonify, request
from.models import Device, MobileUser, Notification
from.schemas import DeviceSchema, MobileUserSchema, NotificationSchema

api = Blueprint('api', __name__)

@api.route('/devices', methods=['GET'])
def get_devices():
    devices = Device.query.all()
    return jsonify([DeviceSchema().dump(device) for device in devices])

@api.route('/mobile_users', methods=['GET'])
def get_mobile_users():
    mobile_users = MobileUser.query.all()
    return jsonify([MobileUserSchema().dump(mobile_user) for mobile_user in mobile_users])

@api.route('/notifications', methods=['GET'])
def get_notifications():
    notifications = Notification.query.all()
    return jsonify([NotificationSchema().dump(notification) for notification in notifications])

@api.route('/mobile_users/<int:mobile_user_id>/notifications', methods=['GET'])
def get_mobile_user_notifications(mobile_user_id):
    mobile_user = MobileUser.query.get(mobile_user_id)
    if not mobile_user:
        return jsonify({'error': 'Mobile user not found'}), 404
    notifications = mobile_user.notifications
    return jsonify([NotificationSchema().dump(notification) for notification in notifications])

@api.route('/notifications/<int:notification_id>', methods=['GET'])
def get_notification(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        return jsonify({'error': 'Notification not found'}), 404
    return jsonify(NotificationSchema().dump(notification))
