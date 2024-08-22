/**
 * Replace the default querySelector
 */
export const element = (className) => document.querySelector(className);
export const elements = (className) => document.querySelectorAll(className);

/**
 * Adds a character counter to an input field and updates a corresponding counter element.
 * @param {HTMLElement} inputElement - The input field.
 * @param {HTMLElement} counterElement - The counter element.
 * @param {number|null} restriction - The character limit (null for no limit).
 */
export const counter = (inputElement, counterElement, restriction = null) => {
  const updateCounter = () => {
    const length = inputElement.value.length;
    counterElement.children[0].textContent = length;
  };

  inputElement.oninput = () => {
    if (restriction === null || inputElement.value.length <= restriction) {
      updateCounter();
    }
  };

  window.onload = () => updateCounter();
};

/**
 * Toggles the visibility of eye icons and input field type in a form.
 * @param {HTMLElement} eyesContainer - The container for eye icons.
 * @param {HTMLInputElement} input - The input field.
 * @param {HTMLElement} eye - The open eye icon.
 * @param {HTMLElement} eyeSlash - The closed eye icon.
 */
export const eyeToggle = (eyesContainer, input, eye, eyeSlash) => {
  eyesContainer.onclick = () => {
    const isText = input.type === "text";
    input.type = isText ? "password" : "text";
    eye.style.display = isText ? "none" : "block";
    eyeSlash.style.display = isText ? "block" : "none";
  };
};

/**
 * Creates a toast notification element and appends it to the flashes container.
 * @param {string} message - The message content of the notification.
 */
export function makeToastNotification(message) {
  const flashes = element(".flashes");

  if (message === "") {
    return;
  }

  const newToast = document.createElement("li");
  newToast.classList.add("message");
  newToast.textContent = message;

  flashes.append(newToast);
  newToast.classList.toggle("active");

  setTimeout(() => {
    newToast.classList.remove("active");
    setTimeout(() => newToast.remove(), 500);
  }, 2000);
}

/**
 * Automatically resizes a textarea element to fit its content.
 */
export const autoResize = (element) => {
  element.style.height = "auto";
  element.style.height = element.scrollHeight + "px";
};
