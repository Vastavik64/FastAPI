from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from app.database.database import Base
from datetime import datetime
app = FastAPI()

from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date


class User(Base):
    
    '''
    This function creates a model in database with all the defined fields
    '''
    __tablename__ = "User Table"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)      #This is the primary key that increases automatically by one everytime is used
    name = Column(String)
    birthdate = Column(Date)
    gender = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=True)