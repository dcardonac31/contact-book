from sqlalchemy.orm import Session
from infrastructure.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from infrastructure.repositories.sqlalchemy_contact_repository import SQLAlchemyContactRepository
from domain.services.user_service import UserService
from domain.services.contact_service import ContactService

class Dependencies:
    @staticmethod
    def get_user_service(db: Session):
        user_repository = SQLAlchemyUserRepository(db)
        return UserService(user_repository)
    
    @staticmethod
    def get_contact_service(db: Session):
        contact_repository = SQLAlchemyContactRepository(db)
        return ContactService(contact_repository)