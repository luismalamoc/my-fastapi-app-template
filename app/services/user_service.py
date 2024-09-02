from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, db: Session, user: UserCreate) -> User:
        return self.repository.create_user(user)
