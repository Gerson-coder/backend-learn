const searchInput = document.querySelector("[data-search]");
const levelCards = [...document.querySelectorAll(".level")];
const progressText = document.querySelector("[data-progress-text]");
const progressBar = document.querySelector("[data-progress-bar]");
const resetButton = document.querySelector("[data-reset]");
const STORAGE_KEY = "python-backend-roadmap-progress";

function loadProgress() {
	try {
		return JSON.parse(localStorage.getItem(STORAGE_KEY)) ?? {};
	} catch {
		return {};
	}
}

function saveProgress(progress) {
	localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
}

function updateProgress() {
	const checkboxes = [...document.querySelectorAll(".module-check")];
	const completed = checkboxes.filter((checkbox) => checkbox.checked).length;
	const total = checkboxes.length;
	const percentage = total === 0 ? 0 : Math.round((completed / total) * 100);

	progressText.textContent = `${completed}/${total} módulos completados · ${percentage}%`;
	progressBar.style.width = `${percentage}%`;
}

function setupModuleProgress() {
	const progress = loadProgress();

	document.querySelectorAll(".module").forEach((module, index) => {
		const title =
			module.querySelector("h4")?.textContent?.trim() ?? `Módulo ${index + 1}`;
		const id = `module-${index}`;
		const label = document.createElement("label");
		label.className = "module-progress";

		const checkbox = document.createElement("input");
		checkbox.className = "module-check";
		checkbox.type = "checkbox";
		checkbox.dataset.moduleId = id;

		const labelText = document.createElement("span");
		labelText.textContent = "Marcar completado";

		label.append(checkbox, labelText);
		module.appendChild(label);

		checkbox.checked = Boolean(progress[id]);
		module.classList.toggle("is-complete", checkbox.checked);
		checkbox.setAttribute("aria-label", `Marcar como completado: ${title}`);

		checkbox.addEventListener("change", () => {
			progress[id] = checkbox.checked;
			if (!checkbox.checked) delete progress[id];
			saveProgress(progress);
			module.classList.toggle("is-complete", checkbox.checked);
			updateProgress();
		});
	});

	updateProgress();
}

function setupSearch() {
	searchInput?.addEventListener("input", () => {
		const query = searchInput.value.trim().toLowerCase();

		levelCards.forEach((level) => {
			const matches = level.textContent.toLowerCase().includes(query);
			level.hidden = query.length > 0 && !matches;
		});
	});
}

function setupReset() {
	resetButton?.addEventListener("click", () => {
		localStorage.removeItem(STORAGE_KEY);
		document.querySelectorAll(".module-check").forEach((checkbox) => {
			checkbox.checked = false;
			checkbox.closest(".module")?.classList.remove("is-complete");
		});
		updateProgress();
	});
}

setupModuleProgress();
setupSearch();
setupReset();
