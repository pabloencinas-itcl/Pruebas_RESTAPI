"""
Utilidades de seguridad: hash de contraseñas y tokens de sesión simples.

"""

import hashlib
import secrets


def hash_password(plain_password: str) -> str:
    """Genera un hash simple de una contraseña en texto plano."""
    salt = secrets.token_hex(8)
    digest = hashlib.sha256((salt + plain_password).encode()).hexdigest()
    return f"{salt}${digest}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Comprueba que una contraseña en texto plano coincide con su hash."""
    salt, digest = hashed_password.split("$")
    return hashlib.sha256((salt + plain_password).encode()).hexdigest() == digest


def generate_session_token() -> str:
    """Genera un token de sesión aleatorio."""
    return secrets.token_urlsafe(32)
