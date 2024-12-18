# Centraliza todas las entidades en un único archivo
from domain.entities.user import User
from domain.entities.contact import Contact

# Exporta para registrar en Base
__all__ = ["User", "Contact"]
