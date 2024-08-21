import generateCandidateCard from "./candidate-card-generator.js";

const candidatesElement = document.getElementById('candidates')

window.onload = () => {
  fetch('/candidates')
  .then(response => response.json())
  .then(data => {

    const candidates = data.candidates;

    const NUMBER_OF_CANDIDATES = candidates.length
    const NUMBER_OF_COLUMNS = 3
    const NUMBER_OF_CANDIDATES_PER_COLUMN = Math.floor(NUMBER_OF_CANDIDATES / NUMBER_OF_COLUMNS)

    let imagesInserted = 0;
    let numberOfColumns = 0;

    for (let index = 0; index < NUMBER_OF_CANDIDATES; index++) {
      const candidate = candidates[index];

      if (imagesInserted === NUMBER_OF_CANDIDATES_PER_COLUMN) imagesInserted = 0;

      if (numberOfColumns < NUMBER_OF_COLUMNS && imagesInserted === 0 || imagesInserted === NUMBER_OF_CANDIDATES_PER_COLUMN) {
        candidatesElement.innerHTML += /* html */`<div class='candidates__column'></div>`;
        numberOfColumns++
      }

      candidatesElement.lastElementChild.innerHTML += generateCandidateCard(candidate);
      imagesInserted++;
    }
  })
}

window.onclick = ({target}) => {
  const clickedCard = target.classList.contains('candidate');

  if (clickedCard) {
    const candidateId = target.dataset.candidateId
    window.location.href = `/candidate/${candidateId}`
  }
}
