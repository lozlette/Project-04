from flask import Blueprint, request, jsonify, g
from models.message import Message, MessageSchema
from lib.secure_route import secure_route

api = Blueprint('messages', __name__)

messages_schema = MessageSchema(many=True)
message_schema = MessageSchema()

@api.route('/messages', methods=['GET'])
def index():
    messages = Message.query.all()
    return messages_schema.jsonify(messages)

@api.route('/messages/<int:message_id>', methods=['GET'])
def show(message_id):
    message = Message.query.get(message_id)
    return message_schema.jsonify(message)

@api.route('/messages', methods=['POST'])
@secure_route
def create():
    message, errors = message_schema.load(request.get_json())
    message.sender = g.current_user
    message.receiver = message_schema.receiver_id

    if errors:
        return jsonify(errors), 422
    message.save()

    return message_schema.jsonify(message)
