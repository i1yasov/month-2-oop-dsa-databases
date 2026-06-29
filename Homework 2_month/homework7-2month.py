import sqlite3

connect = sqlite3.connect('store.db')
cursor = connect.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')
connect.commit()

def create_product(name, price, quantity):
    cursor.execute('''
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
    ''', (name, price, quantity))
    connect.commit()
    print("Товар добавлен!")

def read_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    if not products:
        print("Нет товаров")
    else:
        for product in products:
            print(product)

def update_product(id, price):
    cursor.execute('''
    UPDATE products
    SET price = ?
    WHERE id = ?
    ''', (price, id))
    connect.commit()
    print("Цена обновлена!")

def delete_product(id):
    cursor.execute('''
    DELETE FROM products
    WHERE id = ?
    ''', (id,))
    connect.commit()
    print("Товар удален!")

if __name__ == "__main__":
    create_product("Телефон", 15000, 5)
    create_product("Ноутбук", 50000, 2)

    print("\nВсе товары:")
    read_products()

    print("\nОбновляем цену товара с id=1")
    update_product(1, 20000)

    print("\nПосле обновления:")
    read_products()

    print("\nУдаляем товар с id=2")
    delete_product(2)

    print("\nПосле удаления:")
    read_products()

connect.close()