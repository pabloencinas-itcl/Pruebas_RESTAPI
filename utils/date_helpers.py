"""
Funciones auxiliares para trabajar con fechas.

"""

from datetime import date, timedelta


def is_valid_date_range(check_in: date, check_out: date) -> bool:
    """Comprueba que check_out sea posterior a check_in y no sea en el pasado."""
    if check_out <= check_in:
        return False
    if check_in < date.today():
        return False
    return True


def days_between(start: date, end: date) -> int:
    """Devuelve el número de días entre dos fechas."""
    return (end - start).days


def add_days(base_date: date, days: int) -> date:
    """Suma un número de días a una fecha dada."""
    return base_date + timedelta(days=days)
