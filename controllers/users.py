from flask import Blueprint, request, g, jsonify
from models.user import User, UserSchema
from models.message import Message, MessageSchema
from lib.secure_route import secure_route

api = Blueprint('users', __name__)

users_schema = UserSchema(many=True)
user_schema = UserSchema()
message_schema = MessageSchema()
messages_schema = MessageSchema()

@api.route('/users', methods=['GET'])
@secure_route
def index():
    users = User.query.all()
    return users_schema.jsonify(users)

@api.route('/users/<int:user_id>', methods=['GET'])
# @secure_route
def show(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user)

@api.route('/users/<int:user_id>/inbox', methods=['POST'])
@secure_route
def create(user_id):
    message, errors = message_schema.load(request.get_json())

    if errors:
        return jsonify(errors), 422

    message.sender = g.current_user
    message.receiver = User.query.get(user_id)

    message.save()

    return message_schema.jsonify(message)
