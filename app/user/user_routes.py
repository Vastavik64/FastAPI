from fastapi import APIRouter, Depends, Form, HTTPException, status
from app.database.database import get_db , engine ,SessionLocal
from app.user.user_schemas import CreateUser, DisplayUsers
from app.user.user_model import User
from sqlalchemy.orm import Session
from typing import List


user_route = APIRouter()

# Read all the users
@user_route.get("/v1/user", response_model = List[DisplayUsers])
def get_users(db: Session = Depends(get_db)):

    '''
    Define a function with session directed to the database to fetch all the users using .all()
    '''
    all_users = db.query(User).all()
    return all_users


# Get a specific user by id
@user_route.get('/v1/user/{id}', response_model = DisplayUsers)
def get_user_by_id(id, db: Session = Depends(get_db)):

    '''
    instead of .all() use .filter() to get an item for a particular parameter
    '''
    user_by_id = db.query(User).filter(User.id == id).first()
    return user_by_id



# Create a user
@user_route.post('/v1/user/create', response_model = DisplayUsers)
def create_user(request: CreateUser, db: Session = Depends(get_db)):

    '''
        Add user can be created with the help of three parameters, name, birthdate and gender, specified in 'CreateUser' class
    '''
    add_user = User(**request.dict())
    db.add(add_user)                                #use .add() to add the user
    db.commit()                                     #commit the changes

    return add_user



# Delete a user by id
@user_route.delete('/v1/user/delete/{id}')
def delete_user(id, db: Session = Depends(get_db)):

    '''
    Define a function to delete a particular user with the help of id
    '''
    db.query(User).filter(User.id == id).delete(synchronize_session=False)   #use .delete() to remove a user
    db.commit()                                                              #commit the changes

    return {"Message":"User Deleted Successfully"}


# Update Operation
@user_route.put('/v1/user/update/{id}')
def update_user(id, request: CreateUser, db: Session = Depends(get_db)):
    
    '''
    A function that fetches parameters which can be edited with reference to its unique id. It also allows particular parameter(s) to be modified without altering all the fields
    '''
    upd_user = db.query(User).filter(User.id == id).update(request.dict(exclude_unset=True))
    db.commit()

    return {"Message": "User Updated Successfully"}