"""Routes for last-operation statistics."""

from fastapi import APIRouter, HTTPException

from backend.services.stats_service import get_last_stats

router = APIRouter()


@router.get("/stats")
def get_stats_route() -> dict:
    """
    Retorna as estatísticas da última execução.
    """

    try:
        return get_last_stats()

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível obter as estatísticas."
        ) from exc