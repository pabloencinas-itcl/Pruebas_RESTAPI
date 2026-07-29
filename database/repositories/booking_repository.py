"""
Repositorio de reservas.

Aísla el acceso a los datos de reservas
para que la capa de servicios no necesite saber cómo se almacenan.
"""

from database.models import Booking
from database.session import get_db


class BookingRepository:
    """Acceso a datos de la entidad Booking."""

    def __init__(self):
        self.db = get_db()

    def get_by_id(self, booking_id: int) -> Booking | None:
        return self.db.bookings.get(booking_id)

    def list_by_user(self, user_id: int) -> list[Booking]:
        return [b for b in self.db.bookings.values() if b.user_id == user_id]

    def add(self, booking: Booking) -> Booking:
        booking.id = self.db._next_booking_id
        self.db.bookings[booking.id] = booking
        self.db._next_booking_id += 1
        return booking

    def update(self, booking: Booking) -> Booking:
        self.db.bookings[booking.id] = booking
        return booking

    def delete(self, booking_id: int) -> None:
        self.db.bookings.pop(booking_id, None)
