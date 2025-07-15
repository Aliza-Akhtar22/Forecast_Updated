from sqlalchemy import Column, Integer, String
from database import Base

class CourtData(Base):
    __tablename__ = "courts_data"

    id = Column(Integer, primary_key=True, index=True)
    ds = Column(String, nullable=False)
    institution = Column(Integer)
    disposal = Column(Integer)
    y = Column(Integer)
