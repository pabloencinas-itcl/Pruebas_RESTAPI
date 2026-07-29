"""
Esquemas de entrada/salida relacionados con usuarios.
"""
from dataclasses import dataclass


@dataclass
class UserCreateRequest:
    full_name: str
    email: str
    password: str


@dataclass
class UserResponse:
    id: int
    full_name: str
    email: str
