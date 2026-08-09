document.addEventListener("DOMContentLoaded", async () => {
  const sidebar = document.querySelector("[data-sidebar]");
  const sidebarToggle = document.querySelector("[data-sidebar-toggle]");
  const toast = document.querySelector("[data-toast]");
  const loading = document.querySelector("[data-loading]");
  const loadingText = document.querySelector("[data-loading-text]");
  const actionButtons = document.querySelectorAll("[data-action]");
  const navItems = document.querySelectorAll("[data-section-trigger]");
  const sections = document.querySelectorAll("[data-section]");
  const duplicateList = document.querySelector("[data-duplicate-list]");

  const statElements = {
    organized: document.querySelectorAll(
      '[data-stat="organized"], [data-stat-panel="organized"]'
    ),
    folders: document.querySelectorAll(
      '[data-stat="folders"], [data-stat-panel="folders"]'
    ),
    duplicates: document.querySelectorAll(
      '[data-stat="duplicates"], [data-stat-panel="duplicates"]'
    ),
  };

  let isCollapsed = false;

  async function loadStats() {
    try {
      const response = await fetch("http://127.0.0.1:8001/stats");
      const stats = await response.json();

      window.smartFileUi.updateStats(statElements, {
        organized: stats.organized_files,
        folders: stats.created_folders,
        duplicates: stats.duplicates_found,
      });
    } catch (error) {
      console.error("Erro ao carregar estatísticas:", error);
    }
  }

  const activateSection = (sectionName) => {
    window.smartFileUi.setActiveSection(sections, sectionName);
    window.smartFileUi.setActiveNav(navItems, sectionName);
  };

  activateSection("inicio");

  await loadStats();

  sidebarToggle.addEventListener("click", () => {
    isCollapsed = !isCollapsed;

    window.smartFileUi.setSidebarCollapsed(
      sidebar,
      isCollapsed
    );

    sidebarToggle.setAttribute(
      "aria-label",
      isCollapsed
        ? "Expandir sidebar"
        : "Recolher sidebar"
    );
  });

  navItems.forEach((item) => {
    item.addEventListener("click", () => {
      activateSection(item.dataset.sectionTrigger);
    });
  });

  actionButtons.forEach((button) => {
    button.addEventListener("click", async () => {
      const action = button.dataset.action;

      const actionMap = {
        downloads: {
          endpoint: "downloads",
          section: "downloads",
          loading: "Organizando Downloads...",
        },

        desktop: {
          endpoint: "desktop",
          section: "desktop",
          loading: "Organizando Desktop...",
        },
      };

      const selectedAction = actionMap[action];

      if (!selectedAction) return;

      activateSection(selectedAction.section);

      window.smartFileUi.setToast(toast, false);

      window.smartFileUi.setLoading(
        loading,
        loadingText,
        true,
        selectedAction.loading
      );

      try {
        const response = await fetch(
          `http://127.0.0.1:8001/${selectedAction.endpoint}`,
          {
            method: "POST",
          }
        );

        const data = await response.json();

        await loadStats();

        window.smartFileUi.setToast(
          toast,
          true,
          "Sucesso",
          data.message
        );
      } catch (error) {
        console.error(error);

        window.smartFileUi.setToast(
          toast,
          true,
          "Erro",
          "Não foi possível executar a operação."
        );
      }

      window.smartFileUi.setLoading(
        loading,
        loadingText,
        false
      );
    });
  });
});