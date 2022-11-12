$(document).ready(function () {
	// Check for click events on the navbar burger icon
	$(".navbar-burger").click(function () {
		// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
		$(".navbar-burger").toggleClass("is-active");
		$(".navbar-menu").toggleClass("is-active");
	});
});

// Role changing

function changeValue() {
	if (document.getElementById("role").checked) {
		document.getElementById("roleValue").value = "Doctor";
		document.getElementById("dob").hidden = true;
		document.getElementById("nmc").hidden = false;
		document.getElementById("docField").hidden = false;
	} else {
		document.getElementById("roleValue").value = "Patient";
		document.getElementById("dob").hidden = false;
		document.getElementById("nmc").hidden = true;
		document.getElementById("docField").hidden = true;
	}
}

// Image preview

const imgInput = document.getElementById("file");
const imgEl = document.getElementById("preview");

imgInput.addEventListener("change", () => {
	if (imgInput.files && imgInput.files[0]) {
		imgEl.src = URL.createObjectURL(imgInput.files[0]);
		imgEl.onload = () => {
			URL.revokeObjectURL(imgEl.src);
		};
		document.getElementById("upload").hidden = false;
		document.getElementById("upload").className = "box has-text-centered";
	}
});

// Modal popUp

document.addEventListener("DOMContentLoaded", () => {
	// Functions to open and close a modal
	function openModal($el) {
		$el.classList.add("is-active");
	}

	function closeModal($el) {
		$el.classList.remove("is-active");
	}

	function closeAllModals() {
		(document.querySelectorAll(".modal") || []).forEach(($modal) => {
			closeModal($modal);
		});
	}

	// Add a click event on buttons to open a specific modal
	(document.querySelectorAll(".js-modal-trigger") || []).forEach(($trigger) => {
		const modal = $trigger.dataset.target;
		const $target = document.getElementById(modal);

		$trigger.addEventListener("click", () => {
			openModal($target);
		});
	});

	// Add a click event on various child elements to close the parent modal
	(
		document.querySelectorAll(
			".modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button"
		) || []
	).forEach(($close) => {
		const $target = $close.closest(".modal");

		$close.addEventListener("click", () => {
			closeModal($target);
		});
	});

	// Add a keyboard event to close all modals
	document.addEventListener("keydown", (event) => {
		const e = event || window.event;

		if (e.keyCode === 27) {
			// Escape key
			closeAllModals();
		}
	});
});
