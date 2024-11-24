from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Pydantic schema for Letalo
class LetaloSchema(BaseModel):
    idLetalo: int
    ime_letala: Optional[str] = None
    tip: Optional[str] = None
    registrska_st: Optional[str] = None
    Polet_idPolet: Optional[int] = None

    model_config = {
        "from_attributes": True 
    }

# Pydantic schema for Pilot
class PilotSchema(BaseModel):
    idPilot: int
    ime: str
    priimek: str

    model_config = {
        "from_attributes": True 
    }

# Pydantic schema for Polet
class PoletSchema(BaseModel):
    idPolet: int
    cas_vzleta: datetime
    cas_pristanka: datetime
    Pilot_idPilot: Optional[int] = None

    model_config = {
        "from_attributes": True 
    }
        

