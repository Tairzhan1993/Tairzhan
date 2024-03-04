# задание 1

# from sqlalchemy import insert

# stmt = insert(Person).values(name='Ruslan', age=28)

# connection.execute(stmt)

# задание 2

# import csv
# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


# engine = create_engine('sqlite:///mydatabase.db')


# metadata = MetaData()


# person_table = Table('Person', metadata,
#                      Column('id', Integer, primary_key=True),
#                      Column('name', String),
#                      Column('age', Integer)
#                      )


# connection = engine.connect()


# with open('data.csv', 'r') as csvfile:
#     csv_reader = csv.DictReader(csvfile)
#     for row in csv_reader:
#         stmt = person_table.insert().values(name=row['Name'], age=int(row['Age']))
#         connection.execute(stmt)


# connection.close()
