/**
 * Generates an HTML card for a candidate, including their image and name.
 * @param {Object} candidate - An object that represents a candidate.
 *
 * @returns an HTML template string that represents a candidate card.
 */
export default function generateCandidateCard(candidate) {

  return /* html */`
    <div class="candidate" data-candidate-id="${candidate.id}">
      <img class="candidate__image" src="${candidate.image ?? ''}" alt="${candidate.name}">
      <div class="candidate__data">
        <p class="candidate__data__name">${candidate.name}</p>
        <p class="candidate__data__text">${candidate.content}</p>
        <div class="candidate__data__rating">
          <div class="candidate__data__rating__child positive">
            <div class="candidate__data__rating__value">${candidate.rating.POSITIVE}</div>
            <div class="candidate__data__rating__name">Positive</div>
          </div>
          <div class="candidate__data__rating__child negative">
            <div class="candidate__data__rating__value">${candidate.rating.NEGATIVE}</div>
            <div class="candidate__data__rating__name">Negative</div>
          </div>
          <div class="candidate__data__rating__child neutral">
            <div class="candidate__data__rating__value">${candidate.rating.NEUTRAL}</div>
            <div class="candidate__data__rating__name">Neutral</div>
          </div>
        </div>
      </div>
    </div>
  `
}