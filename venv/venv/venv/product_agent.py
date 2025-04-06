import sqlite3

def get_products_from_db():
    conn = sqlite3.connect('app/database/ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category FROM products")
    products = [{"id": row[0], "name": row[1], "category": row[2]} for row in cursor.fetchall()]
    conn.close()
    return products
