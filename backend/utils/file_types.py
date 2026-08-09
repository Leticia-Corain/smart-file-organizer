from pathlib import Path

CATEGORY_BY_EXTENSION = {
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".gif": "Imagens",
    ".bmp": "Imagens",
    ".webp": "Imagens",
    ".svg": "Imagens",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".pdf": "PDFs",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".ppt": "Documentos",
    ".pptx": "Documentos",
    ".xls": "Planilhas",
    ".xlsx": "Planilhas",
    ".csv": "Planilhas",
    ".zip": "Arquivos Compactados",
    ".rar": "Arquivos Compactados",
    ".7z": "Arquivos Compactados",
    ".tar": "Arquivos Compactados",
    ".gz": "Arquivos Compactados",
    ".mp3": "Musicas",
    ".wav": "Musicas",
    ".flac": "Musicas",
    ".aac": "Musicas",
    ".exe": "Executaveis",
    ".msi": "Executaveis",
}


def get_category(file_path: Path) -> str:
    return CATEGORY_BY_EXTENSION.get(file_path.suffix.lower(), "Outros")
