from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel

class Entry(BaseModel):
    id: int
    title: str
    topic: str
    state: str
    country: str
    is_delete: bool
    created_at: datetime
    updated_at: datetime
    competition_id: int


class CreateEntry(BaseModel):

    '''
    This class includes parameters to be accepted as input from the user
    '''
    title: str
    topic: str
    state: str
    country: str
    competition_id: int

    class Config:
        orm_mode=True                       #Enable ORM mode

class DisplayEntries(BaseModel):

    '''
    This class includes all the objects to be displayed as the response of API
    '''
    id: int
    title: str
    topic: str
    state: str
    country: str
    competition_id: int = None
    
    class Config:
        orm_mode=True                       #Enable ORM mode