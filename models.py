from app import db
# from datetime import datetime


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     phone = db.Column(db.Integer)
#
#     def __init__(self, *args, **kwargs):
#         super(User, self).__init__(*args, **kwargs)
#
#     def __repr__(self):
#         return f" id {self.id} user {self.name} email {self.email} phone {self.phone}"

