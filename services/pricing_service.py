"""
Lógica de negocio relacionada con el cálculo de precios.
"""
from datetime import date
from database.models import Destination


def calculate_nights(check_in: date, check_out: date) -> int:
    """Calcula el número de noches entre dos fechas."""
    return (check_out - check_in).days


def calculate_total_price(destination: Destination, check_in: date,
                           check_out: date, passengers: int) -> float:
    """Calcula el precio total de una reserva.

    Aplica el precio base del destino por noche, por pasajero, y un
    descuento por estancias largas.
    """
    nights = calculate_nights(check_in, check_out)
    if nights <= 0:
        raise ValueError("check_out debe ser posterior a check_in")

    subtotal = destination.base_price * nights * passengers
    return apply_long_stay_discount(subtotal, nights)


def apply_long_stay_discount(subtotal: float, nights: int) -> float:
    """Aplica un descuento del 10% si la estancia es de 7 noches o más."""
    if nights >= 7:
        return round(subtotal * 0.9, 2)
    return round(subtotal, 2)
