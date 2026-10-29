from datetime import date
from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Emprunt(Base):
    __tablename__ = "emprunts"
    id_emprunt: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    date_debut: Mapped[date] = mapped_column(Date, nullable=False)
    date_retour_prevue: Mapped[date] = mapped_column(Date , nullable=False)
    date_retour_effective: Mapped[date|None] = mapped_column(Date, nullable=True)
    id_adherent: Mapped[int] = mapped_column(Integer,ForeignKey("adherents.id_adherent"), nullable=False)
    adherent: Mapped["Adherent"] = relationship(back_populates="emprunts")
    id_ouvrage: Mapped[int] = mapped_column(Integer,ForeignKey("ouvrages.id_ouvrage"), nullable=False)
    ouvrage: Mapped["Ouvrage"] = relationship(back_populates="emprunts")