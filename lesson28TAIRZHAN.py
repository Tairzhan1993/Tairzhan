# # Задание 1
# # SELECT * FROM orders;

# # Задание 2
# # SELECT DISTINCT category FROM products;


# # задание 3
# # from sqlalchemy import create_engine, Column, Integer, String
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker


# # engine = create_engine('sqlite:///mydatabase.db', echo=True)


# # Base = declarative_base()


# # class Person(Base):
# #     __tablename__ = 'person'
    
# #     id = Column(Integer, primary_key=True)
# #     first_name = Column(String)
# #     last_name = Column(String)
# #     balance = Column(Integer)


# # Base.metadata.create_all(engine)


# # Session = sessionmaker(bind=engine)
# # session = Session()


# # results = session.query(Person.first_name, Person.last_name).filter(Person.balance > 1000).all()


# # for result in results:
# #     print(result)

# #     задание 4

# #     from sqlalchemy import create_engine, Column, Integer, String
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker


# # engine = create_engine('sqlite:///mydatabase.db', echo=True)


# # Base = declarative_base()


# # class Employee(Base):
# #     __tablename__ = 'employees'
    
# #     id = Column(Integer, primary_key=True)
# #     name = Column(String)
# #     salary = Column(Integer)


# # Base.metadata.create_all(engine)


# # Session = sessionmaker(bind=engine)
# # session = Session()


# # results = session.query(Employee).order_by(Employee.salary.desc()).all()


# # for employee in results:
# #     print(f"Name: {employee.name}, Salary: {employee.salary}")

# #     Задание 5
# #     from sqlalchemy import create_engine, update
# # from sqlalchemy.orm import sessionmaker
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy import Column, Integer


# # engine = create_engine('sqlite:///mydatabase.db', echo=True)


# # Base = declarative_base()


# # class Employee(Base):
# #     __tablename__ = 'employees'
    
# #     id = Column(Integer, primary_key=True)
# #     name = Column(String)
# #     salary = Column(Integer)


# # Session = sessionmaker(bind=engine)
# # session = Session()


# # session.query(Employee).update({Employee.salary: Employee.salary * 1.05})


# # session.commit()

# Задание 6
# from sqlalchemy import create_engine, update
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String


# engine = create_engine('sqlite:///mydatabase.db', echo=True)


# Base = declarative_base()


# class Order(Base):
#     __tablename__ = 'orders'
    
#     id = Column(Integer, primary_key=True)
#     status = Column(String)
#     country = Column(String)


# Session = sessionmaker(bind=engine)
# session = Session()


# session.query(Order).filter(Order.country == 'USA').update({Order.status: 'Processing'})


# session.commit()

# Задание 7
# from sqlalchemy import create_engine, update
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String, Integer, Float


# engine = create_engine('sqlite:///mydatabase.db', echo=True)


# Base = declarative_base()

# class Product(Base):
#     __tablename__ = 'products'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     price = Column(Float)
#     quantity = Column(Integer)

# Session = sessionmaker(bind=engine)
# session = Session()

# session.query(Product).filter(Product.quantity < 20).update({Product.price: Product.price * 0.9})

# session.commit()

# задание 8
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

# session.query(Customer).filter(Customer.balance > 5000).update({Customer.status: 'Active'})

# session.commit()




