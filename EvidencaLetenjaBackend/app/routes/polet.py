from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from datetime import datetime
from typing import List
from app.core.database import get_db
from app.models.schemas import PoletSchema
from app.models.models import PoletModel

router = APIRouter()

DATE_FORMAT = "%d/%m/%Y %H:%M"

@router.post("/dodajPolet/", response_model=PoletSchema)
def create_polet(polet: PoletSchema, db: Session = Depends(get_db)):
    try:
        datetime.strptime(polet.cas_vzleta, DATE_FORMAT)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format for cas_vzleta. Expected format: {DATE_FORMAT}"
        )

    try:
        datetime.strptime(polet.cas_pristanka, DATE_FORMAT)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format for cas_pristanka. Expected format: {DATE_FORMAT}"
        )
        
    new_polet = PoletModel(
        cas_vzleta=polet.cas_vzleta,
        cas_pristanka=polet.cas_pristanka,
        Pilot_idPilot=polet.Pilot_idPilot,
    )

    # Add and commit the new entry
    db.add(new_polet)
    db.commit()
    db.refresh(new_polet)

    # Return the created instance as a schema
    return PoletSchema(
        idPolet=new_polet.idPolet,
        cas_vzleta=new_polet.cas_vzleta,
        cas_pristanka=new_polet.cas_pristanka,
        Pilot_idPilot=new_polet.Pilot_idPilot,
    )

@router.get("/pridobiPolete/", response_model=List[PoletSchema])
def read_poleti(db: Session = Depends(get_db)):
    poleti = db.query(PoletModel).all()
    # Return the raw string from the database, with parsing handled in the schema or method
    return [
        PoletSchema(
            idPolet=polet.idPolet,
            cas_vzleta=polet.cas_vzleta,
            cas_pristanka=polet.cas_pristanka,
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
            cas_vzleta=polet.cas_vzleta,
            cas_pristanka=polet.cas_pristanka,
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
            cas_vzleta=polet.cas_vzleta,
            cas_pristanka=polet.cas_pristanka,
            Pilot_idPilot=polet.Pilot_idPilot
        )
        for polet in poleti
        if datetime.strptime(polet.cas_vzleta, DATE_FORMAT) < current_date
    ]

@router.put("/poleti/{idPolet}", response_model=dict)
def update_polet(idPolet: int, polet: PoletSchema, db: Session = Depends(get_db)):
    # Fetch the existing flight details
    existing_polet = db.query(PoletModel).filter(PoletModel.idPolet == idPolet).first()

    if not existing_polet:
        raise HTTPException(status_code=404, detail="Polet not found")

    # Update the fields if new values are provided
    if polet.cas_vzleta is not None:
        existing_polet.cas_vzleta = polet.cas_vzleta

    if polet.cas_pristanka is not None:
        existing_polet.cas_pristanka = polet.cas_pristanka

    # Commit the changes only if there are updates
    db.commit()

    return {"message": f"Polet with id {idPolet} updated successfully"}

@router.get("/pridobiPoletePilota/{pilot_id}", response_model=List[PoletSchema])
def read_poleti_for_pilot(pilot_id: int, db: Session = Depends(get_db)):
    poleti = db.query(PoletModel).filter(PoletModel.Pilot_idPilot == pilot_id).all()

    if not poleti:
        raise HTTPException(
            status_code=404,
            detail=f"No flights found for pilot with ID {pilot_id}"
        )

    return [
        PoletSchema(
            idPolet=polet.idPolet,
            cas_vzleta=polet.cas_vzleta,
            cas_pristanka=polet.cas_pristanka,
            Pilot_idPilot=polet.Pilot_idPilot
        )
        for polet in poleti
    ]