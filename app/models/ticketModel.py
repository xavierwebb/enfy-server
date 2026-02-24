from app.database import Base
from sqlalchemy import Column, Integer

class Ticket(Base):
    __tablename__ = 'ticket'
    
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    user_id = Column(Integer)