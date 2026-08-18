from fastapi import APIRouter

from backend.services.duplicate_service import find_duplicates
from backend.utils.paths import get_known_folder

router = APIRouter()


@router.get("/duplicates")
def get_duplicates():

    duplicates = find_duplicates(
        get_known_folder("downloads")
    )

    return {
        "duplicates": duplicates
    }