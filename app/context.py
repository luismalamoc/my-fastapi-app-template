from sqlalchemy.orm import Session
from app.config.database import SessionLocal, engine, Base
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

class AppContext:
    def __init__(self):
        self.engine = engine
        self.SessionLocal = SessionLocal

    def get_user_repository(self, db: Session) -> UserRepository:
        return UserRepository(db)

    def get_user_service(self, db: Session) -> UserService:
        return UserService(self.get_user_repository(db))

    def create_database(self):
        # Create all tables in the database
        Base.metadata.create_all(bind=self.engine)

    def shutdown(self):
        # Close any resources if needed, such as database connections
        pass

app_context = AppContext()
