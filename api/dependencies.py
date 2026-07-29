"""
Dependencias compartidas por las rutas de la API.

Proporciona instancias listas para usar de los servicios, de forma
similar a como se haría con Depends() en FastAPI real.
"""
from services.booking_service import BookingService
from database.repositories.user_repository import UserRepository


def get_booking_service() -> BookingService:
    """Devuelve una instancia del servicio de reservas."""
    return BookingService()


def get_user_repository() -> UserRepository:
    """Devuelve una instancia del repositorio de usuarios."""
    return UserRepository()
