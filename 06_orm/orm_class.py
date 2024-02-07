import sqlite3

connection = sqlite3.connect("ecommerce.db")
cursor = connection.cursor()

class Product:
    all = []

    def __init__(self, name, price, id=None):
        self.id = id
        self.name = name
        self.price = price

    def save(self):
        sql = f'''
        INSERT INTO products(name, price)
        VALUES ("{self.name}", {self.price})
        '''
        cursor.execute(sql)
        connection.commit()

    @classmethod
    def get_product(cls, name):
        sql = f'''
        SELECT * 
        FROM products
        WHERE name = "{name}"
        '''
        data = cursor.execute(sql)
        product = data.fetchone()
        if product:
            return Product(product[0], product[1], product[2])
        else:
            return None
    
    @classmethod
    def create_product(cls, name, price):
        sql = f'''
        INSERT INTO products(name, price)
        VALUES ("{name}", {price})
        '''
        cursor.execute(sql)
        connection.commit()

    def update_price(self, new_price):
        self.price = new_price
        sql = f'''
        UPDATE products
        SET price = {self.price}
        WHERE id = {self.id}
        '''
        cursor.execute(sql)
        connection.commit()

    def delete_self(self):
        sql = f'''
        DELETE from products
        WHERE id = {self.id}
        '''
        cursor.execute(sql)
        connection.commit()

if __name__ == '__main__':
    def view_product():
        input2 = input("Enter product name: ")
        product = Product.get_product(input2)
        if product:
            print("Product found:", product.name, product.price)
        else:
            print("Product not found.")

    def create_product():
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        Product.create_product(name, price)
        print("Product created successfully.")

    def update_product():
        input2 = input("Enter product name to update: ")
        product = Product.get_product(input2)
        if product:
            new_price = input("Enter new price: ")
            product.update_price(new_price)
            print("Product price updated successfully.")
        else:
            print("Product not found.")

    def delete_product():
        input2 = input("Enter product name to delete: ")
        product = Product.get_product(input2)
        if product:
            product.delete_self()
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    while True:
        user_input = input("Create, View, Update, or Delete Product? (Enter quit to exit) ")

        if user_input.lower() == "view":
            view_product()
        elif user_input.lower() == "create":
            create_product()
        elif user_input.lower() == "update":
            update_product()
        elif user_input.lower() == "delete":
            delete_product()
        elif user_input.lower() == "quit":
            print("Exiting....")
            break
        else:
            print("Invalid input. Please try again.")

connection.close()
