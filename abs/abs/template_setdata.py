import psycopg2

#Connect to the db
con = psycopg2.connect(
    host = "localhost",
    database="data",
    user = "myuser",
    password = "mypass"
)
cur = con.cursor()

with open('capitals_best.csv', 'r') as f:
    cur.copy_from(f, 'capital_cities', sep=',')
    con.commit()

cur.close()

#Close the connection
con.close()

