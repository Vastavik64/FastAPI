from fastapi import APIRouter , Depends, Form, HTTPException, status
from app.database.database import get_db , engine ,SessionLocal
from app.entry.entry_schemas import CreateEntry, DisplayEntries
from app.entry.entry_model import Entry
from sqlalchemy.orm import Session
from typing import List

from fastapi import APIRouter

entry_route = APIRouter()

# Get all the entries
@entry_route.get("/v1/entry", response_model=List[DisplayEntries])
def get_entries(db: Session = Depends(get_db)):
    
    '''
    Define a function with session directed to the database to fetch all the Entries using .all()
    '''
    all_entries = db.query(Entry).all()
    return all_entries

# Get an entry by id
@entry_route.get("/v1/entry/{id}", response_model= DisplayEntries)
def get_entry_by_id(id, db: Session = Depends(get_db)):

    '''
    instead of .all() use .filter() to get an item for a particular parameter
    '''
    entry_by_id = db.query(Entry).filter(Entry.id == id).first()
    return entry_by_id

# Create an entry
@entry_route.post("/v1/entry/create", response_model = DisplayEntries)
def create_entry(request: CreateEntry, db: Session = Depends(get_db)):

    '''
        Add Enry can be created with the help of various parameters specified in 'CreateEntry' class
    '''
    add_entry = Entry(**request.dict())
    db.add(add_entry)                               #use .add() to add a competition
    db.commit()                                     #commit the changes

    return add_entry

# Delete an entry
@entry_route.delete("/v1/entry/delete/{id}")
def delete_entry(id: int, db: Session = Depends(get_db)):

    '''
    Define a function to delete a particular Entry with the help of id
    '''
    db.query(Entry).filter(Entry.id == id).delete(synchronize_session=False)            #use .delete() to remove an Entry
    db.commit()                             #commit the changes

    return {"Message": "Entry deleted successfully"}

# Update an entry
@entry_route.put("/v1/entry/update/{id}")
def update_entry(id, request: CreateEntry, db: Session = Depends(get_db)):

    '''
    A function that fetches parameters which can be edited with reference to its unique id. It also allows particular parameter(s) to be modified without altering all the fields
    '''
    upd_entry = db.query(Entry).filter(Entry.id == id).update(request.dict(exclude_unset=True))
    db.commit()

    return {"Message": "Update operation performed successfully"}