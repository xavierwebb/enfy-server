from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.eventModel import event_payments

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String, default='Enthusiast')
    email = Column(String, unique=True)
    password = Column(String)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())

    eventsCreated = relationship(
        'Event', 
        back_populates='owner', 
        cascade='all, delete-orphan'
    )

    eventsBought = relationship(
        'Event',
        secondary = event_payments,
        back_populates='paidUsers'
    )