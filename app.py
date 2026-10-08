import streamlit as st
from datetime import datetime
import random


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="TastyBites Restaurant POS",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #f7f8fc;
}

/* Main title */
.hero {
    background: linear-gradient(135deg, #ff512f, #f09819);
    padding: 35px;
    border-radius: 24px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 48px;
    margin: 0;
    font-weight: 800;
}

.hero p {
    font-size: 18px;
    margin-top: 8px;
}

/* Section headings */
.section-title {
    font-size: 28px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* Small info cards */
.info-card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
}

/* Cart */
.cart-box {
    background: white;
    padding: 22px;
    border-radius: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

/* Total */
.total-box {
    background: linear-gradient(135deg, #ff512f, #f09819);
    color: white;
    padding: 22px;
    border-radius: 18px;
    text-align: center;
    margin-top: 15px;
}

.total-box h1 {
    margin: 0;
    font-size: 32px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 35px;
    color: #777;
}

/* Make buttons rounded */
.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}

/* Search box */
div[data-testid="stTextInput"] input {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# MENU DATA
# ============================================================

menu = {

# ------------------------- STARTERS -------------------------

"French Fries": {
    "category": "Starters",
    "price": 99,
    "rating": 4.5,
    "description": "Golden crispy fries with special seasoning.",
    "badge": "🔥 Popular",
    "time": 10,
    "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=800"
},

"Peri Peri Fries": {
    "category": "Starters",
    "price": 129,
    "rating": 4.7,
    "description": "Crispy fries tossed in spicy peri peri seasoning.",
    "badge": "🌶️ Spicy",
    "time": 10,
    "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=800"
},

"Chicken Wings": {
    "category": "Starters",
    "price": 219,
    "rating": 4.8,
    "description": "Juicy crispy chicken wings with signature sauce.",
    "badge": "⭐ Bestseller",
    "time": 15,
    "image": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=800"
},

"Chicken 65": {
    "category": "Starters",
    "price": 229,
    "rating": 4.8,
    "description": "Crispy spicy South Indian style chicken.",
    "badge": "🔥 Popular",
    "time": 18,
    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800"
},

"Paneer 65": {
    "category": "Starters",
    "price": 189,
    "rating": 4.6,
    "description": "Crispy paneer cubes with Indian spices.",
    "badge": "🌱 Veg",
    "time": 15,
    "image": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=800"
},

"Veg Spring Rolls": {
    "category": "Starters",
    "price": 129,
    "rating": 4.5,
    "description": "Crispy rolls stuffed with fresh vegetables.",
    "badge": "🌱 Veg",
    "time": 12,
    "image": "https://images.unsplash.com/photo-1548507200-d3c9a1a7d8f0?w=800"
},

"Chicken Spring Rolls": {
    "category": "Starters",
    "price": 169,
    "rating": 4.6,
    "description": "Crispy rolls filled with seasoned chicken.",
    "badge": "🔥 Popular",
    "time": 14,
    "image": "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=800"
},

"Garlic Bread": {
    "category": "Starters",
    "price": 119,
    "rating": 4.4,
    "description": "Toasted bread with garlic butter and herbs.",
    "badge": "⭐ Recommended",
    "time": 10,
    "image": "https://images.unsplash.com/photo-1573140247632-f8fd74997d5c?w=800"
},

"Cheese Garlic Bread": {
    "category": "Starters",
    "price": 159,
    "rating": 4.8,
    "description": "Garlic bread loaded with melted cheese.",
    "badge": "⭐ Bestseller",
    "time": 12,
    "image": "https://images.unsplash.com/photo-1573140247632-f8fd74997d5c?w=800"
},

"Chilli Chicken": {
    "category": "Starters",
    "price": 249,
    "rating": 4.7,
    "description": "Tender chicken tossed with chilli sauce.",
    "badge": "🌶️ Spicy",
    "time": 18,
    "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=800"
},


# ------------------------- PIZZA -------------------------

"Margherita Pizza": {
    "category": "Pizza",
    "price": 249,
    "rating": 4.6,
    "description": "Classic tomato, mozzarella and fresh basil.",
    "badge": "⭐ Bestseller",
    "time": 20,
    "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=800"
},

"Farmhouse Pizza": {
    "category": "Pizza",
    "price": 299,
    "rating": 4.7,
    "description": "Loaded with onion, capsicum, corn and tomato.",
    "badge": "🌱 Veg",
    "time": 22,
    "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800"
},

"Paneer Tikka Pizza": {
    "category": "Pizza",
    "price": 329,
    "rating": 4.8,
    "description": "Indian paneer tikka with cheese and herbs.",
    "badge": "🔥 Popular",
    "time": 22,
    "image": "https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?w=800"
},

"Chicken Tikka Pizza": {
    "category": "Pizza",
    "price": 349,
    "rating": 4.9,
    "description": "Chicken tikka, mozzarella and special sauce.",
    "badge": "⭐ Bestseller",
    "time": 24,
    "image": "https://images.unsplash.com/photo-1594007654729-407eedc4be65?w=800"
},

"BBQ Chicken Pizza": {
    "category": "Pizza",
    "price": 369,
    "rating": 4.8,
    "description": "Smoky BBQ chicken with melted cheese.",
    "badge": "🔥 Chef's Choice",
    "time": 24,
    "image": "https://images.unsplash.com/photo-1566843972142-a7fcb70de55a?w=800"
},

"Pepperoni Pizza": {
    "category": "Pizza",
    "price": 399,
    "rating": 4.9,
    "description": "Classic pepperoni with mozzarella cheese.",
    "badge": "⭐ Bestseller",
    "time": 24,
    "image": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=800"
},

"Cheese Burst Pizza": {
    "category": "Pizza",
    "price": 379,
    "rating": 4.8,
    "description": "Extra cheesy pizza with a creamy cheese center.",
    "badge": "🧀 Extra Cheese",
    "time": 25,
    "image": "https://images.unsplash.com/photo-1579751626657-72bc17010498?w=800"
},

"Corn Cheese Pizza": {
    "category": "Pizza",
    "price": 279,
    "rating": 4.5,
    "description": "Sweet corn and mozzarella cheese.",
    "badge": "🌱 Veg",
    "time": 20,
    "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=800"
},


# ------------------------- BURGERS -------------------------

"Classic Veg Burger": {
    "category": "Burgers",
    "price": 129,
    "rating": 4.4,
    "description": "Crispy veg patty with fresh lettuce and sauce.",
    "badge": "🌱 Veg",
    "time": 12,
    "image": "https://images.unsplash.com/photo-1520072959219-c595dc870360?w=800"
},

"Cheese Burger": {
    "category": "Burgers",
    "price": 159,
    "rating": 4.6,
    "description": "Classic burger with melted cheese.",
    "badge": "⭐ Popular",
    "time": 12,
    "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800"
},

"Paneer Burger": {
    "category": "Burgers",
    "price": 169,
    "rating": 4.5,
    "description": "Crispy paneer patty with creamy sauce.",
    "badge": "🌱 Veg",
    "time": 14,
    "image": "https://images.unsplash.com/photo-1550317138-10000687a72b?w=800"
},

"Crispy Chicken Burger": {
    "category": "Burgers",
    "price": 189,
    "rating": 4.8,
    "description": "Crispy chicken patty with fresh vegetables.",
    "badge": "⭐ Bestseller",
    "time": 15,
    "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800"
},

"Chicken Cheese Burger": {
    "category": "Burgers",
    "price": 219,
    "rating": 4.9,
    "description": "Crispy chicken with double cheese.",
    "badge": "🔥 Popular",
    "time": 15,
    "image": "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=800"
},

"Double Chicken Burger": {
    "category": "Burgers",
    "price": 269,
    "rating": 4.9,
    "description": "Double chicken patties with special sauce.",
    "badge": "🔥 Mega",
    "time": 18,
    "image": "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=800"
},

"BBQ Chicken Burger": {
    "category": "Burgers",
    "price": 229,
    "rating": 4.8,
    "description": "Juicy chicken burger with smoky BBQ sauce.",
    "badge": "⭐ Chef's Choice",
    "time": 16,
    "image": "https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=800"
},


# ------------------------- MAIN COURSE -------------------------

"White Sauce Pasta": {
    "category": "Main Course",
    "price": 199,
    "rating": 4.6,
    "description": "Creamy pasta with herbs and parmesan.",
    "badge": "⭐ Popular",
    "time": 18,
    "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=800"
},

"Red Sauce Pasta": {
    "category": "Main Course",
    "price": 189,
    "rating": 4.5,
    "description": "Italian pasta in rich tomato sauce.",
    "badge": "🌱 Veg",
    "time": 18,
    "image": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=800"
},

"Chicken Pasta": {
    "category": "Main Course",
    "price": 249,
    "rating": 4.8,
    "description": "Creamy pasta with grilled chicken.",
    "badge": "🔥 Popular",
    "time": 20,
    "image": "https://images.unsplash.com/photo-1533777857889-4be7c70b33f7?w=800"
},

"Alfredo Pasta": {
    "category": "Main Course",
    "price": 229,
    "rating": 4.7,
    "description": "Rich creamy Alfredo pasta.",
    "badge": "⭐ Recommended",
    "time": 20,
    "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=800"
},

"Veg Noodles": {
    "category": "Main Course",
    "price": 159,
    "rating": 4.4,
    "description": "Stir fried noodles with fresh vegetables.",
    "badge": "🌱 Veg",
    "time": 15,
    "image": "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?w=800"
},

"Chicken Noodles": {
    "category": "Main Course",
    "price": 199,
    "rating": 4.7,
    "description": "Wok tossed noodles with chicken.",
    "badge": "🔥 Popular",
    "time": 17,
    "image": "https://images.unsplash.com/photo-1552611052-33e04de081de?w=800"
},

"Veg Fried Rice": {
    "category": "Main Course",
    "price": 159,
    "rating": 4.5,
    "description": "Classic fried rice with vegetables.",
    "badge": "🌱 Veg",
    "time": 15,
    "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=800"
},

"Chicken Fried Rice": {
    "category": "Main Course",
    "price": 199,
    "rating": 4.8,
    "description": "Fried rice with seasoned chicken.",
    "badge": "⭐ Bestseller",
    "time": 17,
    "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=800"
},


# ------------------------- INDIAN -------------------------

"Chicken Biryani": {
    "category": "Indian",
    "price": 249,
    "rating": 4.9,
    "description": "Aromatic basmati rice with tender chicken.",
    "badge": "⭐ Bestseller",
    "time": 25,
    "image": "https://images.unsplash.com/photo-1563379091339-03246963d51a?w=800"
},

"Veg Biryani": {
    "category": "Indian",
    "price": 199,
    "rating": 4.7,
    "description": "Fragrant basmati rice with vegetables and spices.",
    "badge": "🌱 Veg",
    "time": 22,
    "image": "https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=800"
},

"Paneer Butter Masala": {
    "category": "Indian",
    "price": 229,
    "rating": 4.8,
    "description": "Soft paneer in rich creamy tomato gravy.",
    "badge": "⭐ Popular",
    "time": 20,
    "image": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=800"
},

"Kadai Paneer": {
    "category": "Indian",
    "price": 219,
    "rating": 4.7,
    "description": "Paneer cooked with capsicum and spices.",
    "badge": "🌱 Veg",
    "time": 20,
    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800"
},

"Butter Chicken": {
    "category": "Indian",
    "price": 279,
    "rating": 4.9,
    "description": "Tender chicken in creamy butter gravy.",
    "badge": "⭐ Bestseller",
    "time": 25,
    "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=800"
},

"Chicken Tikka Masala": {
    "category": "Indian",
    "price": 289,
    "rating": 4.8,
    "description": "Grilled chicken in rich spiced tomato gravy.",
    "badge": "🔥 Popular",
    "time": 25,
    "image": "https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?w=800"
},

"Butter Naan": {
    "category": "Indian",
    "price": 49,
    "rating": 4.5,
    "description": "Soft naan brushed with butter.",
    "badge": "⭐ Recommended",
    "time": 8,
    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800"
},

"Garlic Naan": {
    "category": "Indian",
    "price": 69,
    "rating": 4.7,
    "description": "Soft naan topped with garlic and herbs.",
    "badge": "🔥 Popular",
    "time": 8,
    "image": "https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=800"
},


# ------------------------- MEXICAN -------------------------

"Veg Tacos": {
    "category": "Mexican",
    "price": 159,
    "rating": 4.5,
    "description": "Crispy tacos filled with vegetables and salsa.",
    "badge": "🌱 Veg",
    "time": 12,
    "image": "https://images.unsplash.com/photo-1552332386-f8dd00dc2f85?w=800"
},

"Chicken Tacos": {
    "category": "Mexican",
    "price": 199,
    "rating": 4.8,
    "description": "Tacos filled with spicy chicken and salsa.",
    "badge": "🔥 Popular",
    "time": 14,
    "image": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=800"
},

"Cheese Nachos": {
    "category": "Mexican",
    "price": 149,
    "rating": 4.6,
    "description": "Crunchy nachos covered with melted cheese.",
    "badge": "🧀 Cheesy",
    "time": 10,
    "image": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?w=800"
},

"Chicken Nachos": {
    "category": "Mexican",
    "price": 219,
    "rating": 4.8,
    "description": "Loaded nachos with chicken and cheese.",
    "badge": "⭐ Bestseller",
    "time": 12,
    "image": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?w=800"
},

"Loaded Nachos": {
    "category": "Mexican",
    "price": 249,
    "rating": 4.9,
    "description": "Nachos loaded with cheese, salsa and toppings.",
    "badge": "🔥 Chef's Choice",
    "time": 12,
    "image": "https://images.unsplash.com/photo-1582169296194-e4d644c48063?w=800"
},


# ------------------------- FAMILY PACKS -------------------------

"Family Pizza Combo": {
    "category": "Family Packs",
    "price": 699,
    "rating": 4.9,
    "description": "2 large pizzas, fries and 4 soft drinks.",
    "badge": "👨‍👩‍👧‍👦 Best Deal",
    "time": 30,
    "image": "https://images.unsplash.com/photo-1579751626657-72bc17010498?w=800"
},

"Family Burger Combo": {
    "category": "Family Packs",
    "price": 599,
    "rating": 4.8,
    "description": "4 burgers, large fries and 4 soft drinks.",
    "badge": "🔥 Best Deal",
    "time": 25,
    "image": "https://images.unsplash.com/photo-1550317138-10000687a72b?w=800"
},

"Biryani Family Pack": {
    "category": "Family Packs",
    "price": 799,
    "rating": 4.9,
    "description": "Large biryani pack with chicken and sides.",
    "badge": "⭐ Bestseller",
    "time": 35,
    "image": "https://images.unsplash.com/photo-1563379091339-03246963d51a?w=800"
},

"Chicken Feast": {
    "category": "Family Packs",
    "price": 999,
    "rating": 4.9,
    "description": "Chicken biryani, wings, fries and drinks.",
    "badge": "🔥 Mega Deal",
    "time": 35,
    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800"
},

"Friends Party Pack": {
    "category": "Family Packs",
    "price": 899,
    "rating": 4.8,
    "description": "Pizza, burgers, fries and drinks for friends.",
    "badge": "🎉 Party Pack",
    "time": 30,
    "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=800"
},

"Mega Family Combo": {
    "category": "Family Packs",
    "price": 1299,
    "rating": 5.0,
    "description": "A huge combo made for the whole family.",
    "badge": "🔥 Mega",
    "time": 40,
    "image": "https://images.unsplash.com/photo-1579751626657-72bc17010498?w=800"
},


# ------------------------- DESSERTS -------------------------

"Chocolate Cake": {
    "category": "Desserts",
    "price": 129,
    "rating": 4.6,
    "description": "Soft chocolate cake with rich chocolate frosting.",
    "badge": "🍫 Popular",
    "time": 5,
    "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800"
},

"Chocolate Brownie": {
    "category": "Desserts",
    "price": 119,
    "rating": 4.7,
    "description": "Warm fudgy chocolate brownie.",
    "badge": "🍫 Bestseller",
    "time": 5,
    "image": "https://images.unsplash.com/photo-1564355808539-22fda35bed7e?w=800"
},

"Brownie With Ice Cream": {
    "category": "Desserts",
    "price": 179,
    "rating": 4.9,
    "description": "Warm brownie served with creamy ice cream.",
    "badge": "⭐ Bestseller",
    "time": 7,
    "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800"
},

"Chocolate Lava Cake": {
    "category": "Desserts",
    "price": 159,
    "rating": 4.9,
    "description": "Warm chocolate cake with molten center.",
    "badge": "🔥 Chef's Choice",
    "time": 8,
    "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=800"
},

"Gulab Jamun": {
    "category": "Desserts",
    "price": 89,
    "rating": 4.5,
    "description": "Soft traditional Indian sweet.",
    "badge": "🇮🇳 Classic",
    "time": 5,
    "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800"
},

"Cheesecake": {
    "category": "Desserts",
    "price": 199,
    "rating": 4.8,
    "description": "Creamy cheesecake with a biscuit base.",
    "badge": "⭐ Premium",
    "time": 5,
    "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=800"
},

"Chocolate Ice Cream": {
    "category": "Desserts",
    "price": 99,
    "rating": 4.6,
    "description": "Creamy chocolate ice cream.",
    "badge": "🍫 Popular",
    "time": 3,
    "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800"
},


# ------------------------- DRINKS -------------------------

"Coca Cola": {
    "category": "Drinks",
    "price": 60,
    "rating": 4.4,
    "description": "Chilled Coca Cola.",
    "badge": "🥤 Cold",
    "time": 2,
    "image": "https://images.unsplash.com/photo-1554866585-cd94860890b7?w=800"
},

"Pepsi": {
    "category": "Drinks",
    "price": 60,
    "rating": 4.4,
    "description": "Chilled Pepsi.",
    "badge": "🥤 Cold",
    "time": 2,
    "image": "https://images.unsplash.com/photo-1629203849820-fdd70d49c38e?w=800"
},

"Fresh Lime Soda": {
    "category": "Drinks",
    "price": 79,
    "rating": 4.6,
    "description": "Refreshing lime soda.",
    "badge": "🍋 Refreshing",
    "time": 5,
    "image": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=800"
},

"Cold Coffee": {
    "category": "Drinks",
    "price": 119,
    "rating": 4.8,
    "description": "Chilled creamy cold coffee.",
    "badge": "⭐ Bestseller",
    "time": 7,
    "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=800"
},

"Chocolate Shake": {
    "category": "Drinks",
    "price": 149,
    "rating": 4.8,
    "description": "Rich chocolate milkshake.",
    "badge": "🍫 Popular",
    "time": 7,
    "image": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=800"
},

"Mango Shake": {
    "category": "Drinks",
    "price": 139,
    "rating": 4.7,
    "description": "Creamy fresh mango shake.",
    "badge": "🥭 Fresh",
    "time": 7,
    "image": "https://images.unsplash.com/photo-1623065422902-30a2d299bbe4?w=800"
},

"Strawberry Shake": {
    "category": "Drinks",
    "price": 149,
    "rating": 4.7,
    "description": "Fresh strawberry milkshake.",
    "badge": "🍓 Fresh",
    "time": 7,
    "image": "https://images.unsplash.com/photo-1553787499-6f0d90304b9c?w=800"
},

"Mojito": {
    "category": "Drinks",
    "price": 129,
    "rating": 4.8,
    "description": "Refreshing mint and lime cooler.",
    "badge": "🌿 Refreshing",
    "time": 6,
    "image": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=800"
},


# ------------------------- HOT DRINKS -------------------------

"Masala Tea": {
    "category": "Hot Drinks",
    "price": 49,
    "rating": 4.5,
    "description": "Indian tea with aromatic spices.",
    "badge": "☕ Classic",
    "time": 5,
    "image": "https://images.unsplash.com/photo-1597318181409-cf64d0d5a5a8?w=800"
},

"Coffee": {
    "category": "Hot Drinks",
    "price": 59,
    "rating": 4.5,
    "description": "Freshly brewed hot coffee.",
    "badge": "☕ Classic",
    "time": 5,
    "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800"
},

"Cappuccino": {
    "category": "Hot Drinks",
    "price": 129,
    "rating": 4.7,
    "description": "Creamy cappuccino with beautiful foam.",
    "badge": "⭐ Premium",
    "time": 7,
    "image": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=800"
},

"Hot Chocolate": {
    "category": "Hot Drinks",
    "price": 139,
    "rating": 4.8,
    "description": "Rich creamy hot chocolate.",
    "badge": "🍫 Popular",
    "time": 7,
    "image": "https://images.unsplash.com/photo-1542990253-0d0f5be5f0ed?w=800"
}

}


# ============================================================
# SESSION STATE
# ============================================================

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "favorites" not in st.session_state:
    st.session_state.favorites = set()

if "bill_generated" not in st.session_state:
    st.session_state.bill_generated = False


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">

<h1>🍔 TASTYBITES</h1>

<p>
GOOD FOOD. GOOD MOOD.
</p>

<p>
Freshly prepared meals • Premium taste • Happy moments
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# TOP INFORMATION
# ============================================================

info1, info2, info3, info4 = st.columns(4)

with info1:
    st.metric("🍽️ Menu Items", len(menu))

with info2:
    st.metric("⭐ Rating", "4.8 / 5")

with info3:
    st.metric("🔥 Popular Items", "25+")

with info4:
    st.metric("🚚 Average Time", "20 min")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("👤 Customer Details")

    customer_name = st.text_input(
        "Customer Name",
        placeholder="Enter customer name"
    )

    phone = st.text_input(
        "Phone Number",
        placeholder="Optional"
    )

    order_type = st.selectbox(
        "Order Type",
        [
            "🍽️ Dine In",
            "🥡 Takeaway"
        ]
    )

    if order_type == "🍽️ Dine In":

        table = st.selectbox(
            "Table Number",
            [f"Table {i}" for i in range(1, 16)]
        )

    else:

        table = "Takeaway"

    st.divider()

    st.header("💳 Payment")

    payment = st.selectbox(
        "Payment Method",
        [
            "💵 Cash",
            "📱 UPI",
            "💳 Credit Card",
            "💳 Debit Card"
        ]
    )

    st.divider()

    st.header("🎟️ Coupon")

    coupon = st.text_input(
        "Coupon Code",
        placeholder="Try TASTY10"
    ).upper().strip()

    if coupon == "TASTY10":

        st.success("🎉 10% discount applied!")

    elif coupon == "WELCOME50":

        st.success("🎉 ₹50 discount applied!")

    elif coupon != "":

        st.error("❌ Invalid coupon")


# ============================================================
# MAIN COLUMNS
# ============================================================

menu_column, cart_column = st.columns(
    [2.2, 1],
    gap="large"
)


# ============================================================
# MENU SECTION
# ============================================================

with menu_column:

    st.markdown(
        '<div class="section-title">🍽️ Explore Our Menu</div>',
        unsafe_allow_html=True
    )

    # Search

    search = st.text_input(
        "🔍 Search for food",
        placeholder="Search pizza, burger, biryani..."
    )

    # Categories

    categories = [
        "All",
        "⭐ Bestsellers",
        "❤️ Favorites",
        "🥗 Starters",
        "🍕 Pizza",
        "🍔 Burgers",
        "🍝 Main Course",
        "🍛 Indian",
        "🌮 Mexican",
        "👨‍👩‍👧‍👦 Family Packs",
        "🍰 Desserts",
        "🥤 Drinks",
        "☕ Hot Drinks"
    ]

    selected_category = st.radio(
        "Categories",
        categories,
        horizontal=True
    )

    # Sorting

    sort_option = st.selectbox(
        "Sort Menu",
        [
            "Recommended",
            "Price: Low to High",
            "Price: High to Low",
            "Rating: High to Low"
        ]
    )

    # ========================================================
    # FILTER MENU
    # ========================================================

    filtered_items = []

    for name, item in menu.items():

        # Search filter

        if search:

            search_text = (
                name
                + " "
                + item["description"]
                + " "
                + item["category"]
            ).lower()

            if search.lower() not in search_text:
                continue

        # Category filter

        if selected_category == "⭐ Bestsellers":

            if "Bestseller" not in item["badge"]:
                continue

        elif selected_category == "❤️ Favorites":

            if name not in st.session_state.favorites:
                continue

        elif selected_category != "All":

            category_map = {
                "🥗 Starters": "Starters",
                "🍕 Pizza": "Pizza",
                "🍔 Burgers": "Burgers",
                "🍝 Main Course": "Main Course",
                "🍛 Indian": "Indian",
                "🌮 Mexican": "Mexican",
                "👨‍👩‍👧‍👦 Family Packs": "Family Packs",
                "🍰 Desserts": "Desserts",
                "🥤 Drinks": "Drinks",
                "☕ Hot Drinks": "Hot Drinks"
            }

            if item["category"] != category_map[selected_category]:
                continue

        filtered_items.append((name, item))


    # ========================================================
    # SORT
    # ========================================================

    if sort_option == "Price: Low to High":

        filtered_items.sort(
            key=lambda x: x[1]["price"]
        )

    elif sort_option == "Price: High to Low":

        filtered_items.sort(
            key=lambda x: x[1]["price"],
            reverse=True
        )

    elif sort_option == "Rating: High to Low":

        filtered_items.sort(
            key=lambda x: x[1]["rating"],
            reverse=True
        )


    # ========================================================
    # RESULT COUNT
    # ========================================================

    st.caption(
        f"Showing {len(filtered_items)} item(s)"
    )


    # ========================================================
    # FOOD CARDS
    # ========================================================

    for i in range(0, len(filtered_items), 2):

        row = filtered_items[i:i + 2]

        columns = st.columns(2)

        for col, (name, item) in zip(columns, row):

            with col:

                # Image

                st.image(
                    item["image"],
                    use_container_width=True
                )

                # Badge

                st.caption(
                    item["badge"]
                )

                # Name

                st.subheader(name)

                # Description

                st.write(
                    item["description"]
                )

                # Rating

                st.write(
                    f"⭐ {item['rating']} / 5  •  "
                    f"⏱️ {item['time']} min"
                )

                # Price

                st.markdown(
                    f"### ₹{item['price']}"
                )

                # Quantity

                quantity = st.number_input(
                    "Quantity",
                    min_value=1,
                    max_value=20,
                    value=1,
                    key=f"quantity_{name}"
                )

                button1, button2 = st.columns(2)

                # Favorite

                with button1:

                    if name in st.session_state.favorites:

                        favorite_text = "❤️ Saved"

                    else:

                        favorite_text = "♡ Favorite"

                    if st.button(
                        favorite_text,
                        key=f"favorite_{name}",
                        use_container_width=True
                    ):

                        if name in st.session_state.favorites:

                            st.session_state.favorites.remove(name)

                        else:

                            st.session_state.favorites.add(name)

                        st.rerun()

                # Add to cart

                with button2:

                    if st.button(
                        "🛒 Add",
                        key=f"add_{name}",
                        use_container_width=True,
                        type="primary"
                    ):

                        if name in st.session_state.cart:

                            st.session_state.cart[name] += quantity

                        else:

                            st.session_state.cart[name] = quantity

                        st.session_state.bill_generated = False

                        st.toast(
                            f"✅ {name} added to cart!"
                        )

                        st.rerun()

                st.divider()


# ============================================================
# CART SECTION
# ============================================================

with cart_column:

    st.markdown(
        '<div class="cart-box">',
        unsafe_allow_html=True
    )

    st.subheader("🛒 Your Cart")

    if len(st.session_state.cart) == 0:

        st.info(
            "Your cart is empty.\n\n"
            "Add delicious food from the menu!"
        )

    else:

        subtotal = 0
        total_items = 0

        # ====================================================
        # CART ITEMS
        # ====================================================

        for item_name in list(st.session_state.cart.keys()):

            quantity = st.session_state.cart[item_name]

            price = menu[item_name]["price"]

            item_total = quantity * price

            subtotal += item_total

            total_items += quantity

            st.write(
                f"**{item_name}**"
            )

            st.caption(
                f"₹{price} × {quantity} = ₹{item_total}"
            )

            c1, c2, c3 = st.columns(3)

            # Minus

            with c1:

                if st.button(
                    "➖",
                    key=f"minus_{item_name}"
                ):

                    st.session_state.cart[item_name] -= 1

                    if st.session_state.cart[item_name] <= 0:

                        del st.session_state.cart[item_name]

                    st.rerun()

            # Quantity

            with c2:

                st.write(
                    f"**{quantity}**"
                )

            # Plus

            with c3:

                if st.button(
                    "➕",
                    key=f"plus_{item_name}"
                ):

                    st.session_state.cart[item_name] += 1

                    st.rerun()

            if st.button(
                "🗑️ Remove",
                key=f"remove_{item_name}"
            ):

                del st.session_state.cart[item_name]

                st.rerun()

            st.divider()


        # ====================================================
        # COUPON CALCULATION
        # ====================================================

        coupon_discount = 0

        if coupon == "TASTY10":

            coupon_discount = subtotal * 0.10

        elif coupon == "WELCOME50":

            coupon_discount = min(50, subtotal)


        # Discount

        discount = st.number_input(
            "Extra Discount (%)",
            min_value=0,
            max_value=30,
            value=0
        )

        manual_discount = (
            subtotal
            * discount
            / 100
        )


        # ====================================================
        # TOTAL CALCULATIONS
        # ====================================================

        total_discount = (
            coupon_discount
            + manual_discount
        )

        after_discount = (
            subtotal
            - total_discount
        )

        # GST

        gst = after_discount * 0.05

        # Service charge

        service_charge = after_discount * 0.02

        # Grand total

        grand_total = (
            after_discount
            + gst
            + service_charge
        )


        # ====================================================
        # CART SUMMARY
        # ====================================================

        st.write(
            f"Items: **{total_items}**"
        )

        st.write(
            f"Subtotal: **₹{subtotal:.2f}**"
        )

        if coupon_discount > 0:

            st.write(
                f"Coupon Discount: **-₹{coupon_discount:.2f}**"
            )

        if manual_discount > 0:

            st.write(
                f"Extra Discount: **-₹{manual_discount:.2f}**"
            )

        st.write(
            f"GST (5%): **₹{gst:.2f}**"
        )

        st.write(
            f"Service Charge (2%): **₹{service_charge:.2f}**"
        )


        # ====================================================
        # GRAND TOTAL
        # ====================================================

        st.markdown(
            f"""
<div class="total-box">

<h1>₹{grand_total:.2f}</h1>

<p>GRAND TOTAL</p>

</div>
""",
            unsafe_allow_html=True
        )


        st.write("")


        # ====================================================
        # CHECKOUT BUTTON
        # ====================================================

        if st.button(
            "🧾 CHECKOUT & GENERATE BILL",
            use_container_width=True,
            type="primary"
        ):

            st.session_state.bill_generated = True

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# ============================================================
# FINAL BILL
# ============================================================

if st.session_state.bill_generated:

    st.divider()

    st.header("🧾 Your Order Invoice")

    # Order number

    order_number = (
        "TB"
        + datetime.now().strftime("%Y%m%d")
        + "-"
        + str(random.randint(1000, 9999))
    )

    current_time = datetime.now().strftime(
        "%d %B %Y • %I:%M %p"
    )


    # ========================================================
    # PREPARATION TIME
    # ========================================================

    preparation_times = []

    for item_name in st.session_state.cart:

        preparation_times.append(
            menu[item_name]["time"]
        )

    if preparation_times:

        estimated_time = max(preparation_times) + 10

    else:

        estimated_time = 20


    # ========================================================
    # CUSTOMER NAME
    # ========================================================

    if customer_name.strip():

        display_name = customer_name.strip()

    else:

        display_name = "Walk-in Customer"


    # ========================================================
    # INVOICE HEADER
    # ========================================================

    st.markdown(
        f"""
## 🍔 TASTYBITES RESTAURANT

**Order ID:** `{order_number}`

**Customer:** {display_name}

**Phone:** {phone if phone else "Not provided"}

**Order Type:** {order_type}

**Table:** {table}

**Payment:** {payment}

**Date:** {current_time}

---

### ⏱️ Estimated Preparation Time

## {estimated_time} minutes

---
"""
    )


    # ========================================================
    # BILL TABLE
    # ========================================================

    bill_data = []

    for item_name, quantity in st.session_state.cart.items():

        price = menu[item_name]["price"]

        item_total = price * quantity

        bill_data.append(
            {
                "Food Item": item_name,
                "Qty": quantity,
                "Price": f"₹{price:.2f}",
                "Total": f"₹{item_total:.2f}"
            }
        )

    st.table(bill_data)


    # ========================================================
    # FINAL CALCULATION
    # ========================================================

    final_subtotal = sum(
        menu[item]["price"] * quantity
        for item, quantity
        in st.session_state.cart.items()
    )

    final_coupon_discount = 0

    if coupon == "TASTY10":

        final_coupon_discount = (
            final_subtotal * 0.10
        )

    elif coupon == "WELCOME50":

        final_coupon_discount = min(
            50,
            final_subtotal
        )


    final_manual_discount = (
        final_subtotal
        * discount
        / 100
    )

    final_discount = (
        final_coupon_discount
        + final_manual_discount
    )

    final_after_discount = (
        final_subtotal
        - final_discount
    )

    final_gst = (
        final_after_discount * 0.05
    )

    final_service = (
        final_after_discount * 0.02
    )

    final_total = (
        final_after_discount
        + final_gst
        + final_service
    )


    # ========================================================
    # BILL SUMMARY
    # ========================================================

    left, right = st.columns(2)

    with left:

        st.write("Subtotal")
        st.write("Discount")
        st.write("GST")
        st.write("Service Charge")

    with right:

        st.write(
            f"₹{final_subtotal:.2f}"
        )

        st.write(
            f"- ₹{final_discount:.2f}"
        )

        st.write(
            f"₹{final_gst:.2f}"
        )

        st.write(
            f"₹{final_service:.2f}"
        )


    st.divider()


    # ========================================================
    # GRAND TOTAL
    # ========================================================

    st.markdown(
        f"""
# 💰 GRAND TOTAL: ₹{final_total:.2f}
"""
    )


    st.success(
        f"🎉 Order {order_number} has been successfully placed!"
    )


    st.info(
        f"👨‍🍳 Your food should be ready in approximately "
        f"{estimated_time} minutes."
    )


    st.balloons()


    # ========================================================
    # THANK YOU
    # ========================================================

    st.markdown(
        """
---

# 🙏 Thank You for Choosing TastyBites!

### 🍔 Fresh Food • Great Taste • Happy Moments

We hope to see you again soon! ❤️

---
"""
    )


    # ========================================================
    # NEW ORDER
    # ========================================================

    if st.button(
        "🔄 Start New Order",
        use_container_width=True
    ):

        st.session_state.cart = {}

        st.session_state.bill_generated = False

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">

<h3>🍔 TASTYBITES RESTAURANT</h3>

Fresh Food • Great Taste • Happy Moments

<br><br>

⭐ Rated 4.8/5 by our customers

<br>

© 2026 TastyBites Restaurant POS

</div>
""",
    unsafe_allow_html=True
)