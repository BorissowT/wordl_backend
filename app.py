from flask import Flask

from configs.config import LocalConfig, LiveConfig


def create_app(debug=True):
    config = LocalConfig if debug else LiveConfig

    # Create app
    app = Flask(__name__)

    # Set configuration variables
    app.config.from_object(config)
    app.secret_key = app.config['SECRET_KEY']
    app.url_map.strict_slashes = False

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'

    return app


