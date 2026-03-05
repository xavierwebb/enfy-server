from app.database import Base
from sqlalchemy import Column, String, Integer

class Aplications(Base):
    __tablename__ = 'aplications'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)
    contact = Column(String)
    theme = Column(String)