from Engine.models import Admin, Election, Position, Candidate, Course, Organization, Voter, Vote
from flask import Blueprint, Response, jsonify, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.wrappers.response import Response as RedirectResponse
from Engine.admin.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user # type: ignore
from flask_admin.contrib.sqla import ModelView # type: ignore
from flask_login import current_user # type: ignore
from Engine import admin as admin_instance, db
from typing import Optional

author = Blueprint('author', __name__, template_folder='templates/admin', static_folder='static/admin')

class AdminModelView(ModelView):

    def is_accessible(self):
        """
        Since the app only allows login for admins, current_user will always be an admin
        """
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login'))

# Add views
admin_instance.add_view(AdminModelView(Admin, db.session))
admin_instance.add_view(AdminModelView(Election, db.session))
admin_instance.add_view(AdminModelView(Course, db.session))
admin_instance.add_view(AdminModelView(Position, db.session))
admin_instance.add_view(AdminModelView(Candidate, db.session))
admin_instance.add_view(AdminModelView(Organization, db.session))
admin_instance.add_view(AdminModelView(Voter, db.session))
admin_instance.add_view(AdminModelView(Vote, db.session))

@author.get("/login")
def login_form() -> str:
    """
    Displays login form.

    Returns:
        rendered login.html template with the login form
    """
    logout_user()
    form: LoginForm = LoginForm()
    return render_template("login.html", form=form)

@author.post("/login")
def login() -> Response:
    """
    Logs user in.

    Returns:
        - JSON response with status=success if login is successful
        - JSON response with status=error, error message, and form errors if login is unsuccessful
    """
    form: LoginForm = LoginForm(request.form)
    email_input: str = form.login_email.data.strip()

    if not form.validate():
        return jsonify({
            'status': 'error',
            'message': [field.errors for field in form if field.errors]
        })

    admin_user: Optional[Admin] = Admin.query.filter_by(email=email_input).first()

    if admin_user and check_password_hash(str(admin_user.password_hash), form.login_password.data):
        login_user(admin_user)
        return jsonify({
            'status': 'success',
            'url': url_for('index._index')
        })

    return jsonify({
        'status': 'error',
        'message': ["No matching password"]
    })

@author.get("/logout")
def logout() -> RedirectResponse:
    """
    Logs user out.

    Returns:
        Redirects to the login_form route
    """
    logout_user()
    return redirect(url_for('user.login_form'))

@author.get("/register")
def register_form() -> str:
    """
    Displays registration form.

    Returns:
        rendered register.html template with the registration form
    """
    return render_template("register.html", form=RegisterForm())

@author.post("/register")
def register() -> RedirectResponse:
    """
    Registers user.

    Returns:
        - Redirects to the login_form route if registration is successful
        - Renders the register.html template with form errors if registration is unsuccessful
    """
    form: RegisterForm = RegisterForm(request.form)

    if not form.validate():
        return jsonify({
            'status': 'error',
            'message': [field.errors for field in form if field.errors]
        })

    try:
        admin_user: Admin = Admin(
            username=form.register_username.data,
            email=form.register_email.data,
            password_hash=generate_password_hash(form.register_password.data)
        )

        db.session.add(admin_user)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'url': url_for('user.login_form')
        })

    except:
        return jsonify({
            'status': 'error',
            'message': ["Error in registering user"]
        })