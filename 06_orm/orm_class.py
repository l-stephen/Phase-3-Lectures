#implement using a class
import sqlite3
connection = sqlite3.connect("post.db")
cursor = connection.cursor()

class Post:
    def __init__(self, title, id=None):
        self.id = id
        self.title = title
    
    def save(self):
        new_post = cursor.execute(
            f'''
            INSERT INTO posts(title)
            VALUES("{self.title}")
            '''
        )
        connection.commit()
        self.id = cursor.lastrowid

    def delete(self):
        cursor.execute(
            f'''
            DELETE FROM posts
            WHERE id={self.id}
            '''
        )
        connection.commit()

    def patch(self,new_title):
        cursor.execute(
        f'''
        UPDATE posts
        SET title = "{new_title}"
        WHERE id ={self.id};
        ''')
        connection.commit()

    @classmethod
    def get_by_id(cls, search_id):
        data=cursor.execute(
            f'''
            SELECT * FROM posts
            WHERE id = {search_id};
            '''
        ).fetchone()
        if data:
            return Post(data[1], data[0])
        else:
            return None
    
    @classmethod
    def get_all(cls):
        data=cursor.execute(
            f'''
            SELECT * FROM posts;
            '''
        ).fetchall()
        rlist = []
        for post in data:
            rlist.append(Post(post[1],post[0]))
        return rlist

    def __repr__(self):
        return f"{self.id}: {self.title}"

user_input = input("Enter a post id: ")
post1 = Post.get_by_id(user_input) 
print(post1)
all_post = Post.get_all()
print(all_post)

new_post = Post("Testing the save method")
new_post.save()
print(new_post.id)

while True:
    user_select = input('''
        Select a number
        1) Make a new post
        2) Find a post by id
        3) Select all posts
        4) Exit
        ''')
    if user_select == "1":
        user_post = input("Enter the new post title: ")
        new_post = Post(user_post)
        new_post.save()
    elif user_select == "2":
        find_post = input("Enter a post id: ")
        selected = Post.get_by_id(find_post)
        print(selected)
        new_choice = input('''
            Select a number
            1) Patch
            2) Delete
        ''')
        if new_choice == "1":
            new_title = input("Enter a new title: ")
            selected.patch(new_title)
            connection.commit()
        elif new_choice == "2":
            selected.delete()
            connection.commit()
        else:
            print("Not a valid choice")

    elif user_select == "3":
        all_post = Post.get_all()
        print(all_post)

    elif user_select == "4":
        break
    else:
        print("Not Valid Input")
        
        





