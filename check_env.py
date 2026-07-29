"""
Script suelto de un desarrollador para comprobar rápidamente variables
de entorno antes de arrancar el proyecto en local.

No sigue ninguna convención del proyecto, no está importado por ningún
otro módulo y probablemente debería eliminarse o moverse a scripts/.
"""
import os

REQUIRED_VARS = ["DATABASE_URL", "ENVIRONMENT"]

for var in REQUIRED_VARS:
    value = os.getenv(var)
    print(f"{var}: {'OK' if value else 'NO DEFINIDA'}")
