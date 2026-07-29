"""
Configuración global de la aplicación.

Centraliza los parámetros que dependen del entorno (dev, staging, prod).
"""
import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "TravelHub"
    environment: str = os.getenv("ENVIRONMENT", "development")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///travelhub.db")
    max_bookings_per_user: int = 5


_settings = Settings()


def get_settings() -> Settings:
    """Devuelve la configuración de la aplicación (singleton simple)."""
    return _settings
