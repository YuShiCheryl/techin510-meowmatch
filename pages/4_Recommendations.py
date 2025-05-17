import streamlit as st
import pandas as pd
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Your Recommendations - MeowMatch",
    page_icon="🐱",
    layout="wide"
)

# Custom CSS for recommendations page
st.markdown("""
<style>
    .recommendation-container {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .recommendation-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .recommendation-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .match-score {
        font-size: 1.2rem;
        font-weight: bold;
        color: #28a745;
    }
    
    .feature-tag {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.9rem;
        margin: 0.2rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Page title
st.title("🐱 Your Personalized Recommendations")

# Get profile data from session state (this would be populated from the profile page)
# For now, we'll use some default values
profile_data = {
    "name": "Whiskers",
    "age": 5,
    "weight": 10.5,
    "breed": "Persian",
    "activity_level": "Moderate",
    "favorite_flavors": ["Chicken", "Fish"],
    "allergies": ["None"],
    "health_score": 85,
    "special_notes": ""
}

# Display profile summary
st.markdown("### Based on Whiskers' Profile")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Age", f"{profile_data['age']} years")
    st.metric("Weight", f"{profile_data['weight']} lbs")

with col2:
    st.metric("Activity Level", profile_data['activity_level'])
    st.metric("Health Score", f"{profile_data['health_score']}%")

with col3:
    st.metric("Favorite Flavors", ", ".join(profile_data['favorite_flavors']))
    st.metric("Allergies", ", ".join(profile_data['allergies']))

# Recommendation function (replace with your actual recommendation logic)
def get_recommendations(profile):
    # This is placeholder data - replace with your actual recommendation system
    recommendations = [
        {
            "name": "Royal Canin Persian",
            "match_score": 98,
            "price": "$29.9/kg",
            "type": "Dry Food",
            "features": ["Breed Specific", "Hairball Control", "Digestive Health"],
            "image": "https://via.placeholder.com/150",
            "description": "Specially formulated for Persian cats with balanced nutrition and hairball control.",
            "why_match": "Perfect match for Persian breed with hairball control and digestive support."
        },
        {
            "name": "Hill's Science Diet Indoor",
            "match_score": 92,
            "price": "$25.9/kg",
            "type": "Dry Food",
            "features": ["Weight Management", "Digestive Health", "Chicken Flavor"],
            "image": "https://via.placeholder.com/150",
            "description": "Supports healthy weight and digestion with premium chicken protein.",
            "why_match": "Matches your cat's moderate activity level and chicken preference."
        },
        {
            "name": "Blue Buffalo Indoor Health",
            "match_score": 88,
            "price": "$32.9/kg",
            "type": "Dry Food",
            "features": ["Natural Ingredients", "Hairball Control", "Fish Flavor"],
            "image": "https://via.placeholder.com/150",
            "description": "Natural ingredients with added vitamins and minerals, featuring fish flavor.",
            "why_match": "Includes your cat's preferred fish flavor with natural ingredients."
        }
    ]
    return recommendations

# Get and display recommendations
recommendations = get_recommendations(profile_data)

st.markdown("### Recommended Products")
for rec in recommendations:
    with st.container():
        st.markdown('<div class="recommendation-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(rec["image"], width=150)
        
        with col2:
            st.markdown(f"#### {rec['name']}")
            st.markdown(f"**Match Score:** {rec['match_score']}%")
            st.markdown(f"**Price:** {rec['price']}")
            st.markdown(f"**Type:** {rec['type']}")
            
            # Display features as tags
            feature_tags = " ".join([f'<span class="feature-tag">{feature}</span>' for feature in rec['features']])
            st.markdown(feature_tags, unsafe_allow_html=True)
            
            st.markdown(rec['description'])
            st.markdown(f"**Why this matches:** {rec['why_match']}")
            
            # Add to cart button
            if st.button(f"Add to Cart", key=rec['name']):
                st.success(f"Added {rec['name']} to cart!")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Additional Information
st.markdown("---")
st.markdown("### About These Recommendations")
st.markdown("""
Our recommendation system analyzes your cat's profile to find the best matches based on:
- Breed-specific nutritional needs
- Age and weight considerations
- Activity level and lifestyle
- Flavor preferences
- Health requirements
- Dietary restrictions

The match score indicates how well each product aligns with your cat's specific needs.
""") 