import sqlite3

# Setting up connection
connection = sqlite3.connect("products.db")
# Setting up object to run commands
cursor = connection.cursor()

# Setting up classes like normal
class Product:
    all = []

    def __init__(self, name, category, price, quantity, id=-1):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        Product.all.append(self)

    # Create
    def save_to_database(self):
        # Write out a command
        value = '''
        INSERT INTO products (name, category, price, quantity)
        VALUES (?, ?, ?, ?);
        '''
        # Run command
        cursor.execute(value, (self.name, self.category, self.price, self.quantity))
        # Commit when changing database
        connection.commit()
        # Set self.id to the last inserted row id
        self.id = cursor.lastrowid

    # Delete
    def delete_from_database(self):
        value = '''
        DELETE FROM products
        WHERE id = ?;
        '''
        cursor.execute(value, (self.id,))
        connection.commit()

    # Read
    @classmethod
    def get_product_by_id(cls, product_id):
        value = '''
        SELECT * FROM products
        WHERE id = ?;
        '''
        cursor.execute(value, (product_id,))
        return cursor.fetchone()

    @classmethod
    def get_all_products(cls):
        value = '''
        SELECT * FROM products;
        '''
        cursor.execute(value)
        return cursor.fetchall()


# Ensure the table is created
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER
    );
''')
connection.commit()

# Example usage:
product1 = Product("Laptop", "Electronics", 1200.0, 10)
product1.save_to_database()
print("Inserted Product 1 with ID:", product1.id)

# Retrieving a Product by ID
product1_from_db = Product.get_product_by_id(product1.id)
print("Retrieved from database:", product1_from_db)

# Retrieving all Products from the database
all_products = Product.get_all_products()
print("All Products in the database:", all_products)

# Deleting a Product from the database
product1.delete_from_database()
print("Product 1 deleted from database.")
