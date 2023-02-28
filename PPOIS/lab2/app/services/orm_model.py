
Base = declarative_base()


class Customer(Base):
    __table_name__ = 'customer'
    fullname = Column(String)
    account_number = Column(String, primary_key=True)
    address = Column(String)
    mobile = Column(String)
    landline = Column(String)
