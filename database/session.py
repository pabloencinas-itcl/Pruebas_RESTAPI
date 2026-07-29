"""
Gestión de la conexión/sesión a la base de datos.

Se simula con estructuras en memoria en lugar
de una base de datos real, pero mantiene la interfaz que tendría una
sesión de SQLAlchemy para que el resto de capas no necesiten cambiar
si se conecta una base de datos real más adelante.
"""

from datetime import date

from database.models import Booking, BookingStatus, Destination, User


class InMemoryDatabase:
    """Simula el almacenamiento persistente de la aplicación."""

    def __init__(self):
        self.users = {
            1: User(1, "Ana Torres", "ana@example.com", "hash1"),
            2: User(2, "Luis Marín", "luis@example.com", "hash2"),
        }
        self.destinations = {
            1: Destination(1, "Lisboa", "Portugal", 180.0),
            2: Destination(2, "Kioto", "Japón", 950.0),
            3: Destination(3, "Cusco", "Perú", 620.0),
        }
        self.bookings = {
            1: Booking(
                1,
                1,
                1,
                date(2026, 3, 10),
                date(2026, 3, 15),
                BookingStatus.CONFIRMED,
                900.0,
                2,
            ),
        }
        self._next_booking_id = 2


_db = InMemoryDatabase()


def get_db() -> InMemoryDatabase:
    """Devuelve la instancia de base de datos (simulada) de la aplicación."""
    return _db
