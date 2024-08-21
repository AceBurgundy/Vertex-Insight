import generateNewComment from "../../../static/comment-generator.js";
import makeToastNotification from "../../../static/toast.js";
import {socket} from "../../../static/socket.js";

const commentForm = document.getElementById('comment-form');

commentForm.onsubmit = async event => {
    event.preventDefault();

    const formData = new FormData(commentForm);
    const rootElement = event.target.parentElement;

    let formDataValues = Array.from(new FormData(commentForm).values());
    // formDataValues[0] is csrf token

    generateNewComment(formDataValues[1], formDataValues[2], formDataValues[3], new Date());
    makeToastNotification('Comment added')

    const candidateId = rootElement.parentElement.dataset.candidateId;
    if (!candidateId) throw new Error('Missing candidate id');

    let form = {};
    formData.forEach((value, key) => form[key] = value);

    let response = null;

    try {
      response = await fetch(commentForm.dataset.action, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          formData: form,
          candidateId: candidateId
        })
      });
    } catch (error) {
      console.error(error);
    }

    if (!response) return;

    const data = await response.json();
    if (data.message) makeToastNotification(data.message);

    const addedComment = document.getElementById('new-comment');
    if (!addedComment) throw new Error('Comment not added');
    if (data.status === 'error') console.log(data.errors);

    addedComment.setAttribute('id', data.commentId);

    const emotion = data.emotion
    const candidateEmotionElement = document.querySelector(`.${emotion.toLowerCase()}`)
    if (!candidateEmotionElement) return;

    const emotionRatingElement = candidateEmotionElement.firstElementChild;
    if (!emotionRatingElement) return;

    let ratingScore = parseInt(emotionRatingElement.textContent);
    ratingScore++

    emotionRatingElement.innerHTML = ratingScore;
    socket.emit('get_highest_rated_candidate')
};
