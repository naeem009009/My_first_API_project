from app.database import Base
from sqlalchemy import String,Column,Table,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

class Role(Base):
    __tablename__="roles"
    id: Mapped[int]=mapped_column(
        primary_key= True
    )

    name: Mapped[str]=mapped_column(
        String(50)
    )

class Permissions(Base):
    __tablename__="permissions"
    id: Mapped[int]=mapped_column(
        primary_key= True
    )

    name: Mapped[str]=mapped_column(
        String(50)
    )

user_roles=Table(
    "user_roles",Base.metadata,
    Column("user_id",ForeignKey("users.id",ondelete="cascade"),primary_key=True),
    Column("role_id",ForeignKey("roles.id",ondelete="cascade"),primary_key=True),
)

role_permission=Table(
    "role_permission",Base.metadata,
    Column("permission_id",ForeignKey("permission.id",ondelete="cascade"),primary_key=True),
    Column("role_id",ForeignKey("roles.id",ondelete="cascade"),primary_key=True)
)