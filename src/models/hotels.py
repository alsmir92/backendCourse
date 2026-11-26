from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database import Base


class HotelsOrm(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True) # уникальный столбец
    # по определению
    title: Mapped[str] = mapped_column(String(100)) # Не больше 100 символов
    # в названии
    location: Mapped[str]