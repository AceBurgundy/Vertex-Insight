/**
 * The function generates a new comment with the provided email, text, and date posted.
 *
 * @param {string} email - the email address of the person who posted the comment.
 * @param {string} text - the content of the comment that will be displayed in the template.
 * @param {Date} datePosted - The date when the comment was posted.
 * @throws {Error} when one of the arguments is null.
 * @returns {string} an HTML template string that represents a comment.
 */
export default function generateNewComment(email, username, text, dateTimePosted) {
  if (!email) throw new Error('Missing email for creating comment');
  if (!text) throw new Error('Missing text for creating comment');
  if (!dateTimePosted) throw new Error('Missing date posted for creating comment');

  const formattedDate = new Date(dateTimePosted).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  });

  const emailTemplate = email ? `<p class="comment__top__email">${email}</p>` : ''
  const usernameTemplate = username ? `<p class="comment__top__username">${username}</p>` : ''

  const commentTemplate = /* html */`
    <div class="comment" id="new-comment">
      <div class="comment__top">
        ${emailTemplate}
        ${usernameTemplate}
        <p class="comment__top__datetime">${formattedDate}</p>
      </div>
      <p class="comment__text">${text}</p>
    </div>
  `;

  const commentSection = document.getElementById('candidate-comments-list');
  if (!commentSection) throw new Error('Comment section is missing');

  commentSection.innerHTML += commentTemplate;
}