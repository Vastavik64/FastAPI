from  app.database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date, ForeignKey
from app.user.user_model import User
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

class Competition(Base):

    '''
    This function creates a model in database with all the defined fields
    '''
    __tablename__ = "Competition Table"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)              #This is the primary key that increases automatically by one everytime is used
    name = Column(String)
    status = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey(User.id))                  #ForeignKey is used to connect two or multiple models