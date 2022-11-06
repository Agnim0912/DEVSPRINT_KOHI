import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()

'''c.execute ("""create table coffee(
            Recipe text,
            Temperature text,
            Expresso integer,
            Coffee text,
            Milk text,
            water text,
            Extra text);
           """)'''
#c.execute('''INSERT INTO coffee VALUES ("Espresso","Hot", 1, "No", "No", "No", "No"),
'''            ("Doppio", "Hot", 2,	"No", "No",	"No", "No"),
            ("Red Eye", "Hot", 1, "Yes", "No","No","No"),
            ("Black Eye", "Hot", 2, "Yes", "No", "No", "No"),
            ("Americano", "Hot", 1, "No", "No", "Yes", "No"),
            ("Long Black",	"Hot",	2,	"No",	"No",	"Yes",	"No"),
            ("Macchiato",	"Steaming",	1, 	"No",	"Yes",	"No",	"No"),
            ("Long Macchiato",	"Steaming",	2, 	"No",	"Yes",	"No",	"No"),
            ("Cortado", "Warm",	1, 	"No",	"Yes",	"No",	"Foam"),
            ("Breve",	"Steaming",	1, 	"No",	"Yes",	"No",	"Foam"),
            ("Cappaccino", 	"Steaming",	2, 	"No",	"Yes",	"No",	"No"),
            ("Flat White",	"Steaming",	1, 	"No",	"Yes",	"No",	"No"),
            ("Cafe Latte", 	"Steaming",	1, 	"No",	"Yes",	"No",	"Foam"),
            ("Mocha",	"Steaming",	1, 	"No",	"No",	"No",	"Chocolate Syrup"),
            ("Vienna", "Hot",	2, 	"No",	"No",	"No",	"Whipped Cream"),
            ("Affogato",	"Cold",	2, 	"No",	"No",	"No",	"Vanilla Icecream"),
            ("Cafe Au Lait",	"Scalding",	0,	"Yes",	"No",	"No",	"No"),'''
#           ("Iced Coffee",	"Cold",	2,	"No",	"Yes",	"No",	"Ice Flavouring Syrup")''')
item, item2, item3, item4, item5, item6 = "Steaming", 1, "No", "Yes", "No", "No"
c.execute('''SELECT Recipe from coffee 
            WHERE Temperature="{}" AND Expresso="{}" AND Coffee="{}" AND Milk="{}" AND water="{}" AND Extra="{}"'''.format(item, item2, item3, item4, item5, item6))
conn.commit()
a = c.fetchall()
for u in a:
    for j in u:
        print(j)

conn.close()