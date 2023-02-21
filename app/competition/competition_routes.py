from fastapi import APIRouter , Depends
from app.database.database import get_db , engine ,SessionLocal
from app.competition.competition_schemas import CreateCompetition, DisplayCompetitions
from app.competition.competition_model import Competition
from sqlalchemy.orm import Session
from typing import List

from fastapi import APIRouter

competition_route = APIRouter()

# Get all the competitions
@competition_route.get("/v1/competition", response_model=List[DisplayCompetitions])
def get_competitions(db: Session = Depends(get_db)):

    '''
    Define a function with session directed to the database to fetch all the competitions using .all()
    '''
    all_competitions = db.query(Competition).all()
    return all_competitions


# Get a competition by id
@competition_route.get("/v1/competition/{id}", response_model=DisplayCompetitions)
def get_competition_by_id(id, db: Session = Depends(get_db)):

    '''
    instead of .all() use .filter() to get an item for a particular parameter
    '''
    competition_by_id = db.query(Competition).filter(Competition.id == id).first()
    return competition_by_id


# Create a competition
@competition_route.post("/v1/competition/create", response_model= DisplayCompetitions)
def create_competition(request: CreateCompetition, db: Session = Depends(get_db)):

    '''
        Add Competition can be created with the help of various parameters specified in 'CreateCompetition' class
    '''
    add_competition = Competition(**request.dict())
    db.add(add_competition)                                     #use .add() to add a competition
    db.commit()                                                 #commit the changes

    return add_competition


# Delete a competition
@competition_route.delete("/v1/competition/delete/{id}")
def delete_competition(id: int, db:Session = Depends(get_db)):

    '''
    Define a function to delete a particular Competition with the help of id
    '''
    db.query(Competition).filter(Competition.id == id).delete(synchronize_session=False)            #use .delete() to remove a competition
    db.commit                                   #commit the changes

    return {"Message": "Competition deleted successfully"}


# Update a competition
@competition_route.put("/v1/competition/update/{id}")
def update_competition(id, request: CreateCompetition, db: Session = Depends(get_db)):
    
    '''
    A function that fetches parameters which can be edited with reference to its unique id. It also allows particular parameter(s) to be modified without altering all the fields
    '''
    upd_competition = db.query(Competition).filter(Competition.id == id).update(request.dict(exclude_unset=True))
    db.commit()

    return {"Message": "Update operation performed successfully"}