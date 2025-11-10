import sqlite3
import streamlit as st
from PIL import Image
import os

DB = "products.db"

def get_conn():
    return sqlite3.connect(DB, check_same_thread=False)

def fetch_products():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT id, name, description, price, image FROM products")
    rows = c.fetchall()
    conn.close()
    products = [
        {"id": r[0], "name": r[1], "description": r[2], "price": float(r[3]), "image": r[4]}
        for r in rows
    ]
    return products

def fetch_product(pid):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT id, name, description, price, image FROM products WHERE id=?", (pid,))
    r = c.fetchone()
    conn.close()
    if not r:
        return None
    return {"id": r[0], "name": r[1], "description": r[2], "price": float(r[3]), "image": r[4]}

# --- CART STATE ---
if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(pid, qty=1):
    cart = st.session_state.cart
    cart[str(pid)] = cart.get(str(pid), 0) + qty
    st.session_state.cart = cart
    st.success("Added to cart!")

def remove_from_cart(pid):
    cart = st.session_state.cart
    if str(pid) in cart:
        del cart[str(pid)]
    st.session_state.cart = cart

def cart_items():
    items = []
    for pid_s, qty in st.session_state.cart.items():
        pid = int(pid_s)
        p = fetch_product(pid)
        if p:
            p["qty"] = qty
            p["total"] = qty * p["price"]
            items.append(p)
    return items

# --- UI ---
st.set_page_config(page_title="Fast E-Commerce", layout="wide")
st.title("🛍️ Fast E-Commerce MVP (Streamlit)")

menu = st.sidebar.selectbox("Menu", ["Shop", "Cart", "About"])

if menu == "Shop":
    st.header("Products")
    products = fetch_products()
    cols = st.columns(3)
    for i, prod in enumerate(products):
        col = cols[i % 3]
        with col:
            img_path = prod["image"]
            if img_path and os.path.exists(img_path):
                st.image(Image.open(img_path), use_column_width=True)
            else:
                st.image("https://via.placeholder.com/300x200.png?text=Product", use_column_width=True)
            st.subheader(prod["name"])
            st.write(prod["description"])
            st.write(f"**₹{prod['price']:.2f}**")
            qty = st.number_input(f"Qty_{prod['id']}", min_value=1, max_value=10, value=1, key=f"qty_{prod['id']}")
            if st.button("Add to cart", key=f"add_{prod['id']}"):
                add_to_cart(prod["id"], qty)

elif menu == "Cart":
    st.header("Shopping Cart")
    items = cart_items()
    if not items:
        st.info("Your cart is empty.")
    else:
        total = 0.0
        for item in items:
            st.write(f"**{item['name']}** — ₹{item['price']:.2f} × {item['qty']} = ₹{item['total']:.2f}")
            st.button("Remove", key=f"remove_{item['id']}", on_click=remove_from_cart, args=(item['id'],))
            total += item["total"]
        st.markdown("---")
        st.subheader(f"Total: ₹{total:.2f}")
        if st.button("Checkout"):
            st.success("Checkout successful (demo only).")
            st.session_state._
