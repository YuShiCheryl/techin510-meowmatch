import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime, date
import base64
import io
from session_utils import init_session_state, get_user_profile, update_user_profile, get_profile_avatar_html

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


# Initialize session state
init_session_state()

# Function to convert PIL image to base64
def pil_to_base64(img):
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

# Create placeholder image
def create_placeholder_image(width, height, color):
    return Image.new('RGB', (width, height), color)

# Pet profile image
pet_image = create_placeholder_image(300, 300, '#FFE5D4')

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
    
    /* Back button styling for Streamlit - 改为橙色样式 */
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
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
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
        box-shadow: 0 8px 30px rgba(255, 140, 66, 0.1);
        margin: 2rem 0;
        overflow: hidden;
        border: 1px solid rgba(255, 140, 66, 0.1);
        transition: all 0.3s ease;
    }
    
    .section-container:hover {
        box-shadow: 0 12px 40px rgba(255, 140, 66, 0.15);
        transform: translateY(-5px);
    }
    
    /* Section header */
    .section-header {
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
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
    
    /* Stat card */
    .stat-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF8F3 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(255, 140, 66, 0.08);
        border: 1px solid rgba(255, 140, 66, 0.1);
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
        background: linear-gradient(90deg, #FF8C42 0%, #FFB380 100%);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.4s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(255, 140, 66, 0.12);
    }
    
    .stat-card:hover::after {
        transform: scaleX(1);
        transform-origin: left;
    }
    
    .stat-number {
        color: #FF8C42;
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
        border: 1px solid rgba(255, 140, 66, 0.3) !important;
        padding: 0.75rem 1rem !important;
        box-shadow: 0 4px 15px rgba(255, 140, 66, 0.05) !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border: 1px solid rgba(255, 140, 66, 0.8) !important;
        box-shadow: 0 6px 20px rgba(255, 140, 66, 0.1) !important;
    }
    
    .stSelectbox > div > div > div,
    .stDateInput > div > div > div,
    .stMultiselect > div > div > div {
        border-radius: 10px !important;
        border: 1px solid rgba(255, 140, 66, 0.3) !important;
        box-shadow: 0 4px 15px rgba(255, 140, 66, 0.05) !important;
    }
    
    .stDateInput > div > div > div {
        padding: 0.3rem 1rem !important;
    }
    
    /* Slider styling - 橙色主题 */
    .stSlider > div > div > div > div {
        background-color: #FF8C42 !important;
    }
    
    .stSlider > div > div > div > div[data-baseweb="slider"] > div {
        background-color: #FF8C42 !important;
    }
    
    .stSlider > div > div > div > div[data-baseweb="slider"] > div > div {
        background-color: #FF8C42 !important;
    }
    
    /* Activity level select slider 橙色主题 */
    div[data-testid="stSelectSlider"] > div > div > div {
        background-color: #FF8C42 !important;
    }
    
    /* Select slider track 橙色主题 */
    .stSelectSlider > div > div > div > div {
        background-color: #FF8C42 !important;
    }
    
    /* Select slider thumb 橙色主题 */
    .stSelectSlider div[role="slider"] {
        background-color: #FF8C42 !important;
        border-color: #FF8C42 !important;
    }
    
    /* Button styling - 更新为橙色渐变按钮 */
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
    
    /* Health conditions styling */
    .health-conditions {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .health-condition-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }
    
    .health-condition-item:hover {
        background-color: rgba(255, 140, 66, 0.05);
    }
    
    /* Success message styling */
    .success-message {
        background: linear-gradient(90deg, #27AE60 0%, #2ECC71 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(39, 174, 96, 0.2);
    }
    
    /* Unsaved changes warning */
    .unsaved-warning {
        background: linear-gradient(90deg, #FF9500 0%, #FFAD33 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(255, 149, 0, 0.2);
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
""", unsafe_allow_html=True)

# Get current user profile
user_profile = get_user_profile()

# Initialize form state if not exists
if 'form_data' not in st.session_state:
    st.session_state.form_data = user_profile.copy()

# Profile Avatar (with uploaded image if available)
st.markdown(get_profile_avatar_html(), unsafe_allow_html=True)

# Back button - 改为和其他页面一样的Streamlit按钮样式
st.markdown('<div class="back-button-streamlit">', unsafe_allow_html=True)
if st.button("← Back to Home", key="back_home"):
    st.switch_page("app.py")
st.markdown('</div>', unsafe_allow_html=True)

# Page header
st.markdown(f"""
<div class="page-header fade-in">
    <h1 class="profile-header">{user_profile['pet_name']}'s Profile</h1>
    <p class="profile-subheader">Manage your cat's information, health records, and preferences</p>
</div>
""", unsafe_allow_html=True)

# Check if there are unsaved changes
def has_unsaved_changes():
    form_data = st.session_state.form_data
    for key in form_data:
        if key in user_profile and form_data[key] != user_profile[key]:
            return True
    return False

# Show unsaved changes warning
if has_unsaved_changes():
    st.markdown("""
    <div class="unsaved-warning">
        ⚠️ You have unsaved changes. Click "Save Profile" to apply your changes.
    </div>
    """, unsafe_allow_html=True)

# Basic Information Section
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Basic Information</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

# Profile photo and basic info
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Display current profile image or placeholder
    if st.session_state.form_data.get('profile_image'):
        st.image(st.session_state.form_data['profile_image'], use_container_width=True)
    else:
        st.image(pet_image, use_container_width=True, output_format="PNG")
    
    uploaded_file = st.file_uploader("Choose a photo", type=['png', 'jpg', 'jpeg'], key="profile_pic")
    
    if uploaded_file is not None:
        # Save uploaded image to form data (not session state yet)
        image = Image.open(uploaded_file)
        image_base64 = pil_to_base64(image)
        st.session_state.form_data['profile_image'] = image
        st.session_state.form_data['profile_image_base64'] = image_base64
        st.image(image, caption='New Profile Picture (Click Save to apply)', use_container_width=True)
        
with col2:
    col_a, col_b = st.columns(2)
    with col_a:
        # Pet Name input
        new_pet_name = st.text_input(
            "Pet Name", 
            value=st.session_state.form_data['pet_name'],
            placeholder="Enter your pet's name"
        )
        st.session_state.form_data['pet_name'] = new_pet_name
        
        # Birthday input
        new_birthday = st.date_input(
            "Birthday",
            value=st.session_state.form_data['birthday']
        )
        if new_birthday != st.session_state.form_data['birthday']:
            st.session_state.form_data['birthday'] = new_birthday
            # Calculate age from birthday
            today = date.today()
            age = today.year - new_birthday.year - ((today.month, today.day) < (new_birthday.month, new_birthday.day))
            st.session_state.form_data['age'] = age
        
        # Weight input with proper decimal handling
        new_weight = st.number_input(
            "Weight (lbs)", 
            min_value=0.0, 
            max_value=30.0, 
            value=float(st.session_state.form_data['weight']), 
            step=0.1,
            format="%.1f"
        )
        st.session_state.form_data['weight'] = round(new_weight, 1)
            
    with col_b:
        # Breed input - allow custom input with common options
        breed_options = [
            "Persian", "Siamese", "Maine Coon", "Scottish Fold", "Bengal", "Ragdoll", 
            "British Shorthair", "American Shorthair", "Russian Blue", "Abyssinian",
            "Birman", "Norwegian Forest Cat", "Sphinx", "Munchkin", "Other"
        ]
        
        # 处理breed的默认值
        current_breed = st.session_state.form_data.get('breed', '')
        if current_breed == '-' or not current_breed:
            current_breed = "Persian"  # 设置默认品种
        
        # Check if current breed is in options, if not add it
        if current_breed not in breed_options:
            breed_options.insert(-1, current_breed)  # Insert before "Other"
        
        breed_index = breed_options.index(current_breed) if current_breed in breed_options else 0
        
        selected_breed = st.selectbox(
            "Breed", 
            breed_options,
            index=breed_index
        )
        
        # If "Other" is selected, show text input
        if selected_breed == "Other":
            custom_breed = st.text_input(
                "Enter breed name", 
                value=current_breed if current_breed not in breed_options[:-1] else ""
            )
            if custom_breed:
                st.session_state.form_data['breed'] = custom_breed
        else:
            st.session_state.form_data['breed'] = selected_breed
        
        # Gender input
        gender_options = ["Male", "Female"]
        current_gender = st.session_state.form_data.get('gender', 'Male')
        if current_gender == '-' or current_gender not in gender_options:
            current_gender = "Male"  # 默认值
        
        current_gender_index = gender_options.index(current_gender)
        
        new_gender = st.selectbox(
            "Gender", 
            gender_options,
            index=current_gender_index
        )
        st.session_state.form_data['gender'] = new_gender

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Health Statistics Section (using current saved data)
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Health Statistics</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    # Display current saved weight (not form weight)
    weight_display = f"{user_profile['weight']:.1f}"
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{weight_display}</div>
        <div class="stat-label">Current Weight (lbs)</div>
    </div>
    """, unsafe_allow_html=True)

with stat_col2:
    # Count health conditions from saved data
    health_conditions_count = len([cond for cond in user_profile.get('health_conditions', []) if cond])
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{health_conditions_count}</div>
        <div class="stat-label">Health Conditions</div>
    </div>
    """, unsafe_allow_html=True)

with stat_col3:
    # Calculate health score based on saved data
    health_score = 100 - (health_conditions_count * 10) - max(0, (user_profile['age'] - 7) * 5)
    health_score = max(60, min(100, health_score))
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{health_score}%</div>
        <div class="stat-label">Health Score</div>
    </div>
    """, unsafe_allow_html=True)

with stat_col4:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{user_profile['age']}</div>
        <div class="stat-label">Age (years)</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Health Conditions Section
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Health Conditions</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

st.markdown('<p style="font-weight: 600; margin-bottom: 1rem; color: #666666;">Select any health conditions that apply to your cat:</p>', unsafe_allow_html=True)

# Health conditions list
health_conditions_options = [
    "Kidney Disease",
    "Urinary Tract Issues", 
    "Diabetes",
    "Obesity",
    "Digestive Sensitivity",
    "Dental Problems",
    "Senior Cat Special Needs",
    "Kitten Special Needs"
]

# Get current health conditions from form data
current_conditions = st.session_state.form_data.get('health_conditions', [])

# Create checkboxes for health conditions
new_conditions = st.multiselect(
    "",
    health_conditions_options,
    default=current_conditions,
    label_visibility="collapsed"
)
st.session_state.form_data['health_conditions'] = new_conditions

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Diet Preferences Section
st.markdown('<div class="section-container fade-in">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 class="section-title">Diet Preferences</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

diet_col1, diet_col2 = st.columns(2)

with diet_col1:
    st.markdown('<p style="font-weight: 600; margin-bottom: 0.5rem;">Favorite Flavors</p>', unsafe_allow_html=True)
    new_favorite_flavors = st.multiselect(
        "",
        ["Chicken", "Fish", "Beef", "Turkey", "Salmon", "Tuna", "Duck", "Lamb", "Venison"],
        default=st.session_state.form_data['favorite_flavors'],
        label_visibility="collapsed"
    )
    st.session_state.form_data['favorite_flavors'] = new_favorite_flavors
    
    st.markdown('<p style="font-weight: 600; margin: 1.5rem 0 0.5rem 0;">Food Allergies</p>', unsafe_allow_html=True)
    new_allergies = st.multiselect(
        "",
        ["None", "Chicken", "Fish", "Dairy", "Grain", "Beef", "Eggs", "Corn"],
        default=st.session_state.form_data['allergies'],
        label_visibility="collapsed"
    )
    st.session_state.form_data['allergies'] = new_allergies

with diet_col2:
    st.markdown('<p style="font-weight: 600; margin-bottom: 0.5rem;">Activity Level</p>', unsafe_allow_html=True)
    activity_options = ["Very Low", "Low", "Moderate", "High", "Very High"]
    
    # 处理activity_level的默认值
    current_activity = st.session_state.form_data.get('activity_level', 'Moderate')
    if not current_activity or current_activity not in activity_options:
        current_activity = "Moderate"
    
    new_activity = st.select_slider(
        "",
        options=activity_options,
        value=current_activity,
        label_visibility="collapsed"
    )
    st.session_state.form_data['activity_level'] = new_activity
    
    st.markdown('<p style="font-weight: 600; margin: 1.5rem 0 0.5rem 0;">Special Dietary Notes</p>', unsafe_allow_html=True)
    
    # 处理special_notes的默认值
    current_notes = st.session_state.form_data.get('special_notes', '')
    if current_notes == '-':
        current_notes = ''  # 将'-'替换为空字符串
    
    new_notes = st.text_area(
        "", 
        value=current_notes,
        placeholder="Add any special dietary requirements or preferences...", 
        height=120, 
        label_visibility="collapsed"
    )
    st.session_state.form_data['special_notes'] = new_notes

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Save Button
st.markdown('<div style="max-width: 400px; margin: 3rem auto;">', unsafe_allow_html=True)

# Add Cancel and Save buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Cancel Changes", use_container_width=True):
        # Reset form data to current saved data
        st.session_state.form_data = user_profile.copy()
        st.rerun()

with col2:
    if st.button("Save Profile", use_container_width=True, type="primary"):
        # Save all form data to session state
        for key, value in st.session_state.form_data.items():
            update_user_profile(key, value)
        
        st.markdown('<div class="success-message">✅ Profile saved successfully and synced to browser!</div>', unsafe_allow_html=True)
        st.balloons()
        
        # Reset form data to match saved data
        st.session_state.form_data = st.session_state.user_profile.copy()
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Debug: Show current session state (you can remove this in production)
if st.checkbox("Show Debug Info"):
    st.write("**Current Saved Profile:**")
    st.json(user_profile)
    st.write("**Form Data (Unsaved):**")
    st.json(st.session_state.form_data)
    st.write("**Has Unsaved Changes:**", has_unsaved_changes())