"""
Rutas HTTP relacionadas con usuarios.
"""
from core.security import hash_password
from utils.validators import is_valid_email
from schemas.user import UserCreateRequest, UserResponse
from api.dependencies import get_user_repository
from database.models import User

router = "users_router"


def create_user_endpoint(request: UserCreateRequest):
    """POST /users — registra un nuevo usuario."""
    if not is_valid_email(request.email):
        return {"error": "Email no válido"}

    repo = get_user_repository()
    user = User(
        id=0,
        full_name=request.full_name,
        email=request.email,
        hashed_password=hash_password(request.password),
    )
    created = repo.add(user)
    return UserResponse(id=created.id, full_name=created.full_name, email=created.email)


def get_user_endpoint(user_id: int):
    """GET /users/{user_id} — obtiene el detalle de un usuario."""
    repo = get_user_repository()
    user = repo.get_by_id(user_id)
    if user is None:
        return {"error": "Usuario no encontrado"}
    return UserResponse(id=user.id, full_name=user.full_name, email=user.email)
