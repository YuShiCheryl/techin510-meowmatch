import streamlit as st
from PIL import Image
import numpy as np
from utils.session_utils import init_session_state, get_user_profile, get_pet_display_info, get_profile_avatar_html

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

# Create sample images for products - 改为橙色系
product_image1 = create_placeholder_image(300, 300, '#FFE5D4')
product_image2 = create_placeholder_image(300, 300, '#FFEAD6')
product_image3 = create_placeholder_image(300, 300, '#FFF0E6')

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
        background-color: #FFFBF7;
    }
    
    /* Main content container */
    .main .block-container {
        background-color: #FFFBF7;
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
        border: 2px solid #FF8C42;
        background-color: #FFE5D4;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        box-shadow: 0 3px 10px rgba(255, 140, 66, 0.2);
        overflow: hidden;
    }
    
    .profile-avatar:hover {
        transform: scale(1.08);
        box-shadow: 0 5px 15px rgba(255, 140, 66, 0.3);
    }
    
    .profile-icon {
        font-size: 24px;
        color: #FF8C42;
    }
    
    .profile-avatar img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }
    
    /* Back button styling for Streamlit */
    .back-button-streamlit .stButton button {
        background: transparent !important;
        color: #666666 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        box-shadow: none !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 0.5rem !important;
    }

    .back-button-streamlit .stButton button:hover {
        color: #FF8C42 !important;
        transform: translateX(-3px) !important;
        background: rgba(255, 140, 66, 0.05) !important;
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
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
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
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF8F3 100%);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(255, 140, 66, 0.1);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 140, 66, 0.1);
    }
    
    .search-container::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 150px;
        height: 150px;
        background: linear-gradient(45deg, transparent 50%, rgba(255, 140, 66, 0.05) 50%);
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
        border: 1px solid rgba(255, 140, 66, 0.3) !important;
        padding: 0.75rem 1.5rem !important;
        box-shadow: 0 4px 15px rgba(255, 140, 66, 0.05) !important;
        transition: all 0.3s ease !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border: 1px solid rgba(255, 140, 66, 0.8) !important;
        box-shadow: 0 6px 20px rgba(255, 140, 66, 0.1) !important;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div > div {
        border-radius: 30px !important;
        border: 1px solid rgba(255, 140, 66, 0.3) !important;
        padding: 0.3rem 1.5rem !important;
        box-shadow: 0 4px 15px rgba(255, 140, 66, 0.05) !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox > div > div > div:focus {
        border: 1px solid rgba(255, 140, 66, 0.8) !important;
        box-shadow: 0 6px 20px rgba(255, 140, 66, 0.1) !important;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.7rem 2.5rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 15px rgba(255, 140, 66, 0.2) !important;
        letter-spacing: 0.5px !important;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(255, 140, 66, 0.3) !important;
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
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        border-radius: 2px;
    }
    
    /* Product card styling */
    .product-card {
        background: #FFFFFF;
        padding: 1.8rem;
        border-radius: 18px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(255, 140, 66, 0.08);
        border: 1px solid rgba(255, 140, 66, 0.1);
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
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.4s ease;
    }
    
    .product-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(255, 140, 66, 0.12);
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
        box-shadow: 0 5px 15px rgba(255, 140, 66, 0.1);
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
        color: #FF8C42;
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 0.5px;
    }
    
    .product-taste {
        display: inline-block;
        background: rgba(255, 140, 66, 0.1);
        color: #FF8C42;
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
        background-color: rgba(255, 140, 66, 0.2);
        padding: 0 0.3rem;
        border-radius: 3px;
        color: #FF8C42;
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
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        color: white;
        font-size: 0.9rem;
        font-weight: 600;
        padding: 0.5rem 1.2rem;
        border-radius: 30px;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 4px 10px rgba(255, 140, 66, 0.2);
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
        color: rgba(255, 140, 66, 0.3);
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
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.5rem 1.3rem !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 140, 66, 0.15) !important;
        margin-top: 0.8rem !important;
    }
    
    .cart-button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(255, 140, 66, 0.2) !important;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background-color: #FF8C42 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state and display dynamic avatar
init_session_state()
st.markdown(get_profile_avatar_html(), unsafe_allow_html=True)

# Back button - 改为Streamlit按钮
st.markdown('<div class="back-button-streamlit">', unsafe_allow_html=True)
if st.button("← Back to Home", key="back_home"):
    st.switch_page("app.py")
st.markdown('</div>', unsafe_allow_html=True)

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
    st.markdown('<div class="filter-title">Filter by Texture</div>', unsafe_allow_html=True)
    texture = st.selectbox('', ['All Textures', 'Pate', 'Gravy', 'Broth', 'Shreds', 'Chunks', 'Pellets'])
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
if ingredient or texture != 'All Textures' or (age != 'All Ages' and age) or health or price_range != (20, 50):
    st.markdown('<div class="filter-chips fade-in">', unsafe_allow_html=True)
    
    if ingredient:
        st.markdown(f"""
        <div class="filter-chip">
            Ingredient: {ingredient}
            <span class="chip-remove">×</span>
        </div>
        """, unsafe_allow_html=True)
    
    if texture != 'All Textures':
        st.markdown(f"""
        <div class="filter-chip">
            Texture: {texture}
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
if ingredient or texture != 'All Textures' or (age != 'All Ages' and age) or health or price_range != (20, 50):
    st.markdown('<div class="results-title">Search Results</div>', unsafe_allow_html=True)
    
    # Sample product data - this would come from your database in a real app
    sample_products = [
        {
            "name": "ZIWI Peak Lamb Recipe",
            "image": "data/images/products/ZIWI Peak Lamb Recipe.jpg",
            "price": 55.44,
            "price_per_oz": 0.71,
            "oz": 78,
            "food_type": "wet",
            "protein_content": 0.43,
            "fat_content": 0.31,
            "moisture_content": 0.745,
            "kcalories_per_oz": 37.69,
            "protein_sources": "Lamb Recipe",
            "ingredients": "Lamb, Lamb Lung, Lamb Kidney, Lamb Liver, Chickpeas, Lamb Tripe, Lamb Heart, New Zealand Green Mussel",
            "description": "Premium wet food with lamb as main protein source and high moisture content.",
            "match_score": 96,
            "rating": 4.9,
            "reviews": 234,
            "tags": ["Premium", "High Protein", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult", "Senior"],
            "flavors": ["Lamb"],
            "diet_type": "All Types",
            "texture": "Pate",
            "budget_category": "luxury"
        },
        {
            "name": "ZIWI Peak Chicken Recipe",
            "image": "data/images/products/ZIWI Peak Chicken Recipe.jpg",
            "price": 55.44,
            "price_per_oz": 0.71,
            "oz": 78,
            "food_type": "wet",
            "protein_content": 0.46,
            "fat_content": 0.31,
            "moisture_content": 0.74,
            "kcalories_per_oz": 37.69,
            "protein_sources": "Chicken Recipe",
            "ingredients": "Chicken, Chicken Liver, Chicken Heart, Chick Peas, New Zealand Green Mussel, Chicken Bone, Dried Kelp",
            "description": "Premium wet food with chicken as main protein source and high moisture content.",
            "match_score": 94,
            "rating": 4.8,
            "reviews": 198,
            "tags": ["Premium", "High Protein", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult", "Kitten"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Pate",
            "budget_category": "luxury"
        },
        {
            "name": "ZIWI Peak Beef Recipe",
            "image": "data/images/products/ZIWI Peak Beef Recipe.jpg",
            "price": 55.44,
            "price_per_oz": 0.71,
            "oz": 78,
            "food_type": "wet",
            "protein_content": 0.45,
            "fat_content": 0.29,
            "moisture_content": 0.755,
            "kcalories_per_oz": 35.54,
            "protein_sources": "Beef Recipe",
            "ingredients": "Beef, Beef Lung, Beef Kidney, Beef Tripe, Beef Liver, Chickpeas, New Zealand Green Mussel, Beef Bone",
            "description": "Premium wet food with beef as main protein source and high moisture content.",
            "match_score": 91,
            "rating": 4.7,
            "reviews": 156,
            "tags": ["Premium", "High Protein", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Beef"],
            "diet_type": "All Types",
            "texture": "Pate",
            "budget_category": "luxury"
        },
        {
            "name": "ZIWI Peak Rabbit Lamb Recipe",
            "image": "data/images/products/ZIWI Peak Rabbit Lamb Recipe.jpg",
            "price": 76.72,
            "price_per_oz": 0.98,
            "oz": 78,
            "food_type": "wet",
            "protein_content": 0.54,
            "fat_content": 0.21,
            "moisture_content": 0.76,
            "kcalories_per_oz": 31.23,
            "protein_sources": "Rabbit & Lamb",
            "ingredients": "Rabbit Meat, Lamb, Lamb Lung, Lamb Liver, Chickpea, Lamb Kidney, Hare Meat, Lamb Tripe, Lamb Heart",
            "description": "Ultra-premium wet food with rabbit and lamb, ideal for sensitive digestion.",
            "match_score": 88,
            "rating": 4.9,
            "reviews": 89,
            "tags": ["Ultra Premium", "Very High Protein", "Sensitive Digestion", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Rabbit", "Lamb"],
            "diet_type": "Sensitive Digestion",
            "texture": "Pate",
            "budget_category": "luxury"
        },
        {
            "name": "Tiki Cat After Dark Chicken Recipe",
            "image": "data/images/products/Tiki Cat After Dark Chicken Recipe.jpg",
            "price": 27.12,
            "price_per_oz": 0.57,
            "oz": 48,
            "food_type": "wet",
            "protein_content": 0.17,
            "fat_content": 0.02,
            "moisture_content": 0.8,
            "kcalories_per_oz": 18.75,
            "protein_sources": "Chicken Recipe",
            "ingredients": "Chicken, Chicken Broth, Sunflower Oil, Natural Flavor, Tricalcium Phosphate, Potassium Chloride",
            "description": "Natural wet food with real chicken and very high moisture content.",
            "match_score": 85,
            "rating": 4.6,
            "reviews": 423,
            "tags": ["Natural", "High Moisture", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Chunks",
            "budget_category": "premium"
        },
        {
            "name": "Tiki Cat Luau Wild Salmon",
            "image": "data/images/products/Tiki Cat Luau Wild Salmon.jpg",
            "price": 26.32,
            "price_per_oz": 0.55,
            "oz": 48,
            "food_type": "wet",
            "protein_content": 0.15,
            "fat_content": 0.01,
            "moisture_content": 0.83,
            "kcalories_per_oz": 16.25,
            "protein_sources": "Wild Salmon",
            "ingredients": "Salmon, Fish Broth, Sunflower Oil, Natural Flavor, Tricalcium Phosphate, Potassium Chloride",
            "description": "Wild salmon recipe with extremely high moisture content for optimal hydration.",
            "match_score": 82,
            "rating": 4.5,
            "reviews": 367,
            "tags": ["Wild Caught", "Very High Moisture", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Fish"],
            "diet_type": "All Types",
            "texture": "Chunks",
            "budget_category": "premium"
        },
        {
            "name": "Purina ONE Beef Recipe Pate",
            "image": "data/images/products/Purina ONE Beef Recipe Pate.jpg",
            "price": 23.85,
            "price_per_oz": 0.33,
            "oz": 72,
            "food_type": "wet",
            "protein_content": 0.11,
            "fat_content": 0.05,
            "moisture_content": 0.78,
            "kcalories_per_oz": 29.17,
            "protein_sources": "Beef",
            "ingredients": "Beef, Beef Broth, Liver, Meat By-Products, Wheat Gluten, Artificial and Natural Flavors",
            "description": "Affordable beef pate with good moisture content for everyday feeding.",
            "match_score": 78,
            "rating": 4.2,
            "reviews": 512,
            "tags": ["Affordable", "High Moisture", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Beef"],
            "diet_type": "All Types",
            "texture": "Pate",
            "budget_category": "mid-range"
        },
        {
            "name": "Purina ONE Natural Chicken in Gravy",
            "image": "data/images/products/Purina ONE Natural Chicken in Gravy.jpg",
            "price": 22.73,
            "price_per_oz": 0.32,
            "oz": 72,
            "food_type": "wet",
            "protein_content": 0.12,
            "fat_content": 0.02,
            "moisture_content": 0.82,
            "kcalories_per_oz": 22.92,
            "protein_sources": "Chicken",
            "ingredients": "Chicken, Chicken Broth, Liver, Wheat Gluten, Meat By-Products, Modified Corn Starch",
            "description": "Natural chicken in gravy with very high moisture content for hydration.",
            "match_score": 75,
            "rating": 4.1,
            "reviews": 678,
            "tags": ["Natural", "Very High Moisture", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Gravy",
            "budget_category": "mid-range"
        },
        {
            "name": "Nacho Cage Free Chicken Recipe",
            "image": "data/images/products/Nacho Cage Free Chicken Recipe.jpg",
            "price": 18.99,
            "price_per_oz": 0.26,
            "oz": 72,
            "food_type": "wet",
            "protein_content": 0.10,
            "fat_content": 0.06,
            "moisture_content": 0.82,
            "kcalories_per_oz": 27.08,
            "protein_sources": "Chicken",
            "ingredients": "Chicken, Chicken Broth, Natural Flavor, Guar Gum, Potassium Chloride, Salt",
            "description": "Cage-free chicken with high moisture content, budget-friendly option.",
            "match_score": 73,
            "rating": 4.0,
            "reviews": 445,
            "tags": ["Cage Free", "High Moisture", "Budget Friendly", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Chunks",
            "budget_category": "budget"
        },
        {
            "name": "Nacho Sustainably Caught Salmon Recipe",
            "image": "data/images/products/Nacho Sustainably Caught Salmon Recipe.jpg",
            "price": 18.99,
            "price_per_oz": 0.26,
            "oz": 72,
            "food_type": "wet",
            "protein_content": 0.11,
            "fat_content": 0.04,
            "moisture_content": 0.83,
            "kcalories_per_oz": 25.0,
            "protein_sources": "Salmon",
            "ingredients": "Salmon, Fish Broth, Natural Flavor, Guar Gum, Potassium Chloride, Salt",
            "description": "Sustainably caught salmon with very high moisture content, budget-friendly.",
            "match_score": 70,
            "rating": 4.1,
            "reviews": 356,
            "tags": ["Sustainable", "Very High Moisture", "Budget Friendly", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Fish"],
            "diet_type": "All Types",
            "texture": "Chunks",
            "budget_category": "budget"
        },
        {
            "name": "Fancy Feast Gourmet Naturals Beef Recipe",
            "image": "data/images/products/Fancy Feast Gourmet Naturals Beef Recipe.jpg",
            "price": 10.37,
            "price_per_oz": 0.14,
            "oz": 72,
            "food_type": "wet",
            "protein_content": 0.08,
            "fat_content": 0.05,
            "moisture_content": 0.78,
            "kcalories_per_oz": 29.17,
            "protein_sources": "Beef",
            "ingredients": "Beef, Beef Broth, Liver, Wheat Gluten, Meat By-Products, Natural Flavors",
            "description": "Budget-friendly beef recipe with good moisture content for everyday feeding.",
            "match_score": 68,
            "rating": 4.0,
            "reviews": 892,
            "tags": ["Budget Friendly", "Gourmet", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Beef"],
            "diet_type": "All Types",
            "texture": "Pate",
            "budget_category": "budget"
        },
        {
            "name": "Fancy Feast Gourmet Naturals White Meat Chicken Recipe",
            "image": "data/images/products/Fancy Feast Gourmet Naturals White Meat Chicken Recipe.jpg",
            "price": 11.53,
            "price_per_oz": 0.16,
            "oz": 72,
            "food_type": "wet",
            "protein_content": 0.12,
            "fat_content": 0.02,
            "moisture_content": 0.82,
            "kcalories_per_oz": 22.92,
            "protein_sources": "Chicken",
            "ingredients": "Chicken, Chicken Broth, Liver, Wheat Gluten, Natural Flavors, Vitamins, Minerals",
            "description": "White meat chicken with very high moisture content, affordable gourmet option.",
            "match_score": 65,
            "rating": 4.1,
            "reviews": 734,
            "tags": ["White Meat", "Very High Moisture", "Budget Friendly", "Wet Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Pate",
            "budget_category": "budget"
        },
        {
            "name": "Diamond Maintenance Formula Adult Dry Cat Food",
            "image": "data/images/products/Diamond Maintenance Formula Adult Dry Cat Food.jpg",
            "price": 38.99,
            "price_per_oz": 0.61,
            "oz": 64,
            "food_type": "dry",
            "protein_content": 0.32,
            "fat_content": 0.12,
            "moisture_content": 0.10,
            "kcalories_per_oz": 120.0,
            "protein_sources": "Chicken",
            "ingredients": "Chicken Meal, Ground White Rice, Chicken Fat, Beet Pulp, Natural Flavor",
            "description": "Complete adult dry food with balanced nutrition for everyday feeding.",
            "match_score": 60,
            "rating": 4.2,
            "reviews": 423,
            "tags": ["Complete Nutrition", "Adult Formula", "Dry Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Pellets",
            "budget_category": "mid-range"
        },
        {
            "name": "Iams ProActive Health Original with Chicken Dry Cat Food",
            "image": "data/images/products/Iams ProActive Health Original with Chicken Dry Cat Food.jpg",
            "price": 33.99,
            "price_per_oz": 0.53,
            "oz": 64,
            "food_type": "dry",
            "protein_content": 0.32,
            "fat_content": 0.13,
            "moisture_content": 0.10,
            "kcalories_per_oz": 115.0,
            "protein_sources": "Chicken",
            "ingredients": "Chicken, Chicken By-Product Meal, Corn Meal, Ground Whole Grain Sorghum, Chicken Fat",
            "description": "ProActive health formula with chicken for immune system support.",
            "match_score": 58,
            "rating": 4.1,
            "reviews": 567,
            "tags": ["Immune Support", "ProActive Health", "Dry Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Pellets",
            "budget_category": "mid-range"
        },
        {
            "name": "Wellness Complete Health Deboned Chicken Dry Cat Food",
            "image": "data/images/products/Wellness Complete Health Deboned Chicken Dry Cat Food.jpg",
            "price": 32.29,
            "price_per_oz": 0.50,
            "oz": 64,
            "food_type": "dry",
            "protein_content": 0.34,
            "fat_content": 0.12,
            "moisture_content": 0.10,
            "kcalories_per_oz": 110.0,
            "protein_sources": "Chicken",
            "ingredients": "Deboned Chicken, Chicken Meal, Ground Brown Rice, Chicken Fat, Tomato Pomace",
            "description": "Natural dry food with deboned chicken and wholesome ingredients.",
            "match_score": 55,
            "rating": 4.3,
            "reviews": 345,
            "tags": ["Natural", "Deboned Chicken", "Complete Health", "Dry Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Pellets",
            "budget_category": "premium"
        },
        {
            "name": "Instinct Original Real Chicken Recipe Dry Cat Food",
            "image": "data/images/products/Instinct Original Real Chicken Recipe Dry Cat Food.jpg",
            "price": 40.00,
            "price_per_oz": 0.63,
            "oz": 64,
            "food_type": "dry",
            "protein_content": 0.38,
            "fat_content": 0.18,
            "moisture_content": 0.10,
            "kcalories_per_oz": 125.0,
            "protein_sources": "Chicken",
            "ingredients": "Chicken, Chicken Meal, Tapioca, Chicken Fat, Ground Flaxseed, Natural Flavor",
            "description": "High-protein dry food with real chicken as the first ingredient.",
            "match_score": 52,
            "rating": 4.4,
            "reviews": 278,
            "tags": ["High Protein", "Real Chicken", "Natural", "Dry Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Chicken"],
            "diet_type": "All Types",
            "texture": "Pellets",
            "budget_category": "premium"
        },
        {
            "name": "ORIJEN Regional Red Dry Cat Food",
            "image": "data/images/products/ORIJEN Regional Red Dry Cat Food.jpg",
            "price": 72.99,
            "price_per_oz": 1.14,
            "oz": 64,
            "food_type": "dry",
            "protein_content": 0.38,
            "fat_content": 0.18,
            "moisture_content": 0.10,
            "kcalories_per_oz": 130.0,
            "protein_sources": "Regional Red",
            "ingredients": "Deboned Beef, Deboned Wild Boar, Deboned Lamb, Mackerel Meal, Lamb Meal, Beef Meal",
            "description": "Ultra-premium dry food with regional red meat proteins for carnivore nutrition.",
            "match_score": 50,
            "rating": 4.6,
            "reviews": 189,
            "tags": ["Ultra Premium", "Regional Red", "High Protein", "Dry Food"],
            "suitable_breeds": ["All Breeds"],
            "age_range": ["Adult"],
            "flavors": ["Beef", "Lamb"],
            "diet_type": "High Protein",
            "texture": "Pellets",
            "budget_category": "luxury"
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
    elif texture != 'All Textures':
        for product in sample_products:
            if product["texture"].lower() == texture.lower():
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
                    <div class="product-details">
                        <div class="product-title">{product["name"]}</div>
                        <div class="product-description">{product["description"]}</div>
                        <div class="product-taste">{product["texture"]}</div>
                        <div class="product-ingredients"><strong>Ingredients:</strong> {highlighted_ingredients}</div>
                        <div class="product-price">${product["price"]:.2f} (${product["price_per_oz"]:.2f}/oz)</div>
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