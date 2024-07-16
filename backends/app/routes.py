# backend/app/routes.py
from flask import Blueprint, request, jsonify
from app.models import User
from app.models import Admin
from app.models import Device
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


@main.route("/userRegister", methods=["POST"])
def user_register():
    data = request.get_json()
    new_user = User(
        username=data["username"], email=data["email"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})


@main.route("/userLogin", methods=["POST"])
def user_login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if (
        user and user.email == data["email"]
    ):  # Passwords should be hashed and checked securely
        access_token = create_access_token(identity={"username": user.username})
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials!"}), 401


@main.route("/userProtected", methods=["GET"])
@jwt_required()
def user_protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200









@main.route("/adminRegister", methods=["POST"])
def admin_register():
    data = request.get_json()
    new_admin = Admin(
        username=data["username"], password=data["password"]
    )
    db.session.add(new_admin)
    db.session.commit()
    return jsonify({"message": "Admin registered successfully!"})


@main.route("/adminLogin", methods=["POST"])
def admin_login():
    data = request.get_json()
    admin = Admin.query.filter_by(username=data["username"]).first()
    if (
        admin and admin.password == data["password"]
    ):  # Passwords should be hashed and checked securely
        access_token = create_access_token(identity={"username": admin.username})
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials!"}), 401


@main.route("/adminProtected", methods=["GET"])
@jwt_required()
def admin_protected():
    current_admin = get_jwt_identity()
    return jsonify(logged_in_as=current_admin), 200


@main.route("/devicedata", methods=["POST"])
def device_info():
    data = request.get_json()
    new_deviceinfo = Device(
        username=data["username"], imei=data["imei"], phonenumber= data["phonenumber"], complaint= data["complaint"]
    )
    db.session.add(new_deviceinfo)
    db.session.commit()
    return jsonify({"message": " Submitted successfully!"})