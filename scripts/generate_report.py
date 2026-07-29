"""
Script de mantenimiento: genera un informe de texto con las reservas
confirmadas del sistema.

Es una herramienta administrativa independiente, pensada para ejecutarse
de forma manual (p.ej. desde un cron).

Uso:
    python scripts/generate_report.py
"""

from database.models import BookingStatus
from database.session import get_db


def generate_confirmed_bookings_report() -> str:
    db = get_db()
    confirmed = [b for b in db.bookings.values() if b.status == BookingStatus.CONFIRMED]

    lines = [f"Informe de reservas confirmadas ({len(confirmed)})", "-" * 40]
    for booking in confirmed:
        destination = db.destinations[booking.destination_id]
        lines.append(
            f"Reserva #{booking.id} - {destination.city} - {booking.total_price} EUR"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    print(generate_confirmed_bookings_report())
