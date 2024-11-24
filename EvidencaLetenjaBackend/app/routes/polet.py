from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from datetime import datetime
from typing import List
from core.database import get_db
from models.schemas import PoletSchema
from models.models import PoletModel

router = APIRouter()

DATE_FORMAT = "%d/%m/%Y %H:%M"

@router.post("/dodajPolet/", response_model=PoletSchema)
def create_polet(polet: PoletSchema, db: Session = Depends(get_db)):
    try:
        # Convert datetime objects to strings in the desired format
        cas_vzleta_str = polet.cas_vzleta.strftime(DATE_FORMAT)
        cas_pristanka_str = polet.cas_pristanka.strftime(DATE_FORMAT)

        new_polet = PoletModel(
            cas_vzleta=cas_vzleta_str,
            cas_pristanka=cas_pristanka_str,
            Pilot_idPilot=polet.Pilot_idPilot
        )

        db.add(new_polet)
        db.commit()
        db.refresh(new_polet)

        return PoletSchema(
            idPolet=new_polet.idPolet,
            cas_vzleta=datetime.strptime(new_polet.cas_vzleta, DATE_FORMAT),
            cas_pristanka=datetime.strptime(new_polet.cas_pristanka, DATE_FORMAT),
            Pilot_idPilot=new_polet.Pilot_idPilot
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid datetime format: {e}")

@router.get("/pridobiPolete/", response_model=List[PoletSchema])
def read_poleti(db: Session = Depends(get_db)):
    poleti = db.query(PoletModel).all()

    # Return the raw string from the database, with parsing handled in the schema or method
    return [
        PoletSchema(
            idPolet=polet.idPolet,
            cas_vzleta=datetime.strptime(polet.cas_vzleta, DATE_FORMAT),
            cas_pristanka=datetime.strptime(polet.cas_pristanka, DATE_FORMAT),
            Pilot_idPilot=polet.Pilot_idPilot
        )
        for polet in poleti
    ]

@router.delete("/polet/{idPolet}", response_model=dict)
def delete_polet(idPolet: int, db: Session = Depends(get_db)):
    polet = db.query(PoletModel).filter(PoletModel.idPolet == idPolet).first()
    if not polet:
        raise HTTPException(status_code=404, detail="Polet not found")

    # Delete the flight (polet)
    db.delete(polet)
    db.commit()
    
    # Return success message
    return {"message": "Polet deleted successfully"}

@router.get("/pridobiPrihodnjeLete/", response_model=List[PoletSchema])
def read_poleti_after_date(db: Session = Depends(get_db)):
    current_date = datetime.now()
    poleti = db.query(PoletModel).all()

    # Filter and parse future flights
    return [
        PoletSchema(
            idPolet=polet.idPolet,
            cas_vzleta=datetime.strptime(polet.cas_vzleta, DATE_FORMAT),
            cas_pristanka=datetime.strptime(polet.cas_pristanka, DATE_FORMAT),
            Pilot_idPilot=polet.Pilot_idPilot
        )
        for polet in poleti
        if datetime.strptime(polet.cas_vzleta, DATE_FORMAT) >= current_date
    ]

@router.get("/pridobiZgodovinoLetov/", response_model=List[PoletSchema])
def read_poleti_before_date(db: Session = Depends(get_db)):
    current_date = datetime.now()
    poleti = db.query(PoletModel).all()

    # Filter and parse past flights
    return [
        PoletSchema(
            idPolet=polet.idPolet,
            cas_vzleta=datetime.strptime(polet.cas_vzleta, DATE_FORMAT),
            cas_pristanka=datetime.strptime(polet.cas_pristanka, DATE_FORMAT),
            Pilot_idPilot=polet.Pilot_idPilot
        )
        for polet in poleti
        if datetime.strptime(polet.cas_vzleta, DATE_FORMAT) < current_date
    ]

@router.put("/poleti/{idPolet}", response_model=dict)
def update_polet(idPolet: int, polet: PoletSchema, db: Session = Depends(get_db)):
    existing_polet = db.query(PoletModel).filter(PoletModel.idPolet == idPolet).first()

    if not existing_polet:
        raise HTTPException(status_code=404, detail="Polet not found")

    # Update only provided fields
    if polet.cas_vzleta:
        try:
            # Parse and update cas_vzleta
            existing_polet.cas_vzleta = datetime.strptime(polet.cas_vzleta, DATE_FORMAT)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Invalid cas_vzleta format: {e}")

    if polet.cas_pristanka:
        try:
            # Parse and update cas_pristanka
            existing_polet.cas_pristanka = datetime.strptime(polet.cas_pristanka, DATE_FORMAT)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Invalid cas_pristanka format: {e}")

    if polet.Pilot_idPilot is not None:
        existing_polet.Pilot_idPilot = polet.Pilot_idPilot

    db.commit()
    return {"message": f"Polet with id {idPolet} updated successfully"}