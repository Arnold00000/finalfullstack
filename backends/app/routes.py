# backend/app/routes.py
from flask import Blueprint, request, jsonify
from app.models import User
from app.models import Admin
from app.models import Device
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_marshmallow import Marshmallow
from app.schemas import DeviceSchema
from app.schemas import UserSchema
# from app.schemas import AdminSchema


main = Blueprint("main", __name__)
# ma = Marshmallow(main)

# Initialize Schema
device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# admin_schema = AdminSchema()
# admins_schema = AdminSchema(many=True)


@main.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

#CREATE USER
@main.route("/userRegister", methods=["POST"])
def user_register():
    data = request.get_json()
    new_user = User(
        username=data["username"], email=data["email"]
    )
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify({"message": "User registered successfully!"})

#USER LOGIN
@main.route("/userLogin", methods=["POST"])
def user_login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if (
        user and user.email == data["email"]
    ):  # Passwords should be hashed and checked securely
        access_token = create_access_token(identity={"username": user.username})
        return jsonify(access_token=access_token)
    return user_schema.jsonify({"message": "Invalid credentials!"}), 401

#CURRENT USER
@main.route("/userProtected", methods=["GET"])
@jwt_required()
def user_protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200




#CREATE ADMIN
#admins are added directly from the database

# @main.route("/adminRegister", methods=["POST"])
# def admin_register():
#     data = request.get_json()
#     new_admin = Admin(
#         username=data["username"], password=data["password"]
#     )
#     db.session.add(new_admin)
#     db.session.commit()
#     return admin_schema.jsonify({"message": "Admin registered successfully!"})


#ADMIN LOGIN
@main.route("/adminLogin", methods=["POST"])
def admin_login():
    data = request.get_json()
    admin = Admin.query.filter_by(username=data["username"]).first()
    if (
        admin and admin.password == data["password"]
    ):  # Passwords should be hashed and checked securely
        access_token = create_access_token(identity={"username": admin.username})
        return jsonify(access_token=access_token)
    # return admin_schema.jsonify({"message": "Invalid credentials!"}), 401
    return jsonify({"message": "Invalid credentials!"}), 401


# CURRENT ADMIN 
@main.route("/adminProtected", methods=["GET"])
@jwt_required()
def admin_protected():
    current_admin = get_jwt_identity()
    # return admin_schema.jsonify(logged_in_as=current_admin), 200
    return jsonify(logged_in_as=current_admin), 200



#USER POST DATA
@main.route("/devicedata", methods=["POST"])
def device_info():
    data = request.get_json()
    new_deviceinfo = Device(
        username=data["username"], imei=data["imei"], phonenumber= data["phonenumber"], complaint= data["complaint"]
    )
    db.session.add(new_deviceinfo)
    db.session.commit()
    return jsonify({"message": " Submitted successfully!"})


#GET ALL USER DATA
@main.route("/deviceinformation", methods=["GET"])
# @jwt_required()
def get_all_device_data():
    devices = Device.query.all()
    # Serialize device data using devices_schema
    serialized_data = devices_schema.dump(devices)
    return jsonify(serialized_data), 200



#USER DATA DELETE
@main.route("/datadelete/<id>", methods=["DELETE"])
def delete_device_data(id):
    device = Device.query.get(id)
    db.session.delete(device)
    db.session.commit()
    return device_schema.jsonify(device)



# #USER DATA UPDATE
# @main.route("/dataupdate/<id>", methods=["PUT"])
# def update_device_data(id):
#     device = Device.query.get(id)
#     data = request.get_json()
#     device.username = data["username"]
#     device.imei = data["imei"]  
#     device.phonenumber = data["phonenumber"]
#     device.complaint = data["complaint"]
#     db.session.commit()
#     return device_schema.jsonify(device)


