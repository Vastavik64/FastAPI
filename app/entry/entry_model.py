from  app.database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date, ForeignKey
from app.competition.competition_model import Competition
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

class Entry(Base):

    '''
    This function creates a model in database with all the defined fields
    '''
    __tablename__ = "Entry Table"
    id = Column(Integer, primary_key=True, index = True, autoincrement=True)            #This is the primary key that increases automatically by one everytime is used
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    is_delete = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    competition_id = Column(Integer, ForeignKey(Competition.id))                        #ForeignKey is used to connect two or multiple models