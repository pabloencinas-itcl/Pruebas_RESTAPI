"""
Rutas HTTP relacionadas con destinos disponibles.
"""
from database.session import get_db

router = "destinations_router"


def list_destinations_endpoint() -> list[dict]:
    """GET /destinations — lista todos los destinos disponibles."""
    db = get_db()
    return [
        {"id": d.id, "city": d.city, "country": d.country, "base_price": d.base_price}
        for d in db.destinations.values()
    ]


def get_destination_endpoint(destination_id: int) -> dict:
    """GET /destinations/{destination_id} — detalle de un destino."""
    db = get_db()
    destination = db.destinations.get(destination_id)
    if destination is None:
        return {"error": "Destino no encontrado"}
    return {
        "id": destination.id,
        "city": destination.city,
        "country": destination.country,
        "base_price": destination.base_price,
    }
