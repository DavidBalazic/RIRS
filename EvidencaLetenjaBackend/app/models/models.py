from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class LetaloModel(Base):
    __tablename__ = "letalo"
    idLetalo = Column(Integer, primary_key=True, index=True)
    ime_letala = Column(String, nullable=True)
    tip = Column(String, nullable=True)
    registrska_st = Column(String, nullable=True)
    Polet_idPolet = Column(Integer, ForeignKey("polet.idPolet"))

class PilotModel(Base):
    __tablename__ = "pilot"
    idPilot = Column(Integer, primary_key=True, index=True)
    ime = Column(String, nullable=False)
    priimek = Column(String, nullable=False)

class PoletModel(Base):
    __tablename__ = "polet"
    idPolet = Column(Integer, primary_key=True, index=True)
    cas_vzleta = Column(String, nullable=False)  # Stored as text
    cas_pristanka = Column(String, nullable=False)  # Stored as text
    Pilot_idPilot = Column(Integer, ForeignKey("pilot.idPilot"))
