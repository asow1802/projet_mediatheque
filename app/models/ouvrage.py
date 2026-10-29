from datetime import date
from sqlalchemy import String, Integer, Date
from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Ouvrage(Base):
    __tablename__ = "ouvrages"
    id_ouvrage: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    isbn: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    date_publication: Mapped[date] = mapped_column(Date, nullable=False)
    titre: Mapped[str] = mapped_column(String(100), nullable=False)
    nombre_de_pages: Mapped[int] = mapped_column(Integer, nullable=False)
    editeur: Mapped[str] = mapped_column(String(100), nullable=False)
    id_auteur: Mapped[int] = mapped_column(Integer,ForeignKey("auteurs.id_auteur"), nullable=False)
    auteur: Mapped["Auteur"] = relationship(back_populates="ouvrages")
    emprunts: Mapped[list["Emprunt"]] = relationship(back_populates="ouvrage")
    