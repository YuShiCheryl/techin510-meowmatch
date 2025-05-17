import streamlit as st
from PIL import Image
import pandas as pd
import random

# Set page configuration
st.set_page_config(
    page_title="MeowMatch - Personalized Recommendations",
    page_icon="M",
    layout="wide"
)

# Create placeholder images using PIL
def create_placeholder_image(width, height, color):
    img = Image.new('RGB', (width, height), color)
    return img

# Create sample images
product_image1 = create_placeholder_image(300, 300, '#FFE6E6')
product_image2 = create_placeholder_image(300, 300, '#FFCCD5')
product_image3 = create_placeholder_image(300, 300, '#FFD6E0')
product_image4 = create_placeholder_image(300, 300, '#FFC8DD')
product_image5 = create_placeholder_image(300, 300, '#FDECEF')
product_image6 = create_placeholder_image(300, 300, '#FFE2E8')

# Sample cat food data
recommended_products = [
    {
        "name": "Royal Canin Indoor",
        "image": product_image1,
        "price": "$45.99",
        "description": "Formulated for indoor cats to reduce hairballs and maintain healthy weight.",
        "match_score": 96,
        "rating": 4.8,
        "reviews": 520,
        "tags": ["Indoor", "Hairball Control", "Weight Management"]
    },
    {
        "name": "Purina Pro Plan Sensitive Skin",
        "image": product_image2,
        "price": "$39.99",
        "description": "Specially crafted for cats with sensitive skin and stomachs, with salmon as the first ingredient.",
        "match_score": 94,
        "rating": 4.7,
        "reviews": 432,
        "tags": ["Sensitive Skin", "Digestive Health", "High Protein"]
    },
    {
        "name": "Hills Science Diet Adult",
        "image": product_image3,
        "price": "$42.99",
        "description": "Balanced nutrition for adult cats with high-quality protein for lean muscles.",
        "match_score": 91,
        "rating": 4.6,
        "reviews": 380,
        "tags": ["Adult", "Balanced Nutrition", "Muscle Support"]
    },
    {
        "name": "Blue Buffalo Wilderness",
        "image": product_image4,
        "price": "$44.99",
        "description": "Grain-free, high-protein formula inspired by the diet of wildcats with deboned chicken.",
        "match_score": 88,
        "rating": 4.9,
        "reviews": 625,
        "tags": ["Grain-Free", "High Protein", "Natural"]
    },
    {
        "name": "Iams ProActive Health",
        "image": product_image5,
        "price": "$32.99",
        "description": "Complete and balanced nutrition for cats of all life stages with real chicken.",
        "match_score": 85,
        "rating": 4.5,
        "reviews": 310,
        "tags": ["All Life Stages", "Immune Support", "Affordable"]
    },
    {
        "name": "Wellness Complete Health",
        "image": product_image6,
        "price": "$38.99",
        "description": "Natural ingredients with added vitamins and minerals for whole body health.",
        "match_score": 82,
        "rating": 4.7,
        "reviews": 405,
        "tags": ["Natural", "No By-products", "Vitamin-Rich"]
    }
]

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
    }
    
    .profile-avatar:hover {
        transform: scale(1.08);
        box-shadow: 0 5px 15px rgba(255, 107, 149, 0.3);
    }
    
    .profile-icon {
        font-size: 24px;
        color: #FF6B95;
    }
    
    /* Back button */
    .back-button {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #666666;
        text-decoration: none;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .back-button:hover {
        color: #FF6B95;
        transform: translateX(-3px);
    }
    
    /* Main title styling */
    .main-title {
        color: #444444;
        font-size: 3rem;
        font-weight: 800;
        text-align: left;
        margin-bottom: 0.8rem;
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
    
    /* Pet summary card */
    .pet-summary-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF5F7 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0 3rem 0;
        box-shadow: 0 10px 30px rgba(255, 107, 149, 0.1);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 107, 149, 0.1);
        display: flex;
        align-items: center;
        gap: 2rem;
    }
    
    .pet-summary-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 150px;
        height: 150px;
        background: linear-gradient(45deg, transparent 50%, rgba(255, 107, 149, 0.05) 50%);
        border-radius: 0 0 0 100%;
    }
    
    .pet-avatar {
        width: 120px;
        height: 120px;
        border-radius: 60px;
        overflow: hidden;
        border: 4px solid white;
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.15);
    }
    
    .pet-info {
        flex: 1;
    }
    
    .pet-name {
        color: #444444;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .pet-details {
        color: #666666;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    
    .pet-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
    }
    
    .pet-tag {
        background: rgba(255, 107, 149, 0.1);
        color: #FF6B95;
        font-size: 0.9rem;
        font-weight: 600;
        padding: 0.4rem 1rem;
        border-radius: 20px;
    }
    
    /* Product card styling */
    .product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .product-card {
        background: #FFFFFF;
        padding: 1.8rem;
        border-radius: 18px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.08);
        border: 1px solid rgba(255, 107, 149, 0.1);
        position: relative;
        overflow: hidden;
        height: 100%;
        display: flex;
        flex-direction: column;
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
    
    .match-badge {
        position: absolute;
        top: 1.2rem;
        right: 1.2rem;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        color: white;
        font-size: 1rem;
        font-weight: 700;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(255, 107, 149, 0.2);
        z-index: 2;
    }
    
    .product-image {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(255, 107, 149, 0.1);
        margin-bottom: 1.5rem;
        transition: all 0.4s ease;
    }
    
    .product-card:hover .product-image {
        transform: scale(1.03);
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
        flex-grow: 1;
    }
    
    .product-price {
        color: #FF6B95;
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .product-rating {
        color: #FFB443;
        font-size: 1rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.3rem;
    }
    
    .rating-count {
        color: #999999;
        font-size: 0.9rem;
    }
    
    .product-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-bottom: 1.5rem;
    }
    
    .product-tag {
        background: rgba(255, 107, 149, 0.1);
        color: #FF6B95;
        font-size: 0.85rem;
        font-weight: 600;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #444444;
        margin: 3rem 0 1rem 0;
        position: relative;
        display: inline-block;
        padding-bottom: 0.5rem;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        border-radius: 2px;
    }
    
    /* Button styling */
    .cart-button {
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.7rem 1.5rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 15px rgba(255, 107, 149, 0.2) !important;
        letter-spacing: 0.5px !important;
        width: 100%;
        text-align: center;
        cursor: pointer;
        display: inline-block;
    }
    
    .cart-button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(255, 107, 149, 0.3) !important;
    }
    
    .refresh-button {
        background: rgba(255, 107, 149, 0.1) !important;
        color: #FF6B95 !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(255, 107, 149, 0.05) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 0.5rem !important;
    }
    
    .refresh-button:hover {
        background: rgba(255, 107, 149, 0.15) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Filter/preference card */
    .preference-card {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 6px 20px rgba(255, 107, 149, 0.08);
        border: 1px solid rgba(255, 107, 149, 0.1);
        margin-bottom: 1.5rem;
    }
    
    .preference-title {
        color: #444444;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .preference-icon {
        color: #FF6B95;
    }
    
    /* Slider styling */
    .stSlider > div > div > div > div {
        background-color: #FF6B95 !important;
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
    
    /* Footer */
    .footer {
        color: #666666;
        font-size: 1rem;
        font-weight: 500;
        margin-top: 5rem;
        text-align: center;
        position: relative;
        z-index: 1;
        padding: 2rem 0;
        border-top: 1px solid rgba(255, 107, 149, 0.1);
    }
</style>

<!-- Profile Avatar -->
<div class="profile-container">
    <a href="Profile" class="profile-avatar" target="_self">
        <span class="profile-icon">M</span>
    </a>
</div>
""", unsafe_allow_html=True)

# Back button
st.markdown("""
<a href="/" class="back-button">
    <span>←</span> Back to Home
</a>
""", unsafe_allow_html=True)

# Page title
st.markdown('<h1 class="main-title fade-in">Personalized Recommendations</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle fade-in">Discover the perfect cat food based on your pet\'s unique needs and preferences.</p>', unsafe_allow_html=True)

# Pet summary card
st.markdown("""
<div class="pet-summary-card fade-in">
    <div class="pet-avatar">
        <img src="data:image/png;base64," width="120" height="120">
    </div>
    <div class="pet-info">
        <div class="pet-name">Whiskers</div>
        <div class="pet-details">Persian • 5 years old • 10.5 lbs</div>
        <div class="pet-tags">
            <span class="pet-tag">Indoor Cat</span>
            <span class="pet-tag">Sensitive Digestion</span>
            <span class="pet-tag">Moderate Activity</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Filter and preferences sidebar 
sidecol1, maincol = st.columns([1, 3])

with sidecol1:
    st.markdown('<div class="section-header">Preferences</div>', unsafe_allow_html=True)
    
    # Diet Type
    st.markdown("""
    <div class="preference-card">
        <div class="preference-title">
            <span class="preference-icon">🥘</span> Diet Type
        </div>
    """, unsafe_allow_html=True)
    diet_type = st.selectbox("", ["All Types", "Grain-Free", "Limited Ingredient", "Weight Control", "Sensitive Digestion"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Age-specific
    st.markdown("""
    <div class="preference-card">
        <div class="preference-title">
            <span class="preference-icon">🐱</span> Age Specific
        </div>
    """, unsafe_allow_html=True)
    age_specific = st.selectbox("", ["All Ages", "Kitten", "Adult", "Senior"], index=1, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Protein Preference
    st.markdown("""
    <div class="preference-card">
        <div class="preference-title">
            <span class="preference-icon">🍗</span> Protein Preference
        </div>
    """, unsafe_allow_html=True)
    protein_pref = st.multiselect("", ["Chicken", "Fish", "Beef", "Turkey", "Lamb", "Duck"], ["Chicken", "Fish"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Price Range
    st.markdown("""
    <div class="preference-card">
        <div class="preference-title">
            <span class="preference-icon">💰</span> Price Range
        </div>
    """, unsafe_allow_html=True)
    price_range = st.slider("", 10, 70, (25, 50), label_visibility="collapsed", format="$%d")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Refresh Button
    st.markdown("""
    <div style="margin-top: 2rem; text-align: center;">
        <button class="refresh-button">
            <span>↻</span> Refresh Recommendations
        </button>
    </div>
    """, unsafe_allow_html=True)

with maincol:
    # Top Recommendations section
    st.markdown('<div class="section-header">Top Recommendations</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: #666666; margin-bottom: 2rem;">Based on Whiskers\' profile and your preferences</p>', unsafe_allow_html=True)
    
    # Product grid for top recommendations
    st.markdown('<div class="product-grid">', unsafe_allow_html=True)
    
    # Display top 3 recommendations
    for i, product in enumerate(recommended_products[:3]):
        st.markdown(f"""
        <div class="product-card">
            <div class="match-badge">{product["match_score"]}%</div>
            <div class="product-image">
                <img src="data:image/png;base64," width="100%" alt="{product["name"]}">
            </div>
            <div class="product-title">{product["name"]}</div>
            <div class="product-description">{product["description"]}</div>
            <div class="product-price">{product["price"]}</div>
            <div class="product-rating">
                {"⭐" * int(product["rating"])}{"<span style='color:#DDDDDD'>☆</span>" * (5-int(product["rating"]))}
                <span class="rating-count">({product["reviews"]} reviews)</span>
            </div>
            <div class="product-tags">
                {" ".join([f'<span class="product-tag">{tag}</span>' for tag in product["tags"]])}
            </div>
            <div class="cart-button">Add to Cart</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Also Recommended section
    st.markdown('<div class="section-header">Also Recommended</div>', unsafe_allow_html=True)
    st.markdown('<p style="color: #666666; margin-bottom: 2rem;">Other great options that match your preferences</p>', unsafe_allow_html=True)
    
    # Product grid for also recommended
    st.markdown('<div class="product-grid">', unsafe_allow_html=True)
    
    # Display remaining recommendations
    for i, product in enumerate(recommended_products[3:]):
        st.markdown(f"""
        <div class="product-card">
            <div class="match-badge">{product["match_score"]}%</div>
            <div class="product-image">
                <img src="data:image/png;base64," width="100%" alt="{product["name"]}">
            </div>
            <div class="product-title">{product["name"]}</div>
            <div class="product-description">{product["description"]}</div>
            <div class="product-price">{product["price"]}</div>
            <div class="product-rating">
                {"⭐" * int(product["rating"])}{"<span style='color:#DDDDDD'>☆</span>" * (5-int(product["rating"]))}
                <span class="rating-count">({product["reviews"]} reviews)</span>
            </div>
            <div class="product-tags">
                {" ".join([f'<span class="product-tag">{tag}</span>' for tag in product["tags"]])}
            </div>
            <div class="cart-button">Add to Cart</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2024 MeowMatch | All rights reserved | Made with ❤️ for cats everywhere</p>
</div>
""", unsafe_allow_html=True)