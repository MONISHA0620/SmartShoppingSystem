import sqlite3

def get_customer_profile_from_db(customer_id):
    conn = sqlite3.connect('app/database/ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("SELECT preferences FROM customers WHERE id = ?", (customer_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        preferences = row[0].split(',')
        return {"customer_id": customer_id, "preferences": [pref.strip() for pref in preferences]}
    return None
