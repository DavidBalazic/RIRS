from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.schemas import PilotSchema
from app.models.models import PilotModel
from typing import List

router = APIRouter()

@router.post("/dodajPilota/", response_model=PilotSchema)
def create_pilot(pilot: PilotSchema, db: Session = Depends(get_db)):
    new_pilot = PilotModel(ime=pilot.ime, priimek=pilot.priimek)
    db.add(new_pilot)
    db.commit()
    db.refresh(new_pilot)
    return new_pilot

@router.get("/pridobiPilote/", response_model=List[PilotSchema])
def read_pilots(db: Session = Depends(get_db)):
    pilots = db.query(PilotModel).all()
    return pilots

@router.delete("/pilot/{idPilot}", response_model=dict)
def delete_pilot(idPilot: int, db: Session = Depends(get_db)):
    pilot = db.query(PilotModel).filter(PilotModel.idPilot == idPilot).first()
    if not pilot:
        raise HTTPException(status_code=404, detail="Pilot not found")
    
    db.delete(pilot)
    db.commit()
    
    return {"message": "Pilot deleted successfully"}
