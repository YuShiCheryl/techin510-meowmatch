import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="MeowMatch - Personalized Cat Food Recommendations",
    page_icon="🐱",
    layout="wide"
)

# Custom CSS for the avatar
st.markdown("""
<style>
    /* Hide the default Streamlit menu button */
    #MainMenu {
        visibility: hidden;
    }
    
    /* Main background and container styling */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Main content container */
    .main .block-container {
        background-color: #ffffff;
        padding: 3rem;
        padding-top: 6rem;  /* 增加顶部间距 */
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    /* Profile avatar container */
    .profile-container {
        position: fixed;
        top: 2.5rem;  /* 增加顶部间距 */
        right: 2rem;
        z-index: 1001;
        padding: 0.5rem;
    }
    
    .profile-avatar {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        border: 2px solid #e60000;
        background-color: #FFE0E0;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .profile-avatar:hover {
        transform: scale(1.05);
        box-shadow: 0 2px 8px rgba(230,0,0,0.2);
    }
    
    .profile-icon {
        font-size: 24px;
        color: #e60000;
    }

    /* Add top margin to the first section */
    .hero-section {
        margin-top: 3.5rem;  /* 增加顶部间距 */
    }

    /* Feature card styling */
    .feature-card {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        position: relative;
        overflow: hidden;
        border: 1px solid #e0e0e0;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: linear-gradient(45deg, transparent 50%, #ffb3b3 50%);
        border-radius: 0 0 0 100%;
        opacity: 0.8;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.2);
    }
    
    /* Title styling */
    .main-title {
        color: #000000;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: left;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
        text-shadow: 1px 1px 1px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        color: #333333;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 2rem;
        position: relative;
        z-index: 1;
        line-height: 1.6;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #e60000 !important;
        color: white !important;
        border-radius: 25px;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        position: relative;
        z-index: 1;
        box-shadow: 0 2px 8px rgba(230,0,0,0.3);
    }
    
    .stButton button:hover {
        background-color: #cc0000 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(230,0,0,0.4);
    }
    
    /* Feature section styling */
    .feature-title {
        color: #000000;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .feature-description {
        color: #333333;
        font-size: 1rem;
        line-height: 1.6;
        font-weight: 500;
    }
    
    /* Product card styling */
    .product-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        transition: all 0.3s ease;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    }
    
    .product-title {
        color: #000000;
        font-size: 1.2rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .product-price {
        color: #e60000;
        font-size: 1.3rem;
        font-weight: 800;
    }
    
    /* Footer styling */
    .footer {
        color: #333333;
        font-size: 1rem;
        font-weight: 500;
        margin-top: 4rem;
        text-align: center;
        position: relative;
        z-index: 1;
    }

    /* Background decorations */
    .bg-decoration {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        opacity: 0.3;
    }

    /* Section headings */
    h2, h3 {
        color: #000000 !important;
        font-weight: 700 !important;
    }
</style>

<!-- Profile Avatar -->
<div class="profile-container">
    <a href="Profile" class="profile-avatar" target="_self">
        <span class="profile-icon">🐱</span>
    </a>
</div>

# Add search box next to the avatar
search_query = st.text_input('Search', key='search_input', placeholder='Search...', label_visibility='collapsed')

# If search is submitted, navigate to the search page
if search_query:
    st.switch_page('pages/2_Search.py')
""", unsafe_allow_html=True)

# Create placeholder images using PIL
def create_placeholder_image(width, height, color):
    img = Image.new('RGB', (width, height), color)
    return img

# Create sample images
hero_image = create_placeholder_image(800, 400, '#FFD6D6')
product_image1 = create_placeholder_image(300, 300, '#FFE0E0')
product_image2 = create_placeholder_image(300, 300, '#FFD6D6')
product_image3 = create_placeholder_image(300, 300, '#FFCCCC')

# Sample cat food data
sample_food_data = {
    'Name': ['Royal Canin Indoor', 'Hills Science Diet', 'Purina Pro Plan', 'Blue Buffalo'],
    'Protein': ['32%', '30%', '34%', '36%'],
    'Fat': ['15%', '16%', '14%', '15%'],
    'Fiber': ['4.5%', '4%', '3%', '4%'],
    'Price': ['$45.99', '$42.99', '$39.99', '$44.99']
}

# Add custom CSS for styling
st.markdown("""
<style>
    /* Main background and container styling */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Main content container */
    .main .block-container {
        background-color: #ffffff;
        padding: 3rem;
        padding-top: 5rem;  /* 增加顶部间距 */
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    /* Feature card styling */
    .feature-card {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        position: relative;
        overflow: hidden;
        border: 1px solid #e0e0e0;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: linear-gradient(45deg, transparent 50%, #ffb3b3 50%);
        border-radius: 0 0 0 100%;
        opacity: 0.8;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.2);
    }
    
    /* Title styling */
    .main-title {
        color: #000000;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: left;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
        text-shadow: 1px 1px 1px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        color: #333333;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 2rem;
        position: relative;
        z-index: 1;
        line-height: 1.6;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #e60000 !important;
        color: white !important;
        border-radius: 25px;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        position: relative;
        z-index: 1;
        box-shadow: 0 2px 8px rgba(230,0,0,0.3);
    }
    
    .stButton button:hover {
        background-color: #cc0000 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(230,0,0,0.4);
    }
    
    /* Feature section styling */
    .feature-title {
        color: #000000;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .feature-description {
        color: #333333;
        font-size: 1rem;
        line-height: 1.6;
        font-weight: 500;
    }
    
    /* Product card styling */
    .product-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        transition: all 0.3s ease;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    }
    
    .product-title {
        color: #000000;
        font-size: 1.2rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .product-price {
        color: #e60000;
        font-size: 1.3rem;
        font-weight: 800;
    }
    
    /* Footer styling */
    .footer {
        color: #333333;
        font-size: 1rem;
        font-weight: 500;
        margin-top: 4rem;
        text-align: center;
        position: relative;
        z-index: 1;
    }

    /* Background decorations */
    .bg-decoration {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        opacity: 0.3;
    }

    /* Section headings */
    h2, h3 {
        color: #000000 !important;
        font-weight: 700 !important;
    }
</style>

<!-- Add background decorations -->
<div class="bg-decoration">
    <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none">
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#ffe6e6;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#ffffff;stop-opacity:1" />
            </linearGradient>
        </defs>
        <path d="M0,0 C30,20 70,20 100,0 L100,100 L0,100 Z" fill="url(#grad1)"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero-section">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
    <div style="position: relative;">
        <div style="position: absolute; top: -20px; right: 20px; transform: rotate(15deg); z-index: 2;">
            <span style="font-size: 2rem;">🐱</span>
        </div>
        <h1 class="main-title">MeowMatch<br>Food Suggestion for Your Cat</h1>
        <p class="subtitle">Whether cooking for your cat is made in kitchen or delivered, it just is<br>important to feed your cat food that's made with real ingredients.</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("SHOP MEAL MIXES", use_container_width=False)

with col2:
    st.image(hero_image, use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Ingredients & Comparison Section
st.markdown("<h2 id='ingredients'>Ingredients & Comparison</h2>", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    df = pd.DataFrame(sample_food_data)
    st.dataframe(df, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Nutritional Comparison")
        st.bar_chart({"Protein": [32, 30, 34, 36], "Fat": [15, 16, 14, 15]})
    with col2:
        st.subheader("Key Ingredients")
        st.write("• Chicken (Source of protein)")
        st.write("• Fish Oil (Omega-3 fatty acids)")
        st.write("• Sweet Potatoes (Complex carbohydrates)")
        st.write("• Cranberries (Antioxidants)")
    st.markdown('</div>', unsafe_allow_html=True)

# Health Data Input Section
st.markdown("<h2 id='health'>Health Data Input</h2>", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Cat's Age (years)", min_value=0, max_value=30, value=5)
        st.number_input("Weight (lbs)", min_value=0.0, max_value=30.0, value=10.0)
        activity_level = st.select_slider(
            "Activity Level",
            options=["Very Low", "Low", "Moderate", "High", "Very High"],
            value="Moderate"
        )
    with col2:
        st.multiselect("Health Conditions", 
            ["None", "Overweight", "Diabetes", "Kidney Disease", "Food Allergies"])
        st.text_area("Additional Notes", height=100)
        st.button("Save Health Data")
    st.markdown('</div>', unsafe_allow_html=True)

# Search by Ingredient Section
st.markdown("<h2 id='search'>Search by Ingredient</h2>", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    search_col1, search_col2 = st.columns([3, 1])
    with search_col1:
        st.text_input("Search ingredients or nutrients...", placeholder="E.g., chicken, taurine, omega-3")
    with search_col2:
        st.button("Search", use_container_width=True)
    
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    st.write("Popular searches:")
    st.markdown("🔍 Grain-free • 🐟 Fish-based • 🍗 Chicken • 🥩 High protein")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Recommendations Section
st.markdown("<h2 id='recommendations'>Personalized Recommendations</h2>", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    rec_col1, rec_col2, rec_col3 = st.columns(3)
    
    with rec_col1:
        st.image(product_image1, use_column_width=True)
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Organic Chicken & Berries</div>
            <div class="product-price">$24.99</div>
        </div>
        """, unsafe_allow_html=True)
        
    with rec_col2:
        st.image(product_image2, use_column_width=True)
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Mixed Veggie Feast</div>
            <div class="product-price">$22.99</div>
        </div>
        """, unsafe_allow_html=True)
        
    with rec_col3:
        st.image(product_image3, use_column_width=True)
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Grain-Free Fish Mix</div>
            <div class="product-price">$26.99</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer (keep your existing footer)
st.markdown("""
<div class="footer">
    <div style="position: absolute; bottom: 20px; left: 20px; transform: rotate(-15deg);">
        <span style="font-size: 1.5rem;">🐾</span>
    </div>
    <p>© 2024 MeowMatch | All rights reserved</p>
    <div style="position: absolute; bottom: 20px; right: 20px; transform: rotate(15deg);">
        <span style="font-size: 1.5rem;">🎀</span>
    </div>
</div>
""", unsafe_allow_html=True) 