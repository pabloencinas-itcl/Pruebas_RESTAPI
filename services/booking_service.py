"""
Lógica de negocio relacionada con la creación y gestión de reservas.

Orquesta los repositorios (database) y aplica las reglas de negocio,
sin conocer detalles de cómo se exponen las rutas HTTP (api).
"""
from core.config import get_settings
from core.exceptions import (
    BookingNotFoundError,
    InvalidBookingDatesError,
    BookingLimitExceededError,
)
from database.repositories.booking_repository import BookingRepository
from database.repositories.user_repository import UserRepository
from database.session import get_db
from database.models import Booking, BookingStatus
from services.pricing_service import calculate_total_price
from utils.date_helpers import is_valid_date_range


class BookingService:
    """Casos de uso relacionados con reservas."""

    def __init__(self):
        self.booking_repo = BookingRepository()
        self.user_repo = UserRepository()
        self.settings = get_settings()

    def create_booking(self, user_id: int, destination_id: int,
                        check_in, check_out, passengers: int = 1) -> Booking:
        """Crea una nueva reserva para un usuario, validando reglas de negocio."""
        if not is_valid_date_range(check_in, check_out):
            raise InvalidBookingDatesError("Rango de fechas inválido")

        existing = self.booking_repo.list_by_user(user_id)
        active = [b for b in existing if b.status != BookingStatus.CANCELLED]
        if len(active) >= self.settings.max_bookings_per_user:
            raise BookingLimitExceededError(
                f"El usuario {user_id} ya tiene el máximo de reservas activas"
            )

        destination = get_db().destinations[destination_id]
        total_price = calculate_total_price(destination, check_in, check_out, passengers)

        booking = Booking(
            id=0,
            user_id=user_id,
            destination_id=destination_id,
            check_in=check_in,
            check_out=check_out,
            status=BookingStatus.PENDING,
            total_price=total_price,
            passengers=passengers,
        )
        return self.booking_repo.add(booking)

    def cancel_booking(self, booking_id: int) -> Booking:
        """Cancela una reserva existente."""
        booking = self.booking_repo.get_by_id(booking_id)
        if booking is None:
            raise BookingNotFoundError(f"Reserva {booking_id} no encontrada")
        booking.status = BookingStatus.CANCELLED
        return self.booking_repo.update(booking)

    def get_user_bookings(self, user_id: int) -> list[Booking]:
        """Devuelve todas las reservas de un usuario."""
        return self.booking_repo.list_by_user(user_id)
