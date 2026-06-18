from app.database import Base
from sqlalchemy import String,Text,Enum as sqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from enum import Enum

class UserRole(str,Enum):
    admin="admin"
    student="student"
    teacher="teacher"

class User(Base):
    __tablename__="users"
    id: Mapped[int]=mapped_column(
        primary_key=True
    )
    name:Mapped[str]=mapped_column(String(50),nullable=True)

    email:Mapped[str]=mapped_column(String(50),unique=True)

    password:Mapped[str]=mapped_column(Text)

    role:Mapped[UserRole]=mapped_column(
        sqlEnum(UserRole)
    )       
        
    