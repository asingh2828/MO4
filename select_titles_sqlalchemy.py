from sqlalchemy import create_engine, Table, MetaData

# Create the SQLAlchemy engine
engine = create_engine('sqlite:///books.db')

# Create a metadata instance
metadata = MetaData()

# Reflect the table structure from the database
metadata.reflect(bind=engine)

# Get the table object
books_table = metadata.tables['books']

# Execute a select query to retrieve the title column in alphabetical order
query = books_table.select().order_by(books_table.c.title)

# Execute the query and fetch the results
with engine.connect() as connection:
    result = connection.execute(query)
    for row in result:
        print(row['title'])
