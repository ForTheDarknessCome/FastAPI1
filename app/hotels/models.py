from sqlalchemy import ForeignKey, text, Text, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.database import Base, str_uniq, int_pk, str_null_true
from datetime import date


class Hotel(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]


class Room(Base):
    id: Mapped[int_pk]
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[str]