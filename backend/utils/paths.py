from pathlib import Path


KNOWN_FOLDERS = {
    "downloads": Path.home() / "Downloads",
    "desktop": Path.home() / "Desktop",
}


def get_known_folder(folder_name: str) -> Path:
    folder_path = KNOWN_FOLDERS[folder_name].expanduser().resolve()

    if not folder_path.exists() or not folder_path.is_dir():
        raise FileNotFoundError(f"Pasta não encontrada: {folder_path}")

    return folder_path
