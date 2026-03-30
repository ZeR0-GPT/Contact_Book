from contacts_database import create_connection

def add_contact(name, phone, email):
    conn = create_connection()
    conn.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
                 (name, phone, email))
    conn.commit()
    conn.close()

def search_contact(name):
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (f"%{name}%",))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_contact(contact_id):
    conn = create_connection()
    conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

def get_all_contacts():
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM contacts ORDER BY name")
    rows = cursor.fetchall()
    conn.close()
    return rows