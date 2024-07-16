from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow


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


@app.route("/")
def home():
    return "Welcome to the TAC Predictor API!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
