from app.database import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, String, Table, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

event_payments = Table(
    'events_payments',
    Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
)

class Event(Base):
    
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)

    status = Column(
        Enum('active', 'finished', 'cancelled', name='event_status'), 
        default='active', 
        index=True
    )

    name = Column(String)
    description = Column(String)
    creationDate = Column(DateTime(timezone=True), server_default=func.now())
    eventDate = Column(DateTime)
    ubication = Column(String)
    category = Column(String, index=True)
    price = Column(Integer)

    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship('User', back_populates='eventsCreated')

    paidUsers = relationship(
        'User',
        secondary=event_payments,
        back_populates='eventsBought'
    )