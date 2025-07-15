from sqlalchemy import Column, Integer, Float, String
from database import Base

class CommercialTaxData(Base):
    __tablename__ = "commercial_tax_data"

    id = Column(Integer, primary_key=True, index=True)
    ds = Column(String, nullable=False)
    y = Column(Integer)
    cci = Column(Float)
    total_companies = Column(Integer)
    gdp = Column(Float)
