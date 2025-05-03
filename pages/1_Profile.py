import streamlit as st
from PIL import Image
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Pet Profile - MeowMatch",
    page_icon="🐱",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
    }
    
    .profile-container {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border: 1px solid #e0e0e0;
    }
    
    .profile-header {
        color: #000000;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .section-title {
        color: #000000;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #ffb3b3;
    }
    
    .stat-card {
        background-color: #fff5f5;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #ffe6e6;
    }
    
    .stat-number {
        color: #e60000;
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    .stat-label {
        color: #666666;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    .history-item {
        padding: 1rem;
        border-bottom: 1px solid #eeeeee;
        margin: 0.5rem 0;
    }
    
    .upload-box {
        border: 2px dashed #cccccc;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Create placeholder image
def create_placeholder_image(width, height, color):
    return Image.new('RGB', (width, height), color)

# Header
st.markdown('<h1 class="profile-header">🐱 Pet Profile</h1>', unsafe_allow_html=True)

# Main profile container
with st.container():
    st.markdown('<div class="profile-container">', unsafe_allow_html=True)
    
    # Profile photo and basic info
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(create_placeholder_image(300, 300, '#FFE0E0'), use_column_width=True)
        st.markdown('<div class="upload-box">', unsafe_allow_html=True)
        st.file_uploader("Upload new photo", type=['png', 'jpg', 'jpeg'])
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        # Basic Information
        st.markdown('<div class="section-title">Basic Information</div>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Pet Name", value="Whiskers")
            st.date_input("Birthday")
            st.number_input("Weight (lbs)", min_value=0.0, max_value=30.0, value=10.0)
        with col_b:
            st.selectbox("Breed", ["Persian", "Siamese", "Maine Coon", "Other"])
            st.selectbox("Gender", ["Male", "Female"])
            st.number_input("Age (years)", min_value=0, max_value=30, value=5)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Health Stats
st.markdown('<div class="profile-container">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Health Statistics</div>', unsafe_allow_html=True)
stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">10.5</div>
        <div class="stat-label">Current Weight (lbs)</div>
    </div>
    """, unsafe_allow_html=True)

with stat_col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Vet Visits This Year</div>
    </div>
    """, unsafe_allow_html=True)

with stat_col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">85%</div>
        <div class="stat-label">Health Score</div>
    </div>
    """, unsafe_allow_html=True)

with stat_col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">2</div>
        <div class="stat-label">Active Medications</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Medical History
st.markdown('<div class="profile-container">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Medical History</div>', unsafe_allow_html=True)

# Sample medical history data
medical_history = pd.DataFrame({
    'Date': ['2024-03-15', '2024-02-01', '2024-01-10'],
    'Type': ['Vaccination', 'Check-up', 'Dental Cleaning'],
    'Notes': [
        'Annual vaccination renewal',
        'Regular health check - all normal',
        'Professional dental cleaning and check-up'
    ]
})

st.dataframe(medical_history, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Diet Preferences
st.markdown('<div class="profile-container">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Diet Preferences</div>', unsafe_allow_html=True)

diet_col1, diet_col2 = st.columns(2)

with diet_col1:
    st.multiselect(
        "Favorite Flavors",
        ["Chicken", "Fish", "Beef", "Turkey", "Salmon", "Tuna"],
        ["Chicken", "Fish"]
    )
    st.multiselect(
        "Food Allergies",
        ["None", "Chicken", "Fish", "Dairy", "Grain", "Beef"],
        ["None"]
    )

with diet_col2:
    st.select_slider(
        "Activity Level",
        options=["Very Low", "Low", "Moderate", "High", "Very High"],
        value="Moderate"
    )
    st.text_area("Special Dietary Notes", height=100)

st.markdown('</div>', unsafe_allow_html=True)

# Save Button
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("💾 Save Profile", use_container_width=True):
        st.success("Profile saved successfully!") 