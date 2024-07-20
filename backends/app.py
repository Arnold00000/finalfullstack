from flask import Flask,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow
# from app.models import User



# Initialize the flask app
app = Flask(__name__)

app.config.from_object("app.config.Config")
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

# Import and register blueprints
from app.routes import main as main_blueprint

app.register_blueprint(main_blueprint)


# Import and configure schemas
from app.schemas import configure as configure_schemas
configure_schemas(app)  # Pass the app to initialize Marshmallow

@app.route("/")
def home():
    return "Welcome to the TAC Predictor API!"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
