#First import sqlite3
import sqlite3
#Connect to the database using sqlite3.connect('')
connection = sqlite3.connect("post.db")
#Create a cursor class object using .cursor()
#This allows you to execute sql commands, using .execute()
#Cursor Reading: https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm#:~:text=The%20sqlite3.,of%20the%20Connection%20object%2Fclass
cursor = connection.cursor()
print(cursor.execute('SELECT * from posts;').fetchall())

new_table = '''
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY,
        name TEXT,
        comment TEXT
    )
    '''
cursor.execute(new_table)
user_input = input("Enter an id to select a post: ")
post = cursor.execute(f'''
    SELECT * FROM posts
    WHERE id = {user_input};
''').fetchone()

comments = cursor.execute(f'''
    SELECT * FROM comments
    WHERE post_id = {user_input};
''').fetchall()

print(post)
print("Comments")
for comment in comments:
    print(comment)

connection.commit()


