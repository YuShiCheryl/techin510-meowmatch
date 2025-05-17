import streamlit as st
from PIL import Image
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="MeowMatch - Compare Cat Food Products",
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

# Sample cat food data
sample_food_data = {
    "Royal Canin Indoor": {
        "image": product_image1,
        "price": "$45.99",
        "protein": "32%",
        "fat": "15%",
        "fiber": "4.5%",
        "calories": "350 kcal/cup",
        "rating": 4.8,
        "reviews": 520,
        "suitable_for": ["Indoor Cats", "Weight Management", "Hairball Control"],
        "main_ingredients": ["Chicken By-Product Meal", "Corn", "Wheat", "Corn Gluten Meal"],
        "pros": ["Reduces stool odor", "Helps hairball reduction", "Controlled calorie content"],
        "cons": ["Contains grains", "Higher price point", "Contains by-products"]
    },
    "Hills Science Diet": {
        "image": product_image2,
        "price": "$42.99",
        "protein": "30%",
        "fat": "16%",
        "fiber": "4%",
        "calories": "340 kcal/cup",
        "rating": 4.7,
        "reviews": 490,
        "suitable_for": ["Adult Cats", "Digestive Health", "Shiny Coat"],
        "main_ingredients": ["Chicken", "Whole Grain Wheat", "Corn Gluten Meal"],
        "pros": ["Highly digestible", "Supports immune system", "Balanced nutrition"],
        "cons": ["Contains grains", "Some cats dislike taste", "Less protein than competitors"]
    },
    "Purina Pro Plan": {
        "image": product_image3,
        "price": "$39.99",
        "protein": "36%",
        "fat": "14%",
        "fiber": "3%",
        "calories": "370 kcal/cup",
        "rating": 4.9,
        "reviews": 650,
        "suitable_for": ["Active Cats", "All Life Stages", "Picky Eaters"],
        "main_ingredients": ["Chicken", "Rice", "Corn Gluten Meal", "Beef Fat"],
        "pros": ["High protein content", "Great taste acceptance", "Supports digestive health"],
        "cons": ["Contains corn gluten", "Some artificial ingredients", "Higher calorie content"]
    },
    "Blue Buffalo": {
        "image": product_image4,
        "price": "$44.99",
        "protein": "36%",
        "fat": "15%",
        "fiber": "4%",
        "calories": "360 kcal/cup",
        "rating": 4.8,
        "reviews": 580,
        "suitable_for": ["All Cats", "Natural Diet Preference", "Sensitive Stomach"],
        "main_ingredients": ["Deboned Chicken", "Chicken Meal", "Brown Rice", "Barley"],
        "pros": ["No by-products", "Natural ingredients", "No artificial preservatives"],
        "cons": ["Higher price", "Some cats refuse taste", "Occasional digestive issues"]
    }
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
    
    /* Comparison container */
    .comparison-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF5F7 100%);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(255, 107, 149, 0.1);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 107, 149, 0.1);
        transition: all 0.3s ease;
    }
    
    .comparison-container:hover {
        box-shadow: 0 15px 40px rgba(255, 107, 149, 0.15);
        transform: translateY(-5px);
    }
    
    .comparison-container::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 150px;
        height: 150px;
        background: linear-gradient(45deg, transparent 50%, rgba(255, 107, 149, 0.05) 50%);
        border-radius: 0 0 0 100%;
    }
    
    /* Product card styling */
    .product-card {
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 18px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.08);
        border: 1px solid rgba(255, 107, 149, 0.1);
        position: relative;
        overflow: hidden;
        height: 100%;
    }
    
    .product-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.4s ease;
    }
    
    .product-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(255, 107, 149, 0.12);
    }
    
    .product-card:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }
    
    .product-image {
        border-radius: 12px;
        margin-bottom: 1.5rem;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(255, 107, 149, 0.1);
        transition: all 0.4s ease;
    }
    
    .product-card:hover .product-image {
        transform: scale(1.03);
    }
    
    .product-title {
        color: #444444;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 1rem 0;
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
        font-size: 1.1rem;
        margin: 0.5rem 0;
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
    
    /* Comparison table styling */
    .comparison-table {
        background: #FFFFFF;
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.08);
        margin: 2rem 0;
        border: 1px solid rgba(255, 107, 149, 0.1);
    }
    
    .comparison-table th {
        background: linear-gradient(90deg, #FFF5F7 0%, #FFFFFF 100%);
        color: #666666;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 1.2rem 1.5rem;
        text-align: left;
        border-bottom: 2px solid rgba(255, 107, 149, 0.1);
    }
    
    .comparison-table td {
        padding: 1.2rem 1.5rem;
        font-size: 1rem;
        border-bottom: 1px solid rgba(255, 107, 149, 0.1);
        color: #444444;
    }
    
    .comparison-table tr:last-child td {
        border-bottom: none;
    }
    
    .comparison-table tr:hover td {
        background-color: rgba(255, 107, 149, 0.03);
    }
    
    /* Highlight styling */
    .highlight-better {
        background-color: rgba(39, 174, 96, 0.1);
        color: #27AE60;
        font-weight: 600;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
    }
    
    .highlight-worse {
        background-color: rgba(255, 107, 149, 0.1);
        color: #FF6B95;
        font-weight: 600;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #444444;
        margin: 2.5rem 0 1.5rem 0;
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
    
    /* Feature badges */
    .feature-badge {
        display: inline-block;
        background: rgba(255, 107, 149, 0.1);
        color: #FF6B95;
        font-size: 0.85rem;
        font-weight: 600;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        margin-right: 0.6rem;
        margin-bottom: 0.6rem;
    }
    
    /* Pros/Cons box */
    .pros-cons-box {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(255, 107, 149, 0.08);
        border: 1px solid rgba(255, 107, 149, 0.1);
    }
    
    .pros-title {
        color: #27AE60;
        font-weight: 700;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .cons-title {
        color: #FF6B95;
        font-weight: 700;
        margin: 1.2rem 0 0.8rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .pros-cons-list {
        margin: 0;
        padding: 0 0 0 1.5rem;
    }
    
    .pros-cons-list li {
        margin-bottom: 0.5rem;
        line-height: 1.5;
    }
    
    /* Recommendation box */
    .recommendation-box {
        background: linear-gradient(135deg, #FFF5F7 0%, #FFFFFF 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 30px rgba(255, 107, 149, 0.1);
        border: 1px solid rgba(255, 107, 149, 0.1);
        position: relative;
    }
    
    .recommendation-title {
        color: #FF6B95;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        padding-left: 1.5rem;
        position: relative;
    }
    
    .recommendation-title::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 80%;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        border-radius: 2px;
    }
    
    .recommendation-text {
        color: #444444;
        line-height: 1.7;
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
st.markdown('<h1 class="main-title fade-in">Compare Cat Food Products</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle fade-in">Find the best food for your pet by comparing nutrition, ingredients, and benefits.</p>', unsafe_allow_html=True)

# Product selection container
st.markdown('<div class="comparison-container fade-in">', unsafe_allow_html=True)

select_col1, select_col2 = st.columns(2)

with select_col1:
    st.markdown('<div class="section-header">First Product</div>', unsafe_allow_html=True)
    product1 = st.selectbox(
        "",
        list(sample_food_data.keys()),
        index=0,
        key="product1",
        label_visibility="collapsed"
    )

with select_col2:
    st.markdown('<div class="section-header">Second Product</div>', unsafe_allow_html=True)
    product2 = st.selectbox(
        "",
        list(sample_food_data.keys()),
        index=1,
        key="product2",
        label_visibility="collapsed"
    )

# Compare button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    compare_button = st.button("Compare Products", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Get product data for selected products
product1_data = sample_food_data[product1]
product2_data = sample_food_data[product2]

# Display comparison results
if compare_button or True:  # Always show for demo, in production use just compare_button
    # Product cards
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    product_col1, product_col2 = st.columns(2, gap="large")
    
    with product_col1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown('<div class="product-image">', unsafe_allow_html=True)
        st.image(product1_data["image"], use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-title">{product1}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-rating">{"⭐" * int(product1_data["rating"])}{"<span style=\'color:#DDDDDD\'>☆</span>" * (5-int(product1_data["rating"]))} ({product1_data["reviews"]})</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-price">{product1_data["price"]}</div>', unsafe_allow_html=True)
        
        # Suitable for badges
        st.markdown('<div style="margin-top: 1.2rem;">', unsafe_allow_html=True)
        for feature in product1_data["suitable_for"]:
            st.markdown(f'<span class="feature-badge">{feature}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with product_col2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown('<div class="product-image">', unsafe_allow_html=True)
        st.image(product2_data["image"], use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-title">{product2}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-rating">{"⭐" * int(product2_data["rating"])}{"<span style=\'color:#DDDDDD\'>☆</span>" * (5-int(product2_data["rating"]))} ({product2_data["reviews"]})</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-price">{product2_data["price"]}</div>', unsafe_allow_html=True)
        
        # Suitable for badges
        st.markdown('<div style="margin-top: 1.2rem;">', unsafe_allow_html=True)
        for feature in product2_data["suitable_for"]:
            st.markdown(f'<span class="feature-badge">{feature}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Nutritional Comparison Table
    st.markdown('<div class="section-header">Nutritional Comparison</div>', unsafe_allow_html=True)
    
    # Create comparison table HTML
    comparison_table_html = f"""
    <table class="comparison-table" width="100%">
        <tr>
            <th style="width: 30%;">Nutrient</th>
            <th style="width: 35%;">{product1}</th>
            <th style="width: 35%;">{product2}</th>
        </tr>
        <tr>
            <td><strong>Protein</strong></td>
            <td>{product1_data["protein"]}</td>
            <td>{product2_data["protein"]}</td>
        </tr>
        <tr>
            <td><strong>Fat</strong></td>
            <td>{product1_data["fat"]}</td>
            <td>{product2_data["fat"]}</td>
        </tr>
        <tr>
            <td><strong>Fiber</strong></td>
            <td>{product1_data["fiber"]}</td>
            <td>{product2_data["fiber"]}</td>
        </tr>
        <tr>
            <td><strong>Calories</strong></td>
            <td>{product1_data["calories"]}</td>
            <td>{product2_data["calories"]}</td>
        </tr>
        <tr>
            <td><strong>Price</strong></td>
            <td>{product1_data["price"]}</td>
            <td>{product2_data["price"]}</td>
        </tr>
    </table>
    """
    
    st.markdown(comparison_table_html, unsafe_allow_html=True)
    
    # Ingredients Section
    st.markdown('<div class="section-header">Ingredients</div>', unsafe_allow_html=True)
    
    ingredient_col1, ingredient_col2 = st.columns(2)
    
    with ingredient_col1:
        st.markdown(f'<h3 style="color: #444444; font-size: 1.3rem;">{product1}</h3>', unsafe_allow_html=True)
        st.markdown('<ul>', unsafe_allow_html=True)
        for ingredient in product1_data["main_ingredients"]:
            st.markdown(f'<li>{ingredient}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
    
    with ingredient_col2:
        st.markdown(f'<h3 style="color: #444444; font-size: 1.3rem;">{product2}</h3>', unsafe_allow_html=True)
        st.markdown('<ul>', unsafe_allow_html=True)
        for ingredient in product2_data["main_ingredients"]:
            st.markdown(f'<li>{ingredient}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
    
    # Pros and Cons Section
    st.markdown('<div class="section-header">Pros and Cons</div>', unsafe_allow_html=True)
    
    pros_cons_col1, pros_cons_col2 = st.columns(2)
    
    with pros_cons_col1:
        st.markdown(f'<h3 style="color: #444444; font-size: 1.3rem;">{product1}</h3>', unsafe_allow_html=True)
        st.markdown('<div class="pros-cons-box">', unsafe_allow_html=True)
        st.markdown('<div class="pros-title">✓ Pros</div>', unsafe_allow_html=True)
        st.markdown('<ul class="pros-cons-list">', unsafe_allow_html=True)
        for pro in product1_data["pros"]:
            st.markdown(f'<li>{pro}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        
        st.markdown('<div class="cons-title">✗ Cons</div>', unsafe_allow_html=True)
        st.markdown('<ul class="pros-cons-list">', unsafe_allow_html=True)
        for con in product1_data["cons"]:
            st.markdown(f'<li>{con}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with pros_cons_col2:
        st.markdown(f'<h3 style="color: #444444; font-size: 1.3rem;">{product2}</h3>', unsafe_allow_html=True)
        st.markdown('<div class="pros-cons-box">', unsafe_allow_html=True)
        st.markdown('<div class="pros-title">✓ Pros</div>', unsafe_allow_html=True)
        st.markdown('<ul class="pros-cons-list">', unsafe_allow_html=True)
        for pro in product2_data["pros"]:
            st.markdown(f'<li>{pro}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        
        st.markdown('<div class="cons-title">✗ Cons</div>', unsafe_allow_html=True)
        st.markdown('<ul class="pros-cons-list">', unsafe_allow_html=True)
        for con in product2_data["cons"]:
            st.markdown(f'<li>{con}</li>', unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Recommendation Section
    st.markdown('<div class="section-header">Our Recommendation</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
    
    # Simple recommendation logic based on ratings
    if float(product1_data["rating"]) > float(product2_data["rating"]):
        st.markdown(f'<div class="recommendation-title">We Recommend: {product1}</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <p class="recommendation-text">
            Based on our analysis, <strong>{product1}</strong> is the better choice for most cats. 
            It has a higher rating ({product1_data["rating"]} vs {product2_data["rating"]}) with more positive reviews from cat owners.
            It's particularly good for cats that need {", ".join(product1_data["suitable_for"]).lower()}.
        </p>
        """, unsafe_allow_html=True)
    elif float(product2_data["rating"]) > float(product1_data["rating"]):
        st.markdown(f'<div class="recommendation-title">We Recommend: {product2}</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <p class="recommendation-text">
            Based on our analysis, <strong>{product2}</strong> is the better choice for most cats. 
            It has a higher rating ({product2_data["rating"]} vs {product1_data["rating"]}) with more positive reviews from cat owners.
            It's particularly good for cats that need {", ".join(product2_data["suitable_for"]).lower()}.
        </p>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="recommendation-title">Both Are Great Options</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <p class="recommendation-text">
            Both <strong>{product1}</strong> and <strong>{product2}</strong> have similar ratings and are highly recommended by cat owners.
            Your choice should depend on your cat's specific needs:
            <br><br>
            • If your cat needs {", ".join(product1_data["suitable_for"]).lower()}, choose <strong>{product1}</strong>.
            <br>
            • If your cat needs {", ".join(product2_data["suitable_for"]).lower()}, choose <strong>{product2}</strong>.
        </p>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add buttons to add to cart
    add_cart_col1, add_cart_col2 = st.columns(2)
    
    with add_cart_col1:
        st.button(f"Add {product1} to Cart", use_container_width=True)
        
    with add_cart_col2:
        st.button(f"Add {product2} to Cart", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)