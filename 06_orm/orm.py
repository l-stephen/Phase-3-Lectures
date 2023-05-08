#First import sqlite3
import sqlite3
#Connect to the database using sqlite3.connect('')
connection = sqlite3.connect("pokemon.db")
#Create a cursor class object using .cursor()
cursor = connection.cursor()
#This allows you to execute sql commands, using .execute()
#Cursor Reading: https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm#:~:text=The%20sqlite3.,of%20the%20Connection%20object%2Fclass
table = '''
    CREATE TABLE Pokemon(
        id INTEGER PRIMARY KEY,
        name TEXT,
        type TEXT,
        size INTEGER,
        owned INTEGER
    );
    '''

cursor.execute(table)

pikachu = '''
    INSERT INTO pokemon (name,type,size,owned)
    VALUES ("Pikachu","Electric",3,1);
    '''
charmander = '''
    INSERT INTO pokemon (name,type,size,owned)
    VALUES ("Charmander","Fire",3,1);
    '''

cursor.execute(pikachu)
cursor.execute(charmander)
#commit CRUD is performed on the table
connection.commit()

