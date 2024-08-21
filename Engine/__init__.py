from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO # type: ignore
from .admin import setup_admin
from .config import Config
from flask import Flask

db: SQLAlchemy = SQLAlchemy()
socketio: SocketIO = SocketIO()

def create_app(config_class=Config) -> Flask:
    """
    Creates and configures an instance of the Flask application.

    This function initializes the Flask application, sets up the configuration,
    initializes the database and socketio, and registers the blueprints for the
    index, candidate, and error views.

    Returns:
    --------
        app: A Flask application instance.
    """

    app: Flask = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    socketio.init_app(app)

    setup_admin(app)

    # from Engine.index.views import index
    # from Engine.candidate.views import candidate
    from Engine.errors.handlers import errors

    # app.register_blueprint(index)
    # app.register_blueprint(candidate)
    app.register_blueprint(errors)

    return app
