import sqlite3
import matplotlib.pyplot as plt

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

# data visualization with matplotlib
cursor.execute("SELECT release_year, release_name FROM gta")
year_name = cursor.fetchall()
years = []
names = []

# for each tuple element "row"
for i in year_name:
    years.append(i[0])  # append column 1 to years list
    names.append(i[1])  # append column 2 to name list

plt.plot(names, years)
plt.xlabel("Game")
plt.ylabel("Release year")
plt.title("GTA release graph")
plt.show()

# alter table gta and make a new graph based on sales
cursor.execute("ALTER TABLE gta ADD sales INTEGER")  # add new column
query = "UPDATE gta SET sales = ? WHERE release_year = ?"  # prepare update query
cursor.execute("SELECT release_year FROM gta")  # get all years, (use them to distinguish each game)
rows = cursor.fetchall()
values = [3, 2, 14, 17, 21, 25, 140]  # Sales in Millions of copies
i = 0
# for each row execute the update query, adding sales of each game
for row in rows:
    cursor.execute(query, (values[i], row[0]))
    i += 1

# plot graph
# prepare lists to plot
left_coordinates = []
bar_labels = []
heights = []

# get all names and respective sales
cursor.execute("SELECT release_name, sales FROM gta")
rows = cursor.fetchall()
i = 1

# for each row, add its game name and sales to list
for row in rows:
    left_coordinates.append(i)
    bar_labels.append(row[0])
    heights.append(row[1])
    i += 1

plt.bar(left_coordinates, heights, tick_label=bar_labels, width=0.4, color=['red', 'black'])
plt.xlabel('Games')
plt.ylabel('Sales - Millions of copies')
plt.title("GTA bar graph")
plt.show()

connection.close()
