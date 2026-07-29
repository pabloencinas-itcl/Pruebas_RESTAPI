"""
Funciones auxiliares de formateo de texto y números.
"""


def format_currency(amount: float, currency: str = "EUR") -> str:
    """Formatea una cantidad como texto de moneda, p.ej. '1.234,50 EUR'."""
    return (
        f"{amount:,.2f} {currency}".replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def slugify(text: str) -> str:
    """Convierte un texto en un slug apto para URLs (minúsculas, guiones)."""
    return "-".join(text.lower().strip().split())


def truncate(text: str, max_length: int = 100) -> str:
    """Trunca un texto a una longitud máxima, añadiendo puntos suspensivos."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."
