from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime


class User(BaseModel):

    id: int
    name: str
    birthdate: date
    gender: str
    created_at: datetime
    updated_at: datetime
    is_active: bool
    is_delete: bool



class CreateUser(BaseModel):

    '''
    This class includes parameters to be accepted as input from the user
    '''
    name: Optional[str] = None
    birthdate: Optional[date]
    gender: Optional[str]
    
    class Config:
        orm_mode=True                       #Enable ORM mode


class DisplayUsers(BaseModel):

    '''
    This class is used to observe the response of API
    '''
    id: int = None
    name: str
    birthdate: date
    gender: str

    class Config:
        orm_mode=True                       #Enable ORM mode