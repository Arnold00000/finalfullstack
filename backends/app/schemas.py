# app/schemas.py
from flask import Flask
from flask_marshmallow import Marshmallow

ma=Marshmallow()

class DeviceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username' 'imei', 'phonenumber', 'complaint')

class UserSchema(ma.Schema):
    class Meta:
        fields = ( 'id', 'username', 'email')


# class AdminSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         fields = ('id', 'username', 'password')

def configure(app: Flask):
    ma.init_app(app)


