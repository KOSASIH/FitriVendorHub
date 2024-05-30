from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    phone_number = Column(String, unique=True, nullable=False)
    country_code = Column(String, nullable=False)
    loyalty_points = Column(Integer, default=0)

    sales_transactions = relationship("SalesTransaction", backref="customer")

class SalesTransaction(Base):
    __tablename__ = 'ales_transactions'
    transaction_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    transaction_price = Column(Integer)
    transaction_date = Column(DateTime(timezone='EAT'))
