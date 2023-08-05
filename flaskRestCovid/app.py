from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.routes import initialize_routes
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_envvar('envFile')

restServer = Api(app)
jwt = JWTManager(app)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


initialize_routes(restServer)

if __name__ == "__main__":
    app.run(debug=True)