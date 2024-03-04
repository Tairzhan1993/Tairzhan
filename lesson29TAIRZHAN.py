# задание 1 
# from sqlalchemy import create_engine, update
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String, Integer, Float

# engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Base = declarative_base()

# class Customer(Base):
#     __tablename__ = 'customers'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     balance = Column(Float)
#     status = Column(String)

# Session = sessionmaker(bind=engine)
# session = Session()

# session.begin()

# try:
#     session.query(Customer).filter(Customer.balance > 5000).update({Customer.status: 'Active'})
    
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()

#     Задание 2
#     from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.exc import SQLAlchemyError

# engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Session = sessionmaker(bind=engine)
# session = Session()

# trans = session.begin()

# try:
#     session.query(Customer).filter(Customer.balance > 5000).update({Customer.status: 'Active'})
#     session.commit()

#     savepoint = session.begin_nested()

#     try:
#         session.query(Customer).filter_by(id=1).update({'name': 'New Name'})
#         session.commit()  
#     except SQLAlchemyError:
#         savepoint.rollback()  
#         raise  
# except SQLAlchemyError:
#     trans.rollback()  
#     raise  
# finally:
#     session.close()

#     Задание 3
#     from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.exc import SQLAlchemyError

# engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Session = sessionmaker(bind=engine)
# session = Session()

# trans = session.begin()

# try:
#     session.query(Customer).filter(Customer.balance > 5000).update({Customer.status: 'Active'})
#     session.commit()  

#     trans.rollback()
# except SQLAlchemyError:
#     trans.rollback()  
#     raise  
# finally:
#     session.close()


