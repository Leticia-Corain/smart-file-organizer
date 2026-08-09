window.smartFileUi = {
  setSidebarCollapsed(sidebarElement, collapsed) {
    sidebarElement.classList.toggle("sidebar--collapsed", collapsed);
  },

  setLoading(loadingElement, loadingTextElement, isVisible, message) {
    loadingElement.hidden = !isVisible;

    if (message) {
      loadingTextElement.textContent = message;
    }
  },

  setToast(toastElement, visible, title, message) {
    toastElement.classList.toggle("toast--visible", visible);

    if (title) {
      toastElement.querySelector("[data-toast-title]").textContent = title;
    }

    if (message) {
      toastElement.querySelector("[data-toast-message]").textContent = message;
    }
  },

  updateStats(statElements, stats) {
    Object.entries(statElements).forEach(([key, elements]) => {
      elements.forEach((element) => {
        element.textContent = stats[key];
      });
    });
  },

  setActiveSection(sectionElements, targetSection) {
    sectionElements.forEach((section) => {
      section.classList.toggle(
        "app-section--active",
        section.dataset.section === targetSection,
      );
    });
  },

  setActiveNav(navItems, targetSection) {
    navItems.forEach((item) => {
      item.classList.toggle(
        "nav-item--active",
        item.dataset.sectionTrigger === targetSection,
      );
    });
  },

  renderDuplicates(container, duplicates) {
    container.innerHTML = duplicates
      .map(
        (duplicate) => `
          <article class="duplicate-row">
            <span class="duplicate-name">${duplicate.name}</span>
            <span class="duplicate-path">${duplicate.path}</span>
            <span class="duplicate-size">${duplicate.size}</span>
          </article>
        `,
      )
      .join("");
  },
};
