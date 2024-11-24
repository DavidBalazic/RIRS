from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.schemas import LetaloSchema
from app.models.models import LetaloModel
from typing import List

router = APIRouter()

@router.post("/dodajLetalo/", response_model=LetaloSchema)
def create_letalo(letalo: LetaloSchema, db: Session = Depends(get_db)):
    new_letalo = LetaloModel(
        ime_letala=letalo.ime_letala,
        tip=letalo.tip,
        registrska_st=letalo.registrska_st,
        Polet_idPolet=letalo.Polet_idPolet
    )
    db.add(new_letalo)
    db.commit()
    db.refresh(new_letalo)
    return new_letalo


@router.get("/pridobiLetala/", response_model=List[LetaloSchema])
def read_letalos(db: Session = Depends(get_db)):
    return db.query(LetaloModel).all()


@router.delete("/letalo/{idLetalo}", response_model=dict)
def delete_letalo(idLetalo: int, db: Session = Depends(get_db)):
    letalo = db.query(LetaloModel).filter(LetaloModel.idLetalo == idLetalo).first()
    if not letalo:
        raise HTTPException(status_code=404, detail="Letalo not found")
    
    db.delete(letalo)
    db.commit()
    return {"message": "Letalo deleted successfully"}


@router.put("/letalo/{idLetalo}", response_model=dict)
def update_letalo(idLetalo: int, letalo: LetaloSchema, db: Session = Depends(get_db)):
    existing_letalo = db.query(LetaloModel).filter(LetaloModel.idLetalo == idLetalo).first()
    if not existing_letalo:
        raise HTTPException(status_code=404, detail="Letalo not found")
    
    if letalo.ime_letala is not None:
        existing_letalo.ime_letala = letalo.ime_letala
    if letalo.tip is not None:
        existing_letalo.tip = letalo.tip
    if letalo.registrska_st is not None:
        existing_letalo.registrska_st = letalo.registrska_st
    if letalo.Polet_idPolet is not None:
        existing_letalo.Polet_idPolet = letalo.Polet_idPolet
    
    db.commit()
    db.refresh(existing_letalo)
    return {"message": f"Letalo with id {idLetalo} updated successfully"}
