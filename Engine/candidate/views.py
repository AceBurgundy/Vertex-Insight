from flask import jsonify, render_template, Blueprint, request, url_for
from Engine.candidate.forms import CommentForm
from Engine.text_processor import process_text
from werkzeug.datastructures import MultiDict
from Engine.models.models import Candidate, Comment
from Engine.translator import translate
from Engine.emotion import get_emotion
from typing import Dict, List, Union
from Engine import db, socketio
from flask_socketio import emit

candidate: Blueprint = Blueprint('candidate', __name__, template_folder='templates/candidate', static_folder='static/candidate')
DICT_TYPE = Dict[str, Union[str, int]]

@socketio.on('get_highest_rated_candidate')
def broadcast_highest_rated_candidate() -> None:
    candidates: Candidate = Candidate.query.all()
    highest_rated_candidate: Union[DICT_TYPE, None] = None

    for candidate in candidates:
        rating: Dict[str, int] = candidate.get_rating()
        positive_rating: int = rating.get('POSITIVE', 0)

        candidate_data: DICT_TYPE = {
            'id': candidate.id,
            'name': candidate.name,
            'positive_ratings': positive_rating,
        }

        if highest_rated_candidate is None:
            highest_rated_candidate: Union[DICT_TYPE, None] = candidate_data
            continue

        if candidate_data['positive_ratings'] > highest_rated_candidate['positive_ratings']:
            highest_rated_candidate: Union[DICT_TYPE, None] = candidate_data

    emit('highest_rated_candidate', highest_rated_candidate, broadcast=True)

@candidate.get("/candidates")
def get_candidates():
    """
    Retrieves all candidates
    """
    candidates: List[Candidate] = Candidate.query.all()
    data: DICT_TYPE = []

    for candidate in candidates:
        data.append({
            'id': candidate.id,
            'name': candidate.name,
            'content': candidate.content,
            'image': url_for('static', filename='candidate_pictures/' + candidate.image),
            'rating': candidate.get_rating()
        })

    return jsonify({ 'candidates': data })

@candidate.get("/candidate/<int:candidate_id>")
def get_candidate(candidate_id):
    """
    Load the page on a specific candidate.

    Returns:
    --------
        render_template: Rendered HTML template with necessary data.
    """

    comment_form: CommentForm = CommentForm()
    candidate: Candidate = Candidate.query.get(candidate_id)

    return render_template(
        "candidate.html",
        candidate=candidate,
        comment_form=comment_form
    )

@candidate.post("/comment")
def comment() -> Response:
    data = request.get_json()

    form_data: MultiDict = MultiDict(data['formData'])
    candidate_id: int = int(data['candidateId'])

    comment_form: CommentForm = CommentForm(form_data)

    if not comment_form.validate():
        return jsonify({'status': 'error', 'errors': comment_form.errors})

    email: str = comment_form.email.data
    username: str = comment_form.username.data
    text: str = comment_form.text.data

    translated_text: str = translate(text)
    processed_text: str = process_text(translated_text)
    emotion_label: str = get_emotion(processed_text)

    comment_data: DICT_TYPE = {
        'user_email': email,
        'username': username,
        'text': text,
        'emotion': emotion_label,
        'candidate_id': candidate_id
    }

    comment: Comment = Comment(**comment_data)

    db.session.add(comment)
    db.session.commit()

    socketio.emit('rankings_updated', comment_data)

    return jsonify({
        'status': 'success',
        'message': 'Comment saved',
        'commentId': comment.id,
        'emotion': emotion_label
    })

