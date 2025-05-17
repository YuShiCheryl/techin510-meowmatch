import streamlit as st
from PIL import Image
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Pet Profile - MeowMatch",
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

# Create placeholder image
def create_placeholder_image(width, height, color):
    return Image.new('RGB', (width, height), color)

# Pet profile image
pet_image = create_placeholder_image(300, 300, '#FFE6E6')

# Custom CSS
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
    
    /* Page header */
    .page-header {
        text-align: left;
        margin-bottom: 2.5rem;
        position: relative;
    }
    
    .profile-header {
        color: #444444;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .profile-subheader {
        color: #666666;
        font-size: 1.2rem;
        font-weight: 500;
        margin-top: 0.5rem;
    }
    
    /* Section container */
    .section-container {
        background: #FFFFFF;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(255, 107, 149, 0.1);
        margin: 2rem 0;
        overflow: hidden;
        border: 1px solid rgba(255, 107, 149, 0.1);
        transition: all 0.3s ease;
    }
    
    .section-container:hover {
        box-shadow: 0 12px 40px rgba(255, 107, 149, 0.15);
        transform: translateY(-5px);
    }
    
    /* Section header */
    .section-header {
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        padding: 1.5rem 2rem;
        position: relative;
    }
    
    .section-title {
        color: white;
        font-size: 1.4rem;
        font-weight: 700;
        margin: 0;
    }
    
    /* Section content */
    .section-content {
        padding: 2rem;
    }
    
    /* Pet photo container */
    .pet-photo-container {
        position: relative;
        width: 100%;
        margin-bottom: 1.5rem;
    }
    
    .pet-photo {
        width: 100%;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.15);
        transition: all 0.4s ease;
    }
    
    .pet-photo-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 107, 149, 0.05);
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: all 0.3s ease;
    }
    
    .pet-photo-container:hover .pet-photo-overlay {
        opacity: 1;
    }
    
    .photo-upload-button {
        background: rgba(255, 255, 255, 0.9);
        border: none;
        border-radius: 30px;
        padding: 0.8rem 1.5rem;
        color: #FF6B95;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 107, 149, 0.2);
    }
    
    .photo-upload-button:hover {
        background: white;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(255, 107, 149, 0.3);
    }
    
    /* Upload box */
    .upload-box {
        border: 2px dashed rgba(255, 107, 149, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin: 1rem 0;
        transition: all 0.3s ease;
        background: rgba(255, 107, 149, 0.05);
    }
    
    .upload-box:hover {
        border-color: rgba(255, 107, 149, 0.6);
        background: rgba(255, 107, 149, 0.08);
    }
    
    /* Stat card */
    .stat-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF5F7 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(255, 107, 149, 0.08);
        border: 1px solid rgba(255, 107, 149, 0.1);
        height: 100%;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.4s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(255, 107, 149, 0.12);
    }
    
    .stat-card:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }
    
    .stat-number {
        color: #FF6B95;
        font-size: 2.2rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: #666666;
        font-size: 1rem;
        font-weight: 500;
    }
    
    /* Form styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 10px !important;
        border: 1px solid rgba(255, 107, 149, 0.3) !important;
        padding: 0.75rem 1rem !important;
        box-shadow: 0 4px 15px rgba(255, 107, 149, 0.05) !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border: 1px solid rgba(255, 107, 149, 0.8) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 149, 0.1) !important;
    }
    
    .stSelectbox > div > div > div,
    .stDateInput > div > div > div,
    .stMultiselect > div > div > div {
        border-radius: 10px !important;
        border: 1px solid rgba(255, 107, 149, 0.3) !important;
        box-shadow: 0 4px 15px rgba(255, 107, 149, 0.05) !important;
    }
    
    .stDateInput > div > div > div {
        padding: 0.3rem 1rem !important;
    }
    
    /* Table styling */
    .stDataFrame {
        border-radius: 15px !important;
        overflow: hidden !important;
        border: 1px solid rgba(255, 107, 149, 0.1) !important;
        box-shadow: 0 8px 20px rgba(255, 107, 149, 0.08) !important;
    }
    
    .stDataFrame table {
        border-collapse: separate !important;
        border-spacing: 0 !important;
        width: 100% !important;
    }
    
    .stDataFrame th {
        background-color: #FFF5F7 !important;
        color: #FF6B95 !important;
        font-weight: 600 !important;
        padding: 1rem !important;
        text-align: left !important;
        border-bottom: 1px solid rgba(255, 107, 149, 0.1) !important;
    }
    
    .stDataFrame td {
        padding: 1rem !important;
        border-bottom: 1px solid rgba(255, 107, 149, 0.1) !important;
        color: #666666 !important;
    }
    
    /* Slider styling */
    .stSlider > div > div > div > div {
        background-color: #FF6B95 !important;
    }
    
    /* Save button */
    .save-button {
        background: linear-gradient(90deg, #FF6B95 0%, #FF9EB5 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.8rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        border: none !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        box-shadow: 0 8px 25px rgba(255, 107, 149, 0.2) !important;
        letter-spacing: 0.5px !important;
    }
    
    .save-button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 30px rgba(255, 107, 149, 0.3) !important;
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
    .profile-footer {
        text-align: center;
        margin-top: 3rem;
        color: #666666;
        padding: 1.5rem 0;
        border-top: 1px solid rgba(255, 107, 149, 0.1);
    }
</style>

<!-- Profile Avatar -->
<div class="profile-container">
    <a href="/" class="profile-avatar" target="_self">
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

# Page header
st.markdown("""
<div class="page-header fade-in">
    <h1 class="profile-header">Pet Profile</h1>
    <p class="profile-subheader">Manage your cat's information, health records, and preferences</p>
</div>
""", unsafe_allow_html=True)

# Basic Information Section
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Basic Information</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

# Profile photo and basic info
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown('<div class="pet-photo-container">', unsafe_allow_html=True)
    st.image(pet_image, use_column_width=True, output_format="PNG")
    st.markdown('</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose a photo", type=['png', 'jpg', 'jpeg'], key="profile_pic")
    
    if uploaded_file is not None:
        # Display the uploaded image if available
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
with col2:
    col_a, col_b = st.columns(2)
    with col_a:
        st.text_input("Pet Name", value="Whiskers", placeholder="Enter your pet's name")
        st.date_input("Birthday")
        st.number_input("Weight (lbs)", min_value=0.0, max_value=30.0, value=10.0, step=0.1)
    with col_b:
        st.selectbox("Breed", ["Persian", "Siamese", "Maine Coon", "Scottish Fold", "Bengal", "Ragdoll", "Other"])
        st.selectbox("Gender", ["Male", "Female"])
        st.number_input("Age (years)", min_value=0, max_value=30, value=5)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Health Statistics Section
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Health Statistics</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

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
st.markdown('</div>', unsafe_allow_html=True)

# Medical History Section
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Medical History</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

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

# Add record button
col1, col2, col3 = st.columns([4, 2, 4])
with col2:
    st.button("+ Add New Record", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Diet Preferences Section
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Diet Preferences</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

diet_col1, diet_col2 = st.columns(2)

with diet_col1:
    st.markdown('<p style="font-weight: 600; margin-bottom: 0.5rem;">Favorite Flavors</p>', unsafe_allow_html=True)
    favorite_flavors = st.multiselect(
        "",
        ["Chicken", "Fish", "Beef", "Turkey", "Salmon", "Tuna", "Duck", "Lamb", "Venison"],
        ["Chicken", "Fish"],
        label_visibility="collapsed"
    )
    
    st.markdown('<p style="font-weight: 600; margin: 1.5rem 0 0.5rem 0;">Food Allergies</p>', unsafe_allow_html=True)
    allergies = st.multiselect(
        "",
        ["None", "Chicken", "Fish", "Dairy", "Grain", "Beef", "Eggs", "Corn"],
        ["None"],
        label_visibility="collapsed"
    )

with diet_col2:
    st.markdown('<p style="font-weight: 600; margin-bottom: 0.5rem;">Activity Level</p>', unsafe_allow_html=True)
    activity = st.select_slider(
        "",
        options=["Very Low", "Low", "Moderate", "High", "Very High"],
        value="Moderate",
        label_visibility="collapsed"
    )
    
    st.markdown('<p style="font-weight: 600; margin: 1.5rem 0 0.5rem 0;">Special Dietary Notes</p>', unsafe_allow_html=True)
    notes = st.text_area("", placeholder="Add any special dietary requirements or preferences...", height=120, label_visibility="collapsed")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Feeding Schedule Section (New)
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Feeding Schedule</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

schedule_col1, schedule_col2 = st.columns(2)

with schedule_col1:
    st.markdown('<p style="font-weight: 600; margin-bottom: 0.5rem;">Meals Per Day</p>', unsafe_allow_html=True)
    meals_per_day = st.number_input("", min_value=1, max_value=6, value=2, label_visibility="collapsed")
    
    st.markdown('<p style="font-weight: 600; margin: 1.5rem 0 0.5rem 0;">Feeding Times</p>', unsafe_allow_html=True)
    morning_time = st.time_input("Morning", value=None, label_visibility="collapsed")
    evening_time = st.time_input("Evening", value=None, label_visibility="collapsed")

with schedule_col2:
    st.markdown('<p style="font-weight: 600; margin-bottom: 0.5rem;">Portion Size</p>', unsafe_allow_html=True)
    portion_size = st.select_slider(
        "",
        options=["Small", "Medium", "Large"],
        value="Medium",
        label_visibility="collapsed"
    )
    
    st.markdown('<p style="font-weight: 600; margin: 1.5rem 0 0.5rem 0;">Special Instructions</p>', unsafe_allow_html=True)
    feeding_notes = st.text_area("", placeholder="Add any special feeding instructions...", height=120, label_visibility="collapsed", key="feeding_notes")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Save Button
st.markdown('<div style="max-width: 400px; margin: 3rem auto;">', unsafe_allow_html=True)
if st.button("Save Profile", use_container_width=True, type="primary"):
    st.success("Profile saved successfully!")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="profile-footer">
    <p>© 2024 MeowMatch | All rights reserved</p>
</div>
""", unsafe_allow_html=True)