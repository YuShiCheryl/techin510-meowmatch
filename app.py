import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from session_utils import init_session_state, get_user_profile, get_pet_display_info, get_profile_avatar_html

# Set page configuration
st.set_page_config(
    page_title="MeowMatch - Personalized Cat Food Recommendations",
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

# Create sample images
hero_image = create_placeholder_image(800, 400, '#FFE5D4')     # 浅橙色
product_image1 = create_placeholder_image(300, 300, '#FFE5D4') # 浅橙色
product_image2 = create_placeholder_image(300, 300, '#FFEAD6') # 更浅的橙色
product_image3 = create_placeholder_image(300, 300, '#FFF0E6') # 极浅橙色

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
        padding-top: 6rem;
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

    /* Add top margin to the first section */
    .hero-section {
        margin-top: 2rem;
        position: relative;
        overflow: hidden;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(255, 140, 66, 0.1);
        background: linear-gradient(135deg, #FFFBF7 0%, #FFE8D9 100%);
        padding: 2rem;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
    }
    
    .hero-image {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(255, 140, 66, 0.15);
        transform: perspective(1000px) rotateY(-5deg);
        transition: all 0.5s ease;
    }
    
    .hero-image:hover {
        transform: perspective(1000px) rotateY(0deg);
    }

    /* Feature card styling */
    .feature-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF8F3 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        transition: all 0.4s ease;
        box-shadow: 0 8px 20px rgba(255, 140, 66, 0.08);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 140, 66, 0.1);
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 120px;
        height: 120px;
        background: linear-gradient(45deg, transparent 50%, rgba(255, 140, 66, 0.1) 50%);
        border-radius: 0 0 0 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(255, 140, 66, 0.12);
    }
    
    /* Title styling */
    .main-title {
        color: #444444;
        font-size: 3.8rem;
        font-weight: 800;
        text-align: left;
        margin-bottom: 0.8rem;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
    }
    
    .main-title .subtitle-text {
        font-size: 2.2rem;
        font-weight: 700;
        display: block;
        margin-top: 5px;
    }
    
    .subtitle {
        color: #666666;
        font-size: 1.25rem;
        font-weight: 500;
        margin-bottom: 2.5rem;
        position: relative;
        z-index: 1;
        line-height: 1.7;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.8rem 2.8rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        z-index: 1 !important;
        box-shadow: 0 5px 15px rgba(255, 140, 66, 0.2) !important;
        letter-spacing: 0.5px !important;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(255, 140, 66, 0.3) !important;
    }
    
    .stButton button::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, #FFB380 0%, #FF8C42 100%);
        border-radius: 30px;
        opacity: 0;
        z-index: -1;
        transition: opacity 0.3s ease;
    }
    
    .stButton button:hover::after {
        opacity: 1;
    }
    
    /* Feature buttons - Streamlit按钮样式，保持HTML按钮的外观 */
    .feature-button-streamlit .stButton button {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF8F3 100%) !important;
        color: #FF8C42 !important;
        border: 2px solid #FF8C42 !important;
        border-radius: 18px !important;
        padding: 1.2rem 2.5rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 6px 20px rgba(255, 140, 66, 0.08) !important;
        min-width: 220px !important;
        position: relative !important;
        overflow: hidden !important;
        z-index: 1 !important;
        letter-spacing: 0.5px !important;
        width: 100% !important;
    }

    .feature-button-streamlit .stButton button::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        border-radius: 18px;
        opacity: 0;
        z-index: -1;
        transition: opacity 0.3s ease;
    }

    .feature-button-streamlit .stButton button:hover {
        color: #FFFFFF !important;
        transform: translateY(-5px) !important;
        box-shadow: 0 12px 25px rgba(255, 140, 66, 0.15) !important;
    }
    
    .feature-button-streamlit .stButton button:hover::after {
        opacity: 1;
    }
    
    /* Feature section styling */
    .feature-title {
        color: #444444;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .feature-description {
        color: #666666;
        font-size: 1.05rem;
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* Product card styling */
    .product-card {
        background: #FFFFFF;
        padding: 1.8rem;
        border-radius: 18px;
        text-align: center;
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
        height: 5px;
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.4s ease;
    }
    
    .product-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(255, 140, 66, 0.12);
    }
    
    .product-card:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }
    
    .product-image {
        border-radius: 12px;
        margin-bottom: 1.5rem;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(255, 140, 66, 0.1);
        transition: all 0.4s ease;
    }
    
    .product-card:hover .product-image {
        transform: scale(1.03);
    }
    
    .product-title {
        color: #444444;
        font-size: 1.3rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .product-price {
        color: #FF8C42;
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 0.5px;
    }
    
    /* Rating stars */
    .rating {
        color: #FFB443;
        font-size: 1.1rem;
        margin: 0.5rem 0;
    }
    
    /* Badge for new products */
    .badge {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        color: white;
        font-size: 0.85rem;
        font-weight: 600;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        box-shadow: 0 3px 10px rgba(255, 140, 66, 0.2);
        letter-spacing: 0.5px;
    }
    
    /* Section headers */
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #444444;
        margin: 3.5rem 0 1.5rem 0;
        position: relative;
        display: inline-block;
        padding-bottom: 0.5rem;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        border-radius: 2px;
    }
    
    /* Feature buttons container */
    .feature-buttons {
        display: flex;
        justify-content: center;
        gap: 2.5rem;
        margin: 3.5rem 0;
        padding: 1.5rem;
        flex-wrap: wrap;
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
    
    /* Add to cart button */
    .cart-button {
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.6rem 1.5rem !important;
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
    
    /* Footer styling */
    .footer {
        color: #666666;
        font-size: 1rem;
        font-weight: 500;
        margin-top: 5rem;
        text-align: center;
        position: relative;
        z-index: 1;
        padding: 2rem 0;
        border-top: 1px solid rgba(255, 140, 66, 0.1);
    }
    
    .footer-paw {
        position: absolute;
        font-size: 1.5rem;
        opacity: 0.6;
        transition: transform 0.3s ease;
    }
    
    .footer-paw-left {
        bottom: 20px;
        left: 20px;
        transform: rotate(-15deg);
    }
    
    .footer-paw-right {
        bottom: 20px;
        right: 20px;
        transform: rotate(15deg);
    }
    
    .footer:hover .footer-paw {
        transform: scale(1.2);
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
    
    /* Floating elements */
    .floating {
        animation: floating 3s ease-in-out infinite;
    }

    @keyframes floating {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0px);
        }
    }
    
    /* Search bar styling */
    .stTextInput > div > div > input {
        border-radius: 30px !important;
        border: 1px solid rgba(255, 140, 66, 0.3) !important;
        padding: 1rem 1.5rem !important;
        box-shadow: 0 4px 15px rgba(255, 140, 66, 0.05) !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border: 1px solid rgba(255, 140, 66, 0.8) !important;
        box-shadow: 0 6px 20px rgba(255, 140, 66, 0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state and display dynamic avatar
init_session_state()
st.markdown(get_profile_avatar_html(), unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
    <div class="hero-content">
        <h1 class="main-title">MeowMatch<br><span class="subtitle-text">Food Suggestion for Your Cat</span></h1>
        <p class="subtitle">We help you find the perfect nutrition for your feline friend with personalized recommendations based on health needs and preferences.</p>
       
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="hero-image">', unsafe_allow_html=True)
    st.image(hero_image, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Feature Buttons - 改为Streamlit按钮但保持原有样式
st.markdown('<div class="feature-buttons fade-in">', unsafe_allow_html=True)

feature_col1, feature_col2, feature_col3 = st.columns(3, gap="large")

with feature_col1:
    st.markdown('<div class="feature-button-streamlit">', unsafe_allow_html=True)
    if st.button("Search by Ingredient", key="search_btn", use_container_width=True):
        st.switch_page("pages/2_Search.py")
    st.markdown('</div>', unsafe_allow_html=True)

with feature_col2:
    st.markdown('<div class="feature-button-streamlit">', unsafe_allow_html=True)
    if st.button("Compare Products", key="compare_btn", use_container_width=True):
        st.switch_page("pages/3_Compare.py")
    st.markdown('</div>', unsafe_allow_html=True)

with feature_col3:
    st.markdown('<div class="feature-button-streamlit">', unsafe_allow_html=True)
    if st.button("Custom Recommendations", key="recommend_btn", use_container_width=True):
        st.switch_page("pages/4_Recommendations.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Recommendations Section
st.markdown('<h2 class="section-header fade-in">Your Cat Will Love These</h2>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
    rec_col1, rec_col2, rec_col3 = st.columns(3)
    
    with rec_col1:
        st.markdown('<div class="product-image">', unsafe_allow_html=True)
        st.image(product_image1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Organic Chicken & Berries</div>
            <div class="rating">⭐⭐⭐⭐⭐ (128)</div>
            <div class="product-price">$24.99</div>
            <button class="cart-button">Add to Cart</button>
        </div>
        """, unsafe_allow_html=True)
        
    with rec_col2:
        st.markdown('<div class="product-image">', unsafe_allow_html=True)
        st.image(product_image2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Mixed Veggie Feast</div>
            <div class="rating">⭐⭐⭐⭐<span style="color:#DDDDDD">☆</span> (94)</div>
            <div class="product-price">$22.99</div>
            <button class="cart-button">Add to Cart</button>
        </div>
        """, unsafe_allow_html=True)
        
    with rec_col3:
        st.markdown('<div class="product-image">', unsafe_allow_html=True)
        st.image(product_image3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Grain-Free Fish Mix</div>
            <div class="rating">⭐⭐⭐⭐⭐ (156)</div>
            <div class="product-price">$26.99</div>
            <button class="cart-button">Add to Cart</button>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Popular Products Section
st.markdown('<h2 class="section-header fade-in">Popular Products</h2>', unsafe_allow_html=True)

# Sample popular products data
popular_products = [
    {
        "name": "Purina Pro Plan",
        "price": "$27.99",
        "image": product_image1,
        "rating": 4.8,
        "reviews": 1250
    },
    {
        "name": "Orijen Cat & Kitten",
        "price": "$39.99",
        "image": product_image2,
        "rating": 4.9,
        "reviews": 980
    },
    {
        "name": "Acana Wild Coast",
        "price": "$35.99",
        "image": product_image3,
        "rating": 4.7,
        "reviews": 850
    }
]

# Display popular products in a grid
pop_cols = st.columns(3)
for idx, product in enumerate(popular_products):
    with pop_cols[idx]:
        st.markdown('<div class="product-card fade-in">', unsafe_allow_html=True)
        st.markdown('<div class="product-image">', unsafe_allow_html=True)
        st.image(product["image"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="product-title">{product['name']}</div>
        <div class="rating">{"⭐" * int(product['rating'])}{"<span style='color:#DDDDDD'>☆</span>" * (5-int(product['rating']))} ({product['reviews']})</div>
        <div class="product-price">{product['price']}</div>
        """, unsafe_allow_html=True)
        st.markdown('<button class="cart-button">Add to Cart</button>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# New Arrivals Section
st.markdown('<h2 class="section-header fade-in">New Arrivals</h2>', unsafe_allow_html=True)

# Sample new arrivals data
new_arrivals = [
    {
        "name": "Wellness Complete Health",
        "price": "$28.99",
        "image": product_image2,
        "is_new": True
    },
    {
        "name": "Instinct Raw Boost",
        "price": "$34.99",
        "image": product_image3,
        "is_new": True
    },
    {
        "name": "Merrick Backcountry",
        "price": "$31.99",
        "image": product_image1,
        "is_new": True
    }
]

# Display new arrivals in a grid
new_cols = st.columns(3)
for idx, product in enumerate(new_arrivals):
    with new_cols[idx]:
        st.markdown('<div class="product-card fade-in">', unsafe_allow_html=True)
        if product["is_new"]:
            st.markdown('<span class="badge">New</span>', unsafe_allow_html=True)
        st.markdown('<div class="product-image">', unsafe_allow_html=True)
        st.image(product["image"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="product-title">{product['name']}</div>
        <div class="rating">⭐⭐⭐⭐⭐ (New)</div>
        <div class="product-price">{product['price']}</div>
        """, unsafe_allow_html=True)
        st.markdown('<button class="cart-button">Add to Cart</button>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Why Choose Us Section
st.markdown('<h2 class="section-header fade-in">Why Choose MeowMatch</h2>', unsafe_allow_html=True)

why_cols = st.columns(3)
with why_cols[0]:
    st.markdown("""
    <div class="feature-card fade-in">
        <div class="feature-title">Quality Ingredients</div>
        <p class="feature-description">We carefully select products with natural, high-quality ingredients that support your cat's health and wellbeing.</p>
    </div>
    """, unsafe_allow_html=True)
    
with why_cols[1]:
    st.markdown("""
    <div class="feature-card fade-in">
        <div class="feature-title">Nutrition Experts</div>
        <p class="feature-description">Our recommendations are backed by feline nutrition experts to ensure optimal health for your furry friend.</p>
    </div>
    """, unsafe_allow_html=True)
    
with why_cols[2]:
    st.markdown("""
    <div class="feature-card fade-in">
        <div class="feature-title">Personalized Care</div>
        <p class="feature-description">Get tailored food suggestions based on your cat's age, weight, health conditions, and taste preferences.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer fade-in">
    <p>© 2025 MeowMatch | All rights reserved | Purr-fect nutrition, purr-fect love</p>
</div>
""", unsafe_allow_html=True)