"""
Validadores genéricos de datos de entrada.
"""
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: str) -> bool:
    """Comprueba si una cadena tiene formato de email válido."""
    return bool(EMAIL_REGEX.match(email))


def is_positive_integer(value) -> bool:
    """Comprueba si un valor es un entero positivo."""
    return isinstance(value, int) and value > 0
