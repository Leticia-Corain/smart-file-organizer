window.smartFileApi = {
  async getStats() {
    const response = await fetch("http://127.0.0.1:8001/stats");

    if (!response.ok) {
      throw new Error("Erro ao buscar estatísticas");
    }

    return await response.json();
  },

  getPreviewDuplicates() {
    return [
      {
        name: "curriculo-final.pdf",
        path: "C:/Users/letic/Downloads/curriculo-final.pdf",
        size: "2.4 MB",
      },
      {
        name: "curriculo-final.pdf",
        path: "C:/Users/letic/Desktop/curriculo-final.pdf",
        size: "2.4 MB",
      },
      {
        name: "relatorio-vendas.xlsx",
        path: "C:/Users/letic/Downloads/relatorio-vendas.xlsx",
        size: "818 KB",
      },
    ];
  },
};