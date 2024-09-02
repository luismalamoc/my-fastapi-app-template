from app.models.user import User
from app.schemas.user_schema import UserRead

class UserMapper:
    @staticmethod
    def to_read_model(user: User) -> UserRead:
        return UserRead(id=user.id, name=user.name, email=user.email)
