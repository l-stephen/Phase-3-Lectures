#First import sqlite3
import sqlite3

#Connect to the database using sqlite3.connect('')
connection = sqlite3.connect("school.db")
#Create a cursor class object using .cursor()
cursor = connection.cursor()

#This allows you to execute sql commands, using .execute()
#Cursor Reading: https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm#:~:text=The%20sqlite3.,of%20the%20Connection%20object%2Fclass

sql_command = '''
SELECT students.name, courses.topic
FROM major
JOIN courses, students
ON major.student_id == students.id AND major.course_id == courses.id;
'''
cursor.execute(sql_command)
data = cursor.fetchall()
# data = cursor.fetchone()
print(data)


#performing crud on a table
user_input = input("Select a course to delete: ")

sql_command_delete = f'''
DELETE FROM COURSES
WHERE id = {user_input}
'''
cursor.execute(sql_command_delete)
connection.commit()


