"""
Excepciones propias del dominio de TravelHub.

Se usan en las distintas capas para señalar errores de negocio, en lugar
de dejar que se propaguen excepciones genéricas de Python.
"""


class TravelHubError(Exception):
    """Excepción base para todos los errores propios de la aplicación."""


class BookingNotFoundError(TravelHubError):
    """Se lanza cuando no se encuentra una reserva solicitada."""


class InvalidBookingDatesError(TravelHubError):
    """Se lanza cuando las fechas de una reserva no son válidas."""


class UserNotFoundError(TravelHubError):
    """Se lanza cuando no se encuentra un usuario solicitado."""


class BookingLimitExceededError(TravelHubError):
    """Se lanza cuando un usuario supera el número máximo de reservas activas."""
