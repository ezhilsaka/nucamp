import psycopg2

#Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname = week3 user=postgres host = localhost port=5432
    """
)

#command to autocommit the changes to the database
conn.set_session(autocommit=True)

#Open a cursor to perform database operations
cur = conn.cursor()

#using cursor objects to do operations on the table
cur.execute(
    """
    DROP TABLE IF EXISTS veggies
    """
)

cur.execute(
    """
    CREATE TABLE veggies(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        color TEXT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO veggies VALUES 
    (1, 'carrot', 'orange'),
    (2, 'onion', 'yellow'),
    (3, 'zucchini', 'green'),
    (4, 'squash', 'yellow'),
    (5, 'pepper', 'red'),
    (6, 'onion', 'red')
    """
)

# Execute a query
cur.execute(
    """
    SELECT * FROM veggies
    """
)

# Retrieve query results
records = cur.fetchall()

print(records)

cur.execute(
    """
    SELECT color, name FROM veggies
    """
)

veggie_records = cur.fetchall()
for v in veggie_records:
    print(v[0], v[1])


print('')  # new line

cur.execute(
    """
    SELECT color, name FROM veggies ORDER BY name, color
    """
)

veggie_records = cur.fetchall()

for i, v in enumerate(veggie_records):
    print(str(i+1) + ".", v[0].capitalize(), v[1].capitalize())