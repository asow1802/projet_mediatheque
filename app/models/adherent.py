from datetime import date

from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.database import Base


class Adherent(Base):
    __tablename__ = "adherents"
    id_adherent: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    nom: Mapped[str] = mapped_column(String(20), nullable=False)
    prenom: Mapped[str] = mapped_column(String(50), nullable=False)
    adresse: Mapped[str] = mapped_column(String(255), nullable=False)
    date_inscription: Mapped[date] = mapped_column(Date, nullable=False)
    telephone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    emprunts: Mapped[list["Emprunt"]] = relationship(back_populates="adherent")
