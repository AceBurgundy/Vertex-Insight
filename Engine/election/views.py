from flask import Blueprint, render_template, abort
from Engine.models import Election
from typing import Optional

election = Blueprint('election', __name__, template_folder='templates/election', static_folder='static/election')

@election.get('/election/<title>/candidates')
def candidates(title: str) -> str:
    """
    Render the candidates for a specific election based on the title.

    Args:
        title (str): The title of the election.

    Returns:
        Rendered HTML template with the list of candidates for the given election title.
    """
    election: Optional[Election] = Election.query.filter_by(title=title).first()

    if election is None:
        abort(404, description="Election not found")

    return render_template('candidates.html', election=election, candidates=election.candidates)