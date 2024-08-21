import generateNewComment from "../../../static/comment-generator.js";
import {socket, baseURL} from "../../../static/socket.js";

socket.on('rankings_updated', data => {
  const urlElements = window.location.href.split('/');

  const oppenedACandidate = urlElements.includes('candidate')
  const insideDashboard = window.location.href == baseURL

  // updating dashboard
  if (insideDashboard) {
    const candidateCard = document.querySelector(`[data-candidate-id="${data.candidate_id}"]`);

    if (!candidateCard) return;
    const emotion = data.emotion.toLowerCase();

    const rankingElement = candidateCard.querySelector(`.${emotion}`);
    if (!rankingElement) return;

    const rankingScoreElement = rankingElement.firstElementChild;
    if (!rankingScoreElement) return;

    let rankingScore = parseInt(rankingScoreElement.textContent);
    rankingScore++;

    rankingScoreElement.textContent = rankingScore;
  };

  // updating comment section
  if (oppenedACandidate) {
    const comments = document.querySelectorAll('.comment__text');

    let commentFound = false;
    for (let comment of comments) {
      if (comment.textContent == data.text) {
        commentFound = true;
        break;
      }
    }

    if (!commentFound) {
      generateNewComment(
        data?.user_email,
        data?.username,
        data.text,
        new Date()
      );
    }
  }
});

socket.on('connect', () => socket.emit('get_highest_rated_candidate'));

socket.on('highest_rated_candidate', data => {
  if (!data) return;
  const possibleWinnerNameElement = document.getElementById('possible-winner-name');
  const possibleWinnerRatingElement = document.getElementById('possible-winner-rating-positive');

  if (!possibleWinnerNameElement) return;
  if (!possibleWinnerRatingElement) return;

  possibleWinnerNameElement.textContent = data.name
  possibleWinnerRatingElement.textContent = data.positive_ratings
})
