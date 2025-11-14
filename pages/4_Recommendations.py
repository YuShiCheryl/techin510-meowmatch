import streamlit as st
from PIL import Image
import pandas as pd
import random
from utils.session_utils import (
    init_session_state, get_user_profile, get_pet_display_info, 
    get_profile_avatar_html, get_budget_range, get_texture_preferences, 
    has_texture_preference, get_budget_category
)

# Set page configuration
st.set_page_config(
    page_title="MeowMatch - Personalized Recommendations",
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

# Initialize session state
init_session_state()

# Create placeholder images using PIL
def create_placeholder_image(width, height, color):
    img = Image.new('RGB', (width, height), color)
    return img

# Create sample images - 改为橙色系
product_image1 = create_placeholder_image(300, 300, '#FFE5D4')
product_image2 = create_placeholder_image(300, 300, '#FFEAD6')
product_image3 = create_placeholder_image(300, 300, '#FFF0E6')
product_image4 = create_placeholder_image(300, 300, '#FFF2E8')
product_image5 = create_placeholder_image(300, 300, '#FFF4EA')
product_image6 = create_placeholder_image(300, 300, '#FFF6EC')

# Enhanced cat food data with texture and budget information
recommended_products = [
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

# Enhanced function to calculate match score with budget and texture preferences
def calculate_match_score(product, user_profile, user_budget_category, user_textures, price_range=None):
    score = 70  # Base score
    
    # Breed matching
    if user_profile['breed'] in product['suitable_breeds'] or "All Breeds" in product['suitable_breeds']:
        score += 10
    
    # Age matching
    if user_profile['age'] <= 1 and "Kitten" in product['age_range']:
        score += 15
    elif 1 < user_profile['age'] <= 7 and "Adult" in product['age_range']:
        score += 15
    elif user_profile['age'] > 7 and "Senior" in product['age_range']:
        score += 15
    
    # Flavor preference matching
    user_flavors = set(user_profile['favorite_flavors'])
    product_flavors = set(product['flavors'])
    if user_flavors.intersection(product_flavors):
        score += 12
    
    # Budget category matching
    if user_budget_category == 'all' or product['budget_category'] == user_budget_category:
        score += 10
    elif user_budget_category == 'premium' and product['budget_category'] == 'luxury':
        score += 5  # Close match
    elif user_budget_category == 'budget' and product['budget_category'] == 'mid-range':
        score += 5  # Close match
    else:
        score -= 5  # Penalty for budget mismatch
    
    # Texture preference matching
    if user_textures:
        if product['texture'].lower() in [t.lower() for t in user_textures]:
            score += 8
    
    # Price range matching (if custom range provided)
    if price_range:
        if price_range[0] <= product['price'] <= price_range[1]:
            score += 5
        else:
            score -= 8  # Penalty for being outside price range
    
    # Health conditions consideration
    health_conditions = user_profile.get('health_conditions', [])
    if 'Digestive Sensitivity' in health_conditions and 'Sensitive' in product['description']:
        score += 8
    if 'Obesity' in health_conditions and 'Weight' in ' '.join(product['tags']):
        score += 8
    if 'Senior Cat Special Needs' in health_conditions and 'Senior' in product['age_range']:
        score += 8
    
    # Allergies consideration
    allergies = user_profile.get('allergies', [])
    for allergy in allergies:
        if allergy != 'None' and allergy.lower() in product['description'].lower():
            score -= 15  # Heavy penalty for allergens
    
    return min(score, 99)  # Cap at 99%

# Function to filter and sort products based on user profile
def get_filtered_recommendations(user_profile, price_range=None):
    user_budget_category = get_budget_category()
    user_textures = get_texture_preferences()
    
    filtered_products = []
    
    for product in recommended_products:
        # Apply budget filter if no custom price range
        if price_range:
            if price_range[0] <= product['price'] <= price_range[1]:
                product_copy = product.copy()
                product_copy['match_score'] = calculate_match_score(
                    product, user_profile, user_budget_category, user_textures, price_range
                )
                filtered_products.append(product_copy)
        else:
            # Use budget preference for filtering
            budget_range = get_budget_range()
            if budget_range[0] <= product['price'] <= budget_range[1]:
                product_copy = product.copy()
                product_copy['match_score'] = calculate_match_score(
                    product, user_profile, user_budget_category, user_textures
                )
                filtered_products.append(product_copy)
    
    # Sort by match score
    return sorted(filtered_products, key=lambda x: x['match_score'], reverse=True)

# Add custom CSS - 改为橙色主题
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

* { font-family: 'Poppins', sans-serif; }

/* 隐藏Streamlit默认UI元素 */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stDeployButton { display: none; }
div[data-testid="stToolbar"] { display: none; }

.stApp { background-color: #FFFBF7; }

.main .block-container {
    background-color: #FFFBF7;
    padding: 3rem;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

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

.main-title {
    color: #444444;
    font-size: 3rem;
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

.subtitle {
    color: #666666;
    font-size: 1.2rem;
    font-weight: 500;
    margin-bottom: 2.5rem;
    position: relative;
    z-index: 1;
    line-height: 1.7;
}

.pet-summary-card {
    background: linear-gradient(135deg, #FFFFFF 0%, #FFF8F3 100%);
    padding: 2rem;
    border-radius: 20px;
    margin: 1.5rem 0 2rem 0;
    box-shadow: 0 10px 30px rgba(255, 140, 66, 0.1);
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(255, 140, 66, 0.1);
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
    background: linear-gradient(45deg, transparent 50%, rgba(255, 140, 66, 0.05) 50%);
    border-radius: 0 0 0 100%;
}

.pet-avatar {
    width: 120px;
    height: 120px;
    border-radius: 60px;
    overflow: hidden;
    border: 4px solid white;
    box-shadow: 0 8px 25px rgba(255, 140, 66, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
}

.pet-info { flex: 1; }

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
    background: rgba(255, 140, 66, 0.1);
    color: #FF8C42;
    font-size: 0.9rem;
    font-weight: 600;
    padding: 0.4rem 1rem;
    border-radius: 20px;
}

.price-filter-card {
    background: #FFFFFF;
    border-radius: 15px;
    padding: 1.5rem;
    box-shadow: 0 6px 20px rgba(255, 140, 66, 0.08);
    border: 1px solid rgba(255, 140, 66, 0.1);
    margin-bottom: 2rem;
}

.filter-title {
    color: #444444;
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.filter-icon { color: #FF8C42; }

.product-card {
    background: #FFFFFF;
    padding: 1.8rem;
    border-radius: 18px;
    transition: all 0.4s ease;
    box-shadow: 0 8px 25px rgba(255, 140, 66, 0.08);
    border: 1px solid rgba(255, 140, 66, 0.1);
    position: relative;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
    margin-bottom: 2rem;
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

.match-badge {
    position: absolute;
    top: 1.2rem;
    right: 1.2rem;
    background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
    color: white;
    font-size: 1rem;
    font-weight: 700;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(255, 140, 66, 0.2);
    z-index: 2;
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
    color: #FF8C42;
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
    background: rgba(255, 140, 66, 0.1);
    color: #FF8C42;
    font-size: 0.85rem;
    font-weight: 600;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
}

.product-details {
    background: rgba(255, 140, 66, 0.05);
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    border-left: 4px solid #FF8C42;
}

.product-detail-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

.product-detail-label {
    color: #666666;
    font-weight: 600;
}

.product-detail-value {
    color: #FF8C42;
    font-weight: 600;
}

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
    background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
    border-radius: 2px;
}

.stSlider > div > div > div > div { background-color: #FF8C42 !important; }

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

.fade-in { animation: fadeIn 0.5s ease-in; }

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

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
</style>
""", unsafe_allow_html=True)

# Profile Avatar
st.markdown(get_profile_avatar_html(), unsafe_allow_html=True)

# Back button - 改为Streamlit按钮
st.markdown('<div class="back-button-streamlit">', unsafe_allow_html=True)
if st.button("← Back to Home", key="back_home"):
    st.switch_page("app.py")
st.markdown('</div>', unsafe_allow_html=True)

# Page title
st.markdown('<h1 class="main-title fade-in">Personalized Recommendations</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle fade-in">Discover the perfect cat food based on your pet\'s unique needs and preferences.</p>', unsafe_allow_html=True)

# Pet summary card using session state data
user_profile = get_user_profile()
pet_info = get_pet_display_info()

# Create pet avatar HTML with user's uploaded image or placeholder
if pet_info.get('profile_image_base64'):
    pet_avatar_html = f'<img src="{pet_info["profile_image_base64"]}" width="120" height="120" style="border-radius: 60px; object-fit: cover;">'
else:
    pet_avatar_html = '<div style="width: 120px; height: 120px; background: #FFE5D4; border-radius: 60px; display: flex; align-items: center; justify-content: center; font-size: 48px;">🐱</div>'

st.markdown(f"""
<div class="pet-summary-card fade-in">
    <div class="pet-avatar">
        {pet_avatar_html}
    </div>
    <div class="pet-info">
        <div class="pet-name">{pet_info['name']}</div>
        <div class="pet-details">{pet_info['display_text']}</div>
        <div class="pet-tags">
            {' '.join([f'<span class="pet-tag">{tag}</span>' for tag in pet_info['tags']])}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Price range filter (optional override)
st.markdown("""
<div class="price-filter-card">
    <div class="filter-title">
        <span class="filter-icon">💰</span> Custom Price Range (Optional)
    </div>
    <p style="color: #666666; margin-bottom: 1rem; font-size: 0.9rem;">
        Leave unchanged to use your profile budget preference, or adjust to override.
    </p>
</div>
""", unsafe_allow_html=True)

# Get budget range from profile as default
default_budget_range = get_budget_range()
price_range = st.slider(
    "Price Range", 
    5, 80, 
    default_budget_range, 
    label_visibility="collapsed", 
    format="$%d",
    help="Drag to adjust price range, or leave as-is to use your profile budget preference"
)

# Show current budget preference
budget_category = get_budget_category()
texture_prefs = get_texture_preferences()

st.markdown(f"""
<div style="background: rgba(255, 140, 66, 0.05); padding: 1rem; border-radius: 8px; margin-bottom: 2rem; border-left: 4px solid #FF8C42;">
    <p style="margin: 0; color: #666666; font-size: 0.9rem;">
        <strong>Using preferences from your profile:</strong><br>
        💰 Budget: {user_profile.get('budget_preference', 'Mid-Range ($15-30)')}<br>
        🥄 Textures: {', '.join(texture_prefs) if texture_prefs else 'No specific preference'}<br>
        🍗 Flavors: {', '.join(user_profile.get('favorite_flavors', [])) if user_profile.get('favorite_flavors') else 'No specific preference'}
    </p>
</div>
""", unsafe_allow_html=True)

# Check if user is using custom price range
using_custom_range = price_range != default_budget_range
custom_range = price_range if using_custom_range else None

# Get filtered and sorted recommendations
filtered_products = get_filtered_recommendations(user_profile, custom_range)

if len(filtered_products) == 0:
    st.warning("No products match your current filters. Try adjusting your price range.")
else:
    # Top Recommendations section
    st.markdown('<div class="section-header">Top Recommendations</div>', unsafe_allow_html=True)
    recommendation_subtitle = f'Based on {user_profile["pet_name"]}\'s profile'
    if using_custom_range:
        recommendation_subtitle += f' and custom price range (${price_range[0]}-${price_range[1]})'
    else:
        recommendation_subtitle += f' and budget preference ({user_profile.get("budget_preference", "Mid-Range")})'
    
    st.markdown(f'<p style="color: #666666; margin-bottom: 2rem;">{recommendation_subtitle}</p>', unsafe_allow_html=True)
    
    # Display top 3 recommendations
    top_recommendations = filtered_products[:3]
    for i, product in enumerate(top_recommendations):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(product["image"], width=300)
        
        with col2:
            st.markdown(f"""
            <div class="product-card">
                <div class="match-badge">{product["match_score"]}%</div>
                <div class="product-title">{product["name"]}</div>
                <div class="product-description">{product["description"]}</div>
                <div class="product-details">
                    <div class="product-detail-row">
                        <span class="product-detail-label">Texture:</span>
                        <span class="product-detail-value">{product["texture"]}</span>
                    </div>
                    <div class="product-detail-row">
                        <span class="product-detail-label">Budget Category:</span>
                        <span class="product-detail-value">{product["budget_category"].title()}</span>
                    </div>
                    <div class="product-detail-row">
                        <span class="product-detail-label">Primary Flavors:</span>
                        <span class="product-detail-value">{', '.join(product["flavors"])}</span>
                    </div>
                </div>
                <div class="product-price">${product["price"]}</div>
                <div class="product-rating">
                    {"⭐" * int(product["rating"])}{"<span style='color:#DDDDDD'>☆</span>" * (5-int(product["rating"]))}
                    <span class="rating-count">({product["reviews"]} reviews)</span>
                </div>
                <div class="product-tags">
                    {" ".join([f'<span class="product-tag">{tag}</span>' for tag in product["tags"]])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Add to Cart", key=f"cart_{i}", use_container_width=True):
                st.success(f"Added {product['name']} to cart!")
    
    # Also Recommended section
    if len(filtered_products) > 3:
        st.markdown('<div class="section-header">Also Recommended</div>', unsafe_allow_html=True)
        st.markdown('<p style="color: #666666; margin-bottom: 2rem;">Other great options that match your preferences</p>', unsafe_allow_html=True)
        
        # Display remaining recommendations in a grid
        remaining_products = filtered_products[3:]
        
        # Display in rows of 2
        for i in range(0, len(remaining_products), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(remaining_products):
                    product = remaining_products[i + j]
                    with col:
                        st.image(product["image"], width=300)
                        st.markdown(f"""
                        <div class="product-card">
                            <div class="match-badge">{product["match_score"]}%</div>
                            <div class="product-title">{product["name"]}</div>
                            <div class="product-description">{product["description"]}</div>
                            <div class="product-details">
                                <div class="product-detail-row">
                                    <span class="product-detail-label">Texture:</span>
                                    <span class="product-detail-value">{product["texture"]}</span>
                                </div>
                                <div class="product-detail-row">
                                    <span class="product-detail-label">Budget:</span>
                                    <span class="product-detail-value">{product["budget_category"].title()}</span>
                                </div>
                                <div class="product-detail-row">
                                    <span class="product-detail-label">Flavors:</span>
                                    <span class="product-detail-value">{', '.join(product["flavors"])}</span>
                                </div>
                            </div>
                            <div class="product-price">${product["price"]}</div>
                            <div class="product-rating">
                                {"⭐" * int(product["rating"])}{"<span style='color:#DDDDDD'>☆</span>" * (5-int(product["rating"]))}
                                <span class="rating-count">({product["reviews"]} reviews)</span>
                            </div>
                            <div class="product-tags">
                                {" ".join([f'<span class="product-tag">{tag}</span>' for tag in product["tags"]])}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"Add to Cart", key=f"cart_additional_{i+j}", use_container_width=True):
                            st.success(f"Added {product['name']} to cart!")

# Show recommendation insights
st.markdown('<div class="section-header">Why These Recommendations?</div>', unsafe_allow_html=True)

insights_col1, insights_col2 = st.columns(2)

with insights_col1:
    st.markdown("""
    <div style="background: rgba(255, 140, 66, 0.05); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #FF8C42;">
        <h4 style="color: #FF8C42; margin-bottom: 1rem;">🎯 Match Factors</h4>
        <ul style="color: #666666; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
            <li><strong>Age & Life Stage:</strong> Products suited for your cat's age</li>
            <li><strong>Flavor Preferences:</strong> Matches your cat's favorite flavors</li>
            <li><strong>Budget Range:</strong> Fits within your preferred budget</li>
            <li><strong>Texture Preferences:</strong> Includes your cat's preferred textures</li>
            <li><strong>Health Considerations:</strong> Addresses any health conditions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with insights_col2:
    st.markdown("""
    <div style="background: rgba(255, 140, 66, 0.05); padding: 1.5rem; border-radius: 15px; border-left: 4px solid #FF8C42;">
        <h4 style="color: #FF8C42; margin-bottom: 1rem;">💡 Personalization Tips</h4>
        <ul style="color: #666666; line-height: 1.8; margin: 0; padding-left: 1.5rem;">
            <li>Update your cat's profile for better matches</li>
            <li>Try different texture preferences</li>
            <li>Adjust budget settings for more options</li>
            <li>Add health conditions for specialized recommendations</li>
            <li>Rate products to improve future suggestions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Debug info (can be removed in production)
if st.checkbox("Show Recommendation Details"):
    st.write(f"**Showing {len(filtered_products)} products matching your criteria**")
    st.write(f"**Budget Category:** {budget_category}")
    st.write(f"**Budget Range:** ${default_budget_range[0]} - ${default_budget_range[1]}")
    if using_custom_range:
        st.write(f"**Custom Price Range:** ${price_range[0]} - ${price_range[1]}")
    st.write(f"**Texture Preferences:** {texture_prefs if texture_prefs else 'None specified'}")
    st.write(f"**Flavor Preferences:** {user_profile.get('favorite_flavors', [])}")
    st.write(f"**Health Conditions:** {user_profile.get('health_conditions', [])}")

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 MeowMatch | All rights reserved | Purr-fect nutrition, purr-fect love</p>
</div>
""", unsafe_allow_html=True)