import sqlite3
import os

DB = "products.db"

products = [
    ("Red Hoodie", "Comfortable red hoodie, 100% cotton", 29.99, "images/red_hoodie.jpg"),
    ("Blue Sneakers", "Lightweight running shoes", 59.99, "images/blue_sneakers.jpg"),
    ("Coffee Mug", "Ceramic mug 350ml", 9.99, "images/mug.jpg"),
    ("Wireless Mouse", "Ergonomic wireless mouse", 24.99, "images/mouse.jpg"),
    ("Backpack", "Water-resistant backpack 20L", 39.99, "images/backpack.jpg"),
]

def init_db():
    if os.path.exists(DB):
        print(f"{DB} exists, skipping creation.")
        return
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL,
        image TEXT
    )
    """)
    c.executemany("INSERT INTO products (name, description, price, image) VALUES (?, ?, ?, ?)", products)
    conn.commit()
    conn.close()
    print(f"Created {DB} with sample products.")

if __name__ == "__main__":
    init_db()
