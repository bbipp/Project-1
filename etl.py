# https://sportsdata.io/developers/api-documentation/nfl

# https://www.dolthub.com/repositories/Liquidata/nfl-play-by-play/data/master


import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('nfl_2018.sql')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS ")
 
# Creating table
table = """ CREATE TABLE GEEK (
            Email VARCHAR(255) NOT NULL,
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Score INT
        ); """
 
cursor_obj.execute(table)
 
cursor_obj.execute("insert into GEEK values ('h', 'i' , 'j', 100)")
data = (cursor_obj.execute("select * from GEEK"))

for row in data:
    print(row)

print("Table is Ready")
 
# Close the connection
connection_obj.close()
