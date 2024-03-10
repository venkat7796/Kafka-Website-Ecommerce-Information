from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv

from flow.entityproduct import blp as ProductBluePrint
from flow.entityuser import blp as UserBluePrint

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["API_TITLE"] = "ECommerce Website"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["PROPOGATE_EXCEPTIONS"] = True

    api = Api(app=app)

    api.register_blueprint(ProductBluePrint)
    api.register_blueprint(UserBluePrint)

    return app