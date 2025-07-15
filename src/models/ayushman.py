from sqlalchemy import Column, Integer, String
from database import Base

class AyushmanData(Base):
    __tablename__ = "ayushman_bharat_data"

    id = Column(Integer, primary_key=True, index=True)
    ds = Column(String, nullable=False)
    y = Column(Integer)
    total_connection = Column(Integer)
    population = Column(Integer)
