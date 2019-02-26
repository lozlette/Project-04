# from flask import Blueprint, request, jsonify, g
# from models.comment import Comment, CommentSchema
#
# api = Blueprint('comments', __name__)
#
# comments_schema = CommentSchema(many=True)
# comment_schema = CommentSchema()
#
# @api.route('/comments', methods=['GET'])
# def index():
#     comments = Comment.query.all()
#     return comments_schema.jsonify(comments)
#
# @api.route('/comments/<int:comment_id>', methods=['GET'])
# def show(comment_id):
#     comment = Comment.query.get(comment_id)
#     return comment_schema.jsonify(comment)
