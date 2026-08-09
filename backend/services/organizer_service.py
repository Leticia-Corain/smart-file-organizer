import shutil
from pathlib import Path

from backend.services.stats_service import set_last_stats
from backend.utils.file_types import get_category
from backend.utils.paths import get_known_folder


def organize_downloads() -> dict:
    return _organize_known_folder("downloads", "Downloads")



def organize_desktop() -> dict:
    return _organize_known_folder("desktop", "Desktop")



def _organize_known_folder(folder_key: str, folder_label: str) -> dict:
    source_path = get_known_folder(folder_key)
    created_folders = 0
    organized_files = 0

    for item in source_path.iterdir():
        if item.is_dir() or item.name.startswith("."):
            continue

        category = get_category(item)
        destination_folder = source_path / category

        if not destination_folder.exists():
            destination_folder.mkdir(parents=True, exist_ok=True)
            created_folders += 1

        destination_path = _build_destination_path(destination_folder, item.name)
        shutil.move(str(item), str(destination_path))
        organized_files += 1

    set_last_stats(
        last_operation=folder_key,
        organized_files=organized_files,
        created_folders=created_folders,
        duplicates_found=0,
    )

    return {
        "message": f"Organização de {folder_label} concluída.",
        "source": str(source_path),
        "organized_files": organized_files,
        "created_folders": created_folders,
    }



def _build_destination_path(destination_folder: Path, file_name: str) -> Path:
    destination_path = destination_folder / file_name

    if not destination_path.exists():
        return destination_path

    stem = destination_path.stem
    suffix = destination_path.suffix
    counter = 1

    while True:
        candidate = destination_folder / f"{stem} ({counter}){suffix}"

        if not candidate.exists():
            return candidate

        counter += 1
