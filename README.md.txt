# 🛍️ Fast E-Commerce App (Python + Streamlit)

A simple and fast **E-Commerce web app** built using **Python, Streamlit, and SQLite3**.  
It demonstrates how an e-commerce system can display products, manage a shopping cart, and simulate a checkout — all in a clean UI built with Streamlit.

---

## 🚀 Features
✅ Display products with names, images, and prices  
✅ Add products to a cart (stored in Streamlit session state)  
✅ View and remove products from the cart  
✅ Checkout with a total price summary  
✅ SQLite database (`products.db`) for data persistence  
✅ Lightweight, easy to deploy (Streamlit Cloud / Render)

---

## 🧠 Tech Stack
| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **Backend / Logic** | Python |
| **Database** | SQLite3 |
| **Data Visualization** | Streamlit Components |
| **Environment** | Virtualenv / venv |

---

## 🗂️ Project Structure
fast_ecommerce/
│
├── app.py # Main Streamlit app
├── db_init.py # Initializes the SQLite database
├── products.db # (Generated automatically by db_init.py)
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/nitishanaga/fast_ecommerce.git
cd fast_ecommerce
2️⃣ Create and Activate Virtual Environment
Windows:

bash
Copy code
python -m venv .venv
.venv\Scripts\activate
macOS / Linux:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Initialize the Database
bash
Copy code
python db_init.py
If you see
products.db exists, skipping creation.
✅ It means your database is ready.

5️⃣ Run the Streamlit App
bash
Copy code
streamlit run app.py
Then open the local URL shown in your terminal (e.g., http://localhost:8501).

🧾 Example UI Sections
🛒 Shop Tab
Displays product cards with names, prices, and Add to Cart buttons.

🧾 Cart Tab
Shows added items, total price, and Checkout button.

ℹ️ About Tab
Displays app information and credits.

📦 Requirements
This app uses:

nginx
Copy code
streamlit
pillow
Install them using:

bash
Copy code
pip install streamlit pillow
🧑‍💻 Author
Nitisha Naga
👩‍💻 Final Year Engineering Student
🔗 GitHub: @nitishanaga

📄 License
This project is open-source under the MIT License.

🌟 Future Improvements
Add login/signup functionality

Integrate a real payment gateway (e.g., Razorpay or Stripe)

Add product categories and search

Deploy on Streamlit Cloud for public access

✨ Built with Python, Streamlit, and a lot of ❤️ by Nitisha Naga.