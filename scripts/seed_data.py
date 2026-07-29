"""
Script de mantenimiento: rellena la base de datos con datos de ejemplo.

Uso:
    python scripts/seed_data.py
"""

from database.models import Destination
from database.session import get_db


def seed_extra_destinations():
    db = get_db()
    extra = [
        Destination(4, "Marrakech", "Marruecos", 340.0),
        Destination(5, "Reikiavik", "Islandia", 780.0),
    ]
    for destination in extra:
        db.destinations[destination.id] = destination
    print(f"Insertados {len(extra)} destinos adicionales.")


if __name__ == "__main__":
    seed_extra_destinations()
