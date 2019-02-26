# from app import db, ma
#
# class User(db.Model):
#
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     password_hash = db.Column(db.String(200), nullable=False)
#     avatar = db.Column(db.String(200), nullable=False)
#
# class UserSchema(ma.ModelSchema):
#
#     class Meta:
#         model = User
