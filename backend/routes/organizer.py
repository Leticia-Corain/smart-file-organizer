from fastapi import APIRouter, HTTPException

from backend.services.organizer_service import (
    organize_desktop,
    organize_downloads,
)

router = APIRouter()


@router.post("/downloads")
def organize_downloads_route() -> dict:
    try:
        return organize_downloads()

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        ) from exc

    except Exception as exc:
        print(f"ERRO DOWNLOADS: {exc}")

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        ) from exc


@router.post("/desktop")
def organize_desktop_route() -> dict:
    try:
        return organize_desktop()

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        ) from exc

    except Exception as exc:
        print(f"ERRO DESKTOP: {exc}")

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        ) from exc