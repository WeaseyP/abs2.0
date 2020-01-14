import psycopg2

#Connect to the db
con = psycopg2.connect(
    host = "localhost",
    database="data",
    user = "myuser",
    password = "mypass"
)
cur = con.cursor()

with open('birth.csv', 'r') as f:
    cur.copy_from(f, 'births', sep=',')
    con.commit()

cur.execute("SELECT * FROM years")
print(cur.fetchall())

cur.close()

#Close the connection
con.close()

