"""
Punto de entrada de la aplicación TravelHub.

Levanta la API y registra las rutas disponibles.
"""
from core.config import get_settings
from api.routes import bookings, destinations, users


def create_app():
    """Crea y configura la aplicación (simulado, sin framework real)."""
    settings = get_settings()
    routes = {
        "bookings": bookings.router,
        "destinations": destinations.router,
        "users": users.router,
    }
    print(f"Starting {settings.app_name} in {settings.environment} mode")
    print(f"Registered route groups: {list(routes.keys())}")
    return routes


if __name__ == "__main__":
    create_app()
