import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS Styling
# ---------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .hero {
        padding: 2rem;
        border-radius: 15px;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.1rem;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #1e293b;
    }

    .product-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        min-height: 280px;
    }

    .product-title {
        font-size: 20px;
        font-weight: bold;
        color: #111827;
    }

    .product-category {
        color: #6366f1;
        font-size: 14px;
        font-weight: 600;
    }

    .product-price {
        font-size: 24px;
        color: #16a34a;
        font-weight: bold;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        padding: 20px;
        color: gray;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sample Product Data
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "category": "Electronics",
        "description": "Premium Bluetooth headphones with noise cancellation."
    },
    {
        "name": "Smart Watch Pro",
        "price": 4999,
        "category": "Electronics",
        "description": "Track fitness, heart rate, and notifications on the go."
    },
    {
        "name": "Running Shoes",
        "price": 2499,
        "category": "Fashion",
        "description": "Lightweight running shoes designed for comfort."
    },
    {
        "name": "Leather Backpack",
        "price": 1999,
        "category": "Fashion",
        "description": "Stylish backpack suitable for work and travel."
    },
    {
        "name": "Coffee Maker",
        "price": 3499,
        "category": "Home",
        "description": "Automatic coffee maker with programmable timer."
    },
    {
        "name": "Desk Lamp",
        "price": 899,
        "category": "Home",
        "description": "Modern LED desk lamp with adjustable brightness."
    }
]

# ---------------------------------------------------
# Session State for Shopping Cart
# ---------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.selectbox(
    "Filter by Category",
    categories
)

st.sidebar.markdown("---")

# Shopping Cart Summary
st.sidebar.subheader("🛒 Shopping Cart")

cart_count = len(st.session_state.cart)

cart_total = sum(
    item["price"] for item in st.session_state.cart
)

st.sidebar.metric("Items", cart_count)
st.sidebar.metric("Total", f"₹{cart_total:,}")

# ---------------------------------------------------
# Hero Section
# ---------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛒 MiniStore</h1>
    <p>Your one-stop destination for electronics, fashion, and home essentials.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Welcome Section
# ---------------------------------------------------
st.markdown("""
<div class="section-title">Welcome to MiniStore</div>
""", unsafe_allow_html=True)

st.write(
    """
    Browse our curated collection of premium products.
    Discover the latest gadgets, stylish fashion accessories,
    and modern home essentials—all in one place.
    """
)

# ---------------------------------------------------
# Featured Products Section
# ---------------------------------------------------
st.markdown("""
<div class="section-title">Featured Products</div>
""", unsafe_allow_html=True)

# Filter products based on category
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product
        for product in products
        if product["category"] == selected_category
    ]

# ---------------------------------------------------
# Product Grid using Columns
# ---------------------------------------------------
cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown(f"""
        <div class="product-card">
            <div class="product-category">{product['category']}</div>
            <div class="product-title">{product['name']}</div>
            <div style="margin-top:10px;">
                {product['description']}
            </div>
            <div class="product-price">
                ₹{product['price']:,}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Add to Cart Button
        if st.button(
            f"Add to Cart",
            key=product["name"]
        ):
            st.session_state.cart.append(product)
            st.success(
                f"{product['name']} added to cart!"
            )
            st.rerun()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("""
<div class="footer">
    © 2026 MiniStore | Demo E-Commerce Website built with Streamlit
</div>
""", unsafe_allow_html=True)