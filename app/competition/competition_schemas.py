from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel

class Competition(BaseModel):
    id: int
    name: str
    status: str
    description: str
    is_active: bool
    is_delete: bool
    created_at: datetime
    updated_at: datetime
    user_id: int

class CreateCompetition(BaseModel):

    '''
    This class includes parameters to be accepted as input from the user
    '''
    name: str
    status: str
    description: str
    user_id: int

    
    class Config:
        orm_mode=True                       #Enable ORM mode


class DisplayCompetitions(BaseModel):

    '''
    This class includes all the objects to be displayed as the response of API
    '''
    id: int
    name: str
    status: str
    description: str
    user_id: int = None

    
    class Config:
        orm_mode=True                       #Enable ORM mode