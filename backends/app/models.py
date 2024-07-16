from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        
class Device(db.Model):
    __tablename__ = 'deviceinfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    imei = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(100), nullable=False)
    complaint = db.Column(db.String(255), nullable=False)

   
    def __init__(self, username, imei, phonenumber, complaint):
        self.username = username
        self.imei = imei
        self.phonenumber = phonenumber
        self.complaint = complaint


    

