/**
 * Creates a toast notification queryElement and appends it to the flashes container.
 * @param {string} message - The message content of the notification.
 */
export default function makeToastNotification(message) {
	const toasts = document.getElementById("toasts");

	if (message === '') return;

	const newToast = document.createElement("li");
	newToast.classList.add("toast");
	newToast.textContent = message;

	toasts.append(newToast);
	newToast.classList.toggle("active");

	setTimeout(() => {
		newToast.classList.remove("active");
		setTimeout(() => {
			newToast.remove();
		}, 250);
	}, 2000);
}