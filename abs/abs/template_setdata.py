
import psycopg2

#Connect to the db
con = psycopg2.connect(
    host = "localhost",
    database="abs",
    user = "myuser",
    password = "mypass"
)
cur = con.cursor()

with open('Years.csv', 'r') as f:
    cur.copy_from(f, 'population_years', sep=',')
    con.commit()

cur.close()

#Close the connection
con.close()
