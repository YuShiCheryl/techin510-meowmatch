import streamlit as st
from PIL import Image
import numpy as np
from session_utils import init_session_state, get_user_profile, get_pet_display_info, get_profile_avatar_html

# Set page configuration
st.set_page_config(
    page_title="MeowMatch - Search by Ingredient",
    page_icon="M",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add hidden navigation bar CSS
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Create placeholder images using PIL
def create_placeholder_image(width, height, color):
    img = Image.new('RGB', (width, height), color)
    return img

# Create sample images for products
product_image1 = create_placeholder_image(300, 300, '#FFE6E6')
product_image2 = create_placeholder_image(300, 300, '#FFCCD5')
product_image3 = create_placeholder_image(300, 300, '#FFD6E0')

# Add custom CSS for styling
st.markdown("""
<style>
    /* Base styles */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide the default Streamlit menu button */
    #MainMenu {
        visibility: hidden;
    }
    
    /* Main background and container styling */
    .stApp {
        background-color: #FFFAF9;
    }
    
    /* Main content container */
    .main .block-container {
        background-color: #FFFAF9;
        padding: 3rem;
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    /* Profile avatar container */
    .profile-container {
        position: fixed;
        top: 2.5rem;
        right: 2rem;
        z-index: 1001;
        padding: 0.5rem;
    }
    
    .profile-avatar {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        border: 2px solid #FF6B95;
        background-color: #FFE0E6;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        box-shadow: 0 3px 10px rgba(255, 107, 149, 0.2);
        overflow: hidden;
    }
    
    .profile-avatar:hover {
        transform: scale(1.08);
        box-shadow: 0 5px 15px rgba(255, 107, 149, 0.3);
    }
    
    .profile-icon {
        font-size: 24px;
        color: #FF6B95;
    }
    
    .profile-avatar img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }
    
    /* Title styling */
    .main-title {
        color: #444444;
        font-size: 3rem;
        font-weight: 800;
        text-align: left;
        margin-bottom: 1.5rem;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
    }
    
    .subtitle {
        color: #666666;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 2.5rem;
        position: relative;
        z-index: 1;
        line-height: 1.7;
    }
    
    /* Search container */
    .search-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF5F7 100%);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(255, 107, 149, 0.1);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 107, 149, 0.1);
    }
    
    .search-container::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 150px;
        height: 150px;
        background: linear-gradient(45deg, transparent 50%, rgba(255, 107, 149, 0.05) 50%);
        border-radius: 0 0 0 100%;
    }
    
    /* Filter section styling */
    .filter-section {
        margin-bottom: 2rem;
    }
    
    .filter-title {
        color: #444444;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    /* Input fields styling */
    .stTextInput > div > div > input {
        border-radius: 30px !important;
        border: 1px solid rgba(255, 107, 149, 0.3) !important;
        padding: 0.75rem 1.5rem !important;
        box-shadow: 0 4px 15px rgba(255, 107, 149, 0.05) !important;
        transition: all 0.3s ease !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border: 1px solid rgba(255, 107, 149, 0.8) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 149, 0.1) !important;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div > div {
        border-radius: 30px !important;
        border: 1px solid rgba(255, 107, 149, 0.3) !important;
        padding: 0.3rem 1.5rem !important;
        box-shadow: 0 4px 15px rgba(255, 107, 149, 0.05) !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox > div > div > div:focus {
        border: 1px solid rgba(255, 107, 149, 0.8) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 149, 0.1) !important;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.7rem 2.5rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 15px rgba(255, 107, 149, 0.2) !important;
        letter-spacing: 0.5px !important;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(255, 107, 149, 0.3) !important;
    }
    
    /* Results section */
    .results-container {
        margin-top: 3rem;
    }
    
    .results-title {
        color: #444444;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        position: relative;
        display: inline-block;
        padding-bottom: 0.5rem;
    }
    
    .results-title::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        border-radius: 2px;
    }
    
    /* Product card styling */
    .product-card {
        background: #FFFFFF;
        padding: 1.8rem;
        border-radius: 18px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.08);
        border: 1px solid rgba(255, 107, 149, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .product-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.4s ease;
    }
    
    .product-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(255, 107, 149, 0.12);
    }
    
    .product-card:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }
    
    .product-info {
        display: flex;
        align-items: flex-start;
    }
    
    .product-image {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(255, 107, 149, 0.1);
        margin-right: 1.5rem;
        transition: all 0.4s ease;
        flex: 0 0 120px;
    }
    
    .product-details {
        flex: 1;
    }
    
    .product-title {
        color: #444444;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }
    
    .product-description {
        color: #666666;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .product-price {
        color: #FF6B95;
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 0.5px;
    }
    
    .product-taste {
        display: inline-block;
        background: rgba(255, 107, 149, 0.1);
        color: #FF6B95;
        font-size: 0.85rem;
        font-weight: 600;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        margin-right: 0.8rem;
        margin-bottom: 0.8rem;
    }
    
    .product-ingredients {
        color: #666666;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }
    
    .highlight {
        background-color: rgba(255, 107, 149, 0.2);
        padding: 0 0.3rem;
        border-radius: 3px;
        color: #FF6B95;
        font-weight: 600;
    }
    
    /* Filter chips */
    .filter-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin: 1.5rem 0;
    }
    
    .filter-chip {
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        color: white;
        font-size: 0.9rem;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
        border-radius: 30px;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 4px 10px rgba(255, 107, 149, 0.2);
    }
    
    .chip-remove {
        background-color: rgba(255, 255, 255, 0.3);
        width: 18px;
        height: 18px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .chip-remove:hover {
        background-color: rgba(255, 255, 255, 0.5);
    }
    
    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 3rem;
        color: #666666;
    }
    
    .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: rgba(255, 107, 149, 0.3);
    }
    
    .empty-state-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #444444;
    }
    
    .empty-state-text {
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    /* Animation for elements */
    .fade-in {
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Section headings */
    h2, h3 {
        color: #444444 !important;
        font-weight: 700 !important;
    }
    
    /* Cart button */
    .cart-button {
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.5rem 1.3rem !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 107, 149, 0.15) !important;
        margin-top: 0.8rem !important;
    }
    
    .cart-button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(255, 107, 149, 0.2) !important;
    }
    
    /* Back button */
    .back-button {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #666666;
        text-decoration: none;
        margin-bottom: 2rem;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .back-button:hover {
        color: #FF6B95;
        transform: translateX(-3px);
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background-color: #FF6B95 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state and display dynamic avatar
init_session_state()
st.markdown(get_profile_avatar_html(), unsafe_allow_html=True)

# Back button
st.markdown("""
<a href="/" class="back-button" target="_self">
    <span>←</span> Back to Home
</a>
""", unsafe_allow_html=True)

# Page title
st.markdown('<h1 class="main-title fade-in">Search Cat Food by Ingredient</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle fade-in">Find the perfect nutrition for your cat by searching specific ingredients or flavors.</p>', unsafe_allow_html=True)

# Search container
st.markdown('<div class="search-container fade-in">', unsafe_allow_html=True)

# Create 2 columns for filters
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    st.markdown('<div class="filter-title">Filter by Ingredient</div>', unsafe_allow_html=True)
    ingredient = st.text_input('', placeholder='E.g., Chicken, Fish, Rice...')
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    st.markdown('<div class="filter-title">Filter by Taste</div>', unsafe_allow_html=True)
    taste = st.selectbox('', ['All Tastes', 'Sweet', 'Sour', 'Bitter', 'Salty', 'Umami'])
    st.markdown('</div>', unsafe_allow_html=True)

# Additional filters (expandable)
with st.expander("Advanced Filters"):
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    
    # Age filter
    st.markdown('<div class="filter-title">Cat Age</div>', unsafe_allow_html=True)
    age = st.selectbox('', ['All Ages', 'Kitten (0-1 year)', 'Adult (1-7 years)', 'Senior (7+ years)'])
    
    # Health condition
    st.markdown('<div class="filter-title">Health Condition</div>', unsafe_allow_html=True)
    health = st.multiselect('', ['Weight Management', 'Sensitive Digestion', 'Hairball Control', 'Urinary Health', 'Joint Health'])
    
    # Price range
    st.markdown('<div class="filter-title">Price Range</div>', unsafe_allow_html=True)
    price_range = st.slider('', 0, 100, (20, 50), format="$%d")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Search button
search_btn = st.button('Search')

st.markdown('</div>', unsafe_allow_html=True)

# Display active filters if any
if ingredient or taste != 'All Tastes' or (age != 'All Ages' and age) or health or price_range != (20, 50):
    st.markdown('<div class="filter-chips fade-in">', unsafe_allow_html=True)
    
    if ingredient:
        st.markdown(f"""
        <div class="filter-chip">
            Ingredient: {ingredient}
            <span class="chip-remove">×</span>
        </div>
        """, unsafe_allow_html=True)
    
    if taste != 'All Tastes':
        st.markdown(f"""
        <div class="filter-chip">
            Taste: {taste}
            <span class="chip-remove">×</span>
        </div>
        """, unsafe_allow_html=True)
    
    if age != 'All Ages' and age:
        st.markdown(f"""
        <div class="filter-chip">
            Age: {age}
            <span class="chip-remove">×</span>
        </div>
        """, unsafe_allow_html=True)
    
    for h in health:
        st.markdown(f"""
        <div class="filter-chip">
            {h}
            <span class="chip-remove">×</span>
        </div>
        """, unsafe_allow_html=True)
    
    if price_range != (20, 50):
        st.markdown(f"""
        <div class="filter-chip">
            Price: ${price_range[0]} - ${price_range[1]}
            <span class="chip-remove">×</span>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# Display search results
st.markdown('<div class="results-container">', unsafe_allow_html=True)

# Results header
if ingredient or taste != 'All Tastes' or (age != 'All Ages' and age) or health or price_range != (20, 50):
    st.markdown('<div class="results-title">Search Results</div>', unsafe_allow_html=True)
    
    # Sample product data - this would come from your database in a real app
    sample_products = [
        {
            "name": "Premium Chicken Recipe",
            "description": "A balanced meal with real chicken as the first ingredient",
            "price": "$24.99",
            "image": product_image1,
            "taste": "Umami",
            "ingredients": "Chicken, Brown Rice, Carrots, Peas",
            "search_term": "Chicken"
        },
        {
            "name": "Ocean Fish & Vegetable Mix",
            "description": "Wild-caught fish with a blend of nutritious vegetables",
            "price": "$26.99",
            "image": product_image2,
            "taste": "Salty",
            "ingredients": "Salmon, Cod, Spinach, Sweet Potatoes",
            "search_term": "Fish"
        },
        {
            "name": "Grain-Free Turkey Formula",
            "description": "Grain-free recipe ideal for cats with sensitive digestion",
            "price": "$29.99",
            "image": product_image3,
            "taste": "Umami",
            "ingredients": "Turkey, Potato, Green Beans, Cranberries",
            "search_term": "Turkey"
        }
    ]
    
    # Filter products based on search criteria
    filtered_products = []
    
    # For demo purposes - in reality, you would query your database
    if ingredient:
        ingredient_lower = ingredient.lower()
        for product in sample_products:
            if ingredient_lower in product["ingredients"].lower() or ingredient_lower in product["name"].lower():
                filtered_products.append(product)
    elif taste != 'All Tastes':
        for product in sample_products:
            if product["taste"] == taste:
                filtered_products.append(product)
    else:
        filtered_products = sample_products
    
    # Display results
    if filtered_products:
        for product in filtered_products:
            highlighted_ingredients = product["ingredients"]
            if ingredient:
                # Highlight the search term in ingredients
                highlighted_ingredients = product["ingredients"].replace(
                    ingredient, f'<span class="highlight">{ingredient}</span>'
                ) if ingredient.lower() in product["ingredients"].lower() else product["ingredients"]
            
            st.markdown(f"""
            <div class="product-card fade-in">
                <div class="product-info">
                    <div class="product-image">
                        <img src="data:image/png;base64,{product_image1}" width="120">
                    </div>
                    <div class="product-details">
                        <div class="product-title">{product["name"]}</div>
                        <div class="product-description">{product["description"]}</div>
                        <div class="product-taste">{product["taste"]}</div>
                        <div class="product-ingredients"><strong>Ingredients:</strong> {highlighted_ingredients}</div>
                        <div class="product-price">{product["price"]}</div>
                        <button class="cart-button">Add to Cart</button>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        # No results found
        st.markdown("""
        <div class="empty-state fade-in">
            <div class="empty-state-icon">🔍</div>
            <div class="empty-state-title">No products found</div>
            <div class="empty-state-text">Try adjusting your search filters or try a different ingredient.</div>
        </div>
        """, unsafe_allow_html=True)
else:
    # Initial state before search
    st.markdown("""
    <div class="empty-state fade-in">
        <div class="empty-state-icon">🔍</div>
        <div class="empty-state-title">Find the perfect food for your cat</div>
        <div class="empty-state-text">Enter an ingredient or select a taste preference to start your search.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)