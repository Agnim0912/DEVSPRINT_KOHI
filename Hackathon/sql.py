import sqlite3

conn = sqlite3.connect("menu6.db")
c = conn.cursor()

'''c.execute ("""create table coffee(
            Recipe text,
            Temperature text,
            Expresso integer,
            Coffee integer,
            Milk text,
            water text,
            Extra text);
           """)'''
c.execute('''INSERT INTO food VALUES(),
           (15,"mineral water",30),
           ;''')
#c.execute('SELECT * from coffee')
conn.commit()
print (c.fetchall())
conn.close()