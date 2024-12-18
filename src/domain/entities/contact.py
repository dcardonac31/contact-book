import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from infrastructure.database.db import Base

class Contact(Base):
    __tablename__ = 'contacts'

    # Identificador único (UUID)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    # Atributos del contacto
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)  # Opcional
    phone_number = Column(String, nullable=True)  # Opcional
    photo_url = Column(String, nullable=True)  # URL opcional para la foto del contacto

    # Relación con la tabla User (si el contacto pertenece a un usuario)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="contacts")