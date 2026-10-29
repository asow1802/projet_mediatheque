from datetime import date
from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.database import Base


class Auteur(Base):
    __tablename__ = "auteurs"
    id_auteur: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    nom: Mapped[str] = mapped_column(String(20), nullable=False)
    prenom: Mapped[str] = mapped_column(String(50), nullable=False)
    date_naissance: Mapped[date] = mapped_column(Date, nullable=False)
    lieu_naissance: Mapped[str] = mapped_column(String(100), nullable=False)
    ouvrages: Mapped[list["Ouvrage"]] = relationship(back_populates="auteur")