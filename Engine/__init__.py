from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from flask_login import LoginManager # type: ignore
from flask_socketio import SocketIO # type: ignore
from flask_admin import Admin # type: ignore
from .config import Config
from flask import Flask

login_manager: LoginManager = LoginManager()
login_manager.login_view = 'login_form'

db: SQLAlchemy = SQLAlchemy()
socketio: SocketIO = SocketIO()
admin = Admin(template_mode='bootstrap3')

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

    login_manager.init_app(app)
    db.init_app(app)
    socketio.init_app(app)
    admin.init_app(app)

    from Engine.errors.handlers import errors
    from Engine.admin.views import author

    app.register_blueprint(errors)
    app.register_blueprint(author)

    # Register custom Jinja filters
    @app.template_filter('start_prefix_text')
    def start_time_prefix_text_filter(start_time):
        """
        Determine the appropriate text for the start time based on the current time.

        Args:
            start_time (datetime): The start time to compare with the current time.

        Returns:
            str: The text prefix for the start time.
        """
        current_time = datetime.now(timezone.utc)
        return "Will start at" if current_time < start_time else "Started on"

    @app.template_filter('end_prefix_text')
    def end_time_prefix_text_filter(end_time):
        """
        Determine the appropriate text for the end time based on the current time.

        Args:
            end_time (datetime): The end time to compare with the current time.

        Returns:
            str: The text prefix for the end time.
        """
        current_time = datetime.now(timezone.utc)
        return "Ends at" if current_time < end_time else "Ended at"

    def after_request(response):
        """Ensure responses aren't cached"""
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    app.after_request(after_request)

    return app
