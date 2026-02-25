from app.database import Base
from sqlalchemy import Column, Integer, Enum

class Ticket(Base):
    __tablename__ = 'ticket'
    
    id = Column(Integer, primary_key=True)
    status = Column(Enum('active', 'finished', name='status'), default='active')
    event_id = Column(Integer)
    user_id = Column(Integer)