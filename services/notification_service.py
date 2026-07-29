"""
Servicio de notificaciones a usuarios.

"""

from database.models import Booking, User


def notify_booking_confirmed(user: User, booking: Booking) -> str:
    """Genera (y "envía") el mensaje de confirmación de una reserva."""
    message = (
        f"Hola {user.full_name}, tu reserva #{booking.id} ha sido confirmada. "
        f"Total: {booking.total_price} EUR."
    )
    print(f"[notification] -> {user.email}: {message}")
    return message


def notify_booking_cancelled(user: User, booking: Booking) -> str:
    """Genera (y "envía") el mensaje de cancelación de una reserva."""
    message = f"Hola {user.full_name}, tu reserva #{booking.id} ha sido cancelada."
    print(f"[notification] -> {user.email}: {message}")
    return message
