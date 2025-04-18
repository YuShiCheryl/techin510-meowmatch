import streamlit as st
from PIL import Image
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="MeowMatch - Personalized Cat Food Recommendations",
    page_icon="🐱",
    layout="wide"
)

# Create placeholder images using PIL
def create_placeholder_image(width, height, color):
    img = Image.new('RGB', (width, height), color)
    return img

# Create sample images
hero_image = create_placeholder_image(800, 400, '#FFE5E5')
product_image1 = create_placeholder_image(300, 300, '#FFF0F0')
product_image2 = create_placeholder_image(300, 300, '#FFE8E8')
product_image3 = create_placeholder_image(300, 300, '#FFDADA')

# Add custom CSS for styling
st.markdown("""
<style>
    /* Main background and container styling */
    .stApp {
        background-color: #fff5f5;
    }
    
    /* Main content container */
    .main .block-container {
        background-color: transparent;
        padding: 3rem;
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    /* Feature card styling */
    .feature-card {
        background-color: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: linear-gradient(45deg, transparent 50%, #ffecec 50%);
        border-radius: 0 0 0 100%;
        opacity: 0.5;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Title styling */
    .main-title {
        color: #2d3436;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: left;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
    }
    
    .subtitle {
        color: #636e72;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        position: relative;
        z-index: 1;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #ff6b6b !important;
        color: white !important;
        border-radius: 25px;
        padding: 0.8rem 2.5rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
        position: relative;
        z-index: 1;
    }
    
    .stButton button:hover {
        background-color: #ff8787 !important;
        transform: translateY(-2px);
    }
    
    /* Feature section styling */
    .feature-title {
        color: #2d3436;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .feature-description {
        color: #636e72;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Product card styling */
    .product-card {
        background-color: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        transition: all 0.3s ease;
        margin: 1rem 0;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .product-title {
        color: #2d3436;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 1rem 0;
    }
    
    .product-price {
        color: #ff6b6b;
        font-size: 1.2rem;
        font-weight: 700;
    }
    
    /* Footer styling */
    .footer {
        color: #636e72;
        font-size: 0.9rem;
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
        opacity: 0.5;
    }
</style>

<!-- Add background decorations -->
<div class="bg-decoration">
    <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none">
        <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#ffecec;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#fff5f5;stop-opacity:1" />
            </linearGradient>
        </defs>
        <path d="M0,0 C30,20 70,20 100,0 L100,100 L0,100 Z" fill="url(#grad1)"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# Add hero section with image
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

# Add featured products section
st.markdown("""
<div style="text-align: center; margin: 4rem 0 2rem;">
    <h2 style="color: #2d3436; font-size: 2rem;">Featured Products</h2>
</div>
""", unsafe_allow_html=True)

prod_col1, prod_col2, prod_col3 = st.columns(3)

with prod_col1:
    st.image(product_image1, use_column_width=True)
    st.markdown("""
    <div class="product-card">
        <div class="product-title">Organic Chicken & Berries</div>
        <div class="product-price">$24.99</div>
    </div>
    """, unsafe_allow_html=True)

with prod_col2:
    st.image(product_image2, use_column_width=True)
    st.markdown("""
    <div class="product-card">
        <div class="product-title">Mixed Veggie Feast</div>
        <div class="product-price">$22.99</div>
    </div>
    """, unsafe_allow_html=True)

with prod_col3:
    st.image(product_image3, use_column_width=True)
    st.markdown("""
    <div class="product-card">
        <div class="product-title">Grain-Free Fish Mix</div>
        <div class="product-price">$26.99</div>
    </div>
    """, unsafe_allow_html=True)

# Add key features section
st.markdown("""
<div style="position: relative; margin-top: 4rem;">
    <h3 style="color: #2d3436; margin-bottom: 2rem; position: relative; z-index: 1;">Our Features</h3>
    <div style="position: absolute; top: -10px; right: 30px; transform: rotate(-10deg); z-index: 2;">
        <span style="font-size: 1.5rem;">✨</span>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">
            <span>🥩</span>
            <span>Ingredients & Nutrition</span>
        </div>
        <div class="feature-description">
        • Detailed ingredient analysis<br>
        • Nutritional content comparison<br>
        • Health-focused recommendations
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">
            <span>🏥</span>
            <span>Health Tracking</span>
        </div>
        <div class="feature-description">
        • Age and weight monitoring<br>
        • Activity level assessment<br>
        • Special dietary needs support
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">
            <span>💰</span>
            <span>Budget & Taste</span>
        </div>
        <div class="feature-description">
        • Price range filtering<br>
        • Flavor preference tracking<br>
        • Value analysis
        </div>
    </div>
    """, unsafe_allow_html=True)

# Add footer with decorative elements
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