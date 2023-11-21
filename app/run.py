from flask import Flask

from app.config import Config
from flask_swagger_ui import get_swaggerui_blueprint


def create_app(config_class: Config = Config):

    # Create app
    app = Flask(__name__)

    # Set configuration variables
    app.config.from_object(config_class)
    app.secret_key = app.config['SECRET_KEY']
    app.url_map.strict_slashes = False

    if config_class.FLASK_ENV == "development":
        # init swagger
        SWAGGER_URL = '/api/docs'
        # URL for exposing Swagger UI (without trailing '/')
        API_URL = '/static/swagger.json'
        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
            API_URL,
            config={  # Swagger UI config overrides
                'app_name': "Sidecar application"
            },
            # oauth_config={  # OAuth config.
            # See
            # https://github.com/swagger-api/swagger-ui#oauth2-configuration .
            #    'clientId': "your-client-id",
            #    'clientSecret': "your-client-secret-if-required",
            #    'realm': "your-realms",
            #    'appName': "your-app-name",
            #    'scopeSeparator': " ",
            #    'additionalQueryStringParams': {'test': "hello"}
            # }
        )
        app.register_blueprint(swaggerui_blueprint)


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5005)
