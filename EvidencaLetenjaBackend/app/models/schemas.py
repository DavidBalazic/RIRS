from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Pydantic schema for Letalo
class LetaloSchema(BaseModel):
    idLetalo: Optional[int] = None
    ime_letala: Optional[str] = None
    tip: Optional[str] = None
    registrska_st: Optional[str] = None
    Polet_idPolet: Optional[int] = None

    model_config = {
        "from_attributes": True 
    }

# Pydantic schema for Pilot
class PilotSchema(BaseModel):
    idPilot: Optional[int] = None
    ime: str
    priimek: str

    model_config = {
        "from_attributes": True 
    }

# Pydantic schema for Polet
class PoletSchema(BaseModel):
    idPolet: Optional[int] = None
    cas_vzleta: str
    cas_pristanka: str
    Pilot_idPilot: Optional[int] = None

    model_config = {
        "from_attributes": True 
    }
        

