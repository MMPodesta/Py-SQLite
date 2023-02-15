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

# create first table
cursor.executemany("insert into gta values (?,?,?)", release_list)  # ? => place holder for values to be insert

# print all database rows
for row in cursor.execute("select * from gta"):
    print(row)

cursor.execute("select * from gta")
search_all_cities = cursor.fetchall()

# print specific rows
print("**********************************************")
cursor.execute('select * from gta where city="Liberty City"')
gta_search = cursor.fetchall()
print(gta_search)

# create second table
print("**********************************************")
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.execute("insert into cities values (?,?)", ("Liberty City", "New York"))

# fetch specific row
cursor.execute('select * from cities where gta_city="Liberty City"')
cities_search = cursor.fetchall()
print(cities_search)

print("**********************************************")
# adjust retrieved values
for i in search_all_cities:
    # change for "new york" if value is "Liberty City"
    adjusted = [cities_search[0][1] if value == cities_search[0][0] else value for value in i]
    print(adjusted)

connection.close()
