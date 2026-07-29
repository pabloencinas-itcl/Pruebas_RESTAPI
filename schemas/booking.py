"""
Esquemas de entrada/salida relacionados con reservas.

Definen la forma de los datos que la API espera recibir y devolver,
separada de los modelos internos de base de datos.
"""
from dataclasses import dataclass
from datetime import date


@dataclass
class BookingCreateRequest:
    user_id: int
    destination_id: int
    check_in: date
    check_out: date
    passengers: int = 1


@dataclass
class BookingResponse:
    id: int
    destination_city: str
    check_in: date
    check_out: date
    total_price: float
    status: str
