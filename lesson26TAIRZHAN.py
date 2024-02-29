# # задание 1

# # from sqlalchemy import create_engine, Column, Integer, String
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker


# # engine = create_engine('sqlite:///mydatabase.db', echo=True)


# # Base = declarative_base()


# # class Person(Base):
# #     __tablename__ = 'person'

# #     id = Column(Integer, primary_key=True)
# #     name = Column(String)
# #     age = Column(Integer)


# # Base.metadata.create_all(engine)


# # Session = sessionmaker(bind=engine)
# # session = Session()

# Задание 2


# person1 = Person(name='Victor', age=30)
# person2 = Person(name='Ruslan', age=25)
# person3 = Person(name='Katya', age=35)


# session.add_all([person1, person2, person3])


# session.commit()

