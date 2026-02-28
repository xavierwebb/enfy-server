from app.database import Base
from sqlalchemy import Column, Integer, String

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    category = Column(String)