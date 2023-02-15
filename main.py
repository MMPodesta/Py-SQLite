import sqlite3

connection = sqlite3.connect("gta.db")  # database name
cursor = connection.cursor()  # does all comm with database

# creates table with each datatype
cursor.execute("create table gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

# ? => place holder for values to be insert
cursor.executemany("insert into gta values (?,?,?)", release_list)

connection.close()
