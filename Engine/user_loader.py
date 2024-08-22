# /app/auth/login_manager.py
from Engine.models.Admin import Admin
from Engine import login_manager

@login_manager.user_loader
def load_user(user_id: str):
    """
    Loads the current user
    """
    return Admin.query.get(int(user_id))
