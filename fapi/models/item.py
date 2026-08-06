from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Item(Base):
    __tablename__ = "items"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    description: Mapped[str|None] = mapped_column(String(255), nullable=True)

    price: Mapped[int] = mapped_column(server_default=text("0"), nullable=False)