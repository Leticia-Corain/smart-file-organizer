"""Routes for duplicate file lookup."""

from pathlib import Path

from fastapi import APIRouter

from services.duplicate_service import find_duplicates

router = APIRouter()


@router.get("/duplicates")
def get_duplicates():

    duplicates = find_duplicates(Path.home())

    return {
        "duplicates": duplicates
    }