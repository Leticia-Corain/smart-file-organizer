from copy import deepcopy

_LAST_STATS = {
    "last_operation": None,
    "organized_files": 0,
    "created_folders": 0,
    "duplicates_found": 0,
}


def set_last_stats(*, last_operation: str, organized_files: int, created_folders: int, duplicates_found: int) -> None:
    _LAST_STATS.update(
        {
            "last_operation": last_operation,
            "organized_files": organized_files,
            "created_folders": created_folders,
            "duplicates_found": duplicates_found,
        }
    )


def get_last_stats() -> dict:
    return deepcopy(_LAST_STATS)
