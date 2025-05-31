import streamlit as st
from datetime import date

def init_session_state():
    """Initialize session state with default values if not already present"""
    
    # User profile data
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {
            'pet_name': '',
            'breed': '',
            'gender': '',
            'age': 0,
            'weight': 10,
            'birthday': date(2019, 5, 15),
            'activity_level': 'Moderate',
            'favorite_flavors': [],
            'allergies': [],
            'health_conditions': [],  # New field for health conditions
            'special_notes': '',
            'profile_image': None,  # PIL Image object
            'profile_image_base64': None  # Base64 string for display
        }
    
    # User preferences for recommendations
    if 'user_preferences' not in st.session_state:
        st.session_state.user_preferences = {
            'price_range': (25, 50),
            'diet_type': 'All Types',
            'age_specific': 'Adult',
            'protein_preferences': ['Chicken', 'Fish']
        }
    
    # Shopping cart
    if 'shopping_cart' not in st.session_state:
        st.session_state.shopping_cart = []

def get_user_profile():
    """Get current user profile from session state"""
    init_session_state()  # Ensure session state is initialized
    return st.session_state.user_profile

def update_user_profile(key, value):
    """Update a specific field in user profile"""
    init_session_state()
    st.session_state.user_profile[key] = value

def get_user_preferences():
    """Get user preferences for recommendations"""
    init_session_state()
    return st.session_state.user_preferences

def update_user_preferences(preferences_dict):
    """Update user preferences"""
    init_session_state()
    st.session_state.user_preferences.update(preferences_dict)

def add_to_cart(product):
    """Add product to shopping cart"""
    init_session_state()
    st.session_state.shopping_cart.append(product)

def get_cart():
    """Get shopping cart contents"""
    init_session_state()
    return st.session_state.shopping_cart

def clear_cart():
    """Clear shopping cart"""
    init_session_state()
    st.session_state.shopping_cart = []

def get_pet_display_info():
    """Get formatted pet information for display"""
    profile = get_user_profile()
    
    # Generate activity-based tags
    tags = []
    if profile['activity_level']:
        tags.append(f"{profile['activity_level']} Activity")
    
    # Health conditions tag
    if profile['health_conditions']:
        if len(profile['health_conditions']) == 1:
            tags.append(f"Has {profile['health_conditions'][0]}")
        else:
            tags.append(f"{len(profile['health_conditions'])} Health Conditions")
    else:
        tags.append("No Known Health Issues")
    
    # Allergies tag
    if profile['allergies'] and profile['allergies'] != ['None']:
        tags.append("Has Allergies")
    
    # Flavor preferences
    if len(profile['favorite_flavors']) > 0:
        flavor_text = ', '.join(profile['favorite_flavors'][:2])  # Show first 2 flavors
        if len(profile['favorite_flavors']) > 2:
            flavor_text += f" +{len(profile['favorite_flavors']) - 2} more"
        tags.append(f"Likes {flavor_text}")
    
    return {
        'name': profile['pet_name'],
        'breed': profile['breed'],
        'age': profile['age'],
        'weight': round(profile['weight'], 1),  # Round weight for display
        'gender': profile['gender'],
        'tags': tags,
        'display_text': f"{profile['breed']} • {profile['age']} years old • {round(profile['weight'], 1)} lbs",
        'profile_image_base64': profile.get('profile_image_base64', None)
    }

def calculate_health_score():
    """Calculate a health score based on profile data"""
    profile = get_user_profile()
    
    score = 85  # Base score
    
    # Age factor
    if profile['age'] <= 2:
        score += 10  # Young cats generally healthier
    elif profile['age'] <= 7:
        score += 5   # Adult cats
    else:
        score -= (profile['age'] - 7) * 3  # Senior cats may have more issues
    
    # Weight factor (assuming healthy weight range)
    weight = profile['weight']
    if 8 <= weight <= 15:
        score += 10
    elif weight < 6:
        score -= 15  # Underweight
    elif weight > 18:
        score -= 15  # Overweight
    elif weight < 8 or weight > 15:
        score -= 5   # Slightly under/overweight
    
    # Activity level factor
    activity_scores = {
        'Very High': 10,
        'High': 8,
        'Moderate': 5,
        'Low': 0,
        'Very Low': -10
    }
    score += activity_scores.get(profile['activity_level'], 0)
    
    # Health conditions factor
    health_conditions = profile.get('health_conditions', [])
    score -= len(health_conditions) * 8  # Deduct points for each condition
    
    # Allergies factor
    if profile['allergies'] == ['None']:
        score += 5
    else:
        score -= len([a for a in profile['allergies'] if a != 'None']) * 3
    
    # Cap the score between 40 and 100
    return max(40, min(100, score))

def get_profile_avatar_html():
    """Get HTML for profile avatar with image or default icon"""
    profile = get_user_profile()
    
    if profile.get('profile_image_base64'):
        return f"""
        <div class="profile-container">
            <a href="Profile" class="profile-avatar" target="_self">
                <img src="{profile['profile_image_base64']}" alt="Profile">
            </a>
        </div>
        """
    else:
        return """
        <div class="profile-container">
            <a href="Profile" class="profile-avatar" target="_self">
                <span class="profile-icon">M</span>
            </a>
        </div>
        """

def save_profile_data():
    """Save profile data (placeholder for future database integration)"""
    # This function can be expanded later to save to a database
    # For now, data is automatically saved in session state
    pass

def load_profile_data(user_id=None):
    """Load profile data (placeholder for future database integration)"""
    # This function can be expanded later to load from a database
    # For now, we use the default session state initialization
    init_session_state()
    
def reset_profile():
    """Reset profile to default values"""
    if 'user_profile' in st.session_state:
        del st.session_state.user_profile
    if 'user_preferences' in st.session_state:
        del st.session_state.user_preferences
    if 'shopping_cart' in st.session_state:
        del st.session_state.shopping_cart
    init_session_state()

# Debug functions (can be removed in production)
def show_debug_info():
    """Show debug information about session state"""
    st.sidebar.write("### Debug Info")
    st.sidebar.write("**User Profile:**")
    profile_debug = get_user_profile().copy()
    # Don't show image data in debug (too long)
    if 'profile_image' in profile_debug:
        profile_debug['profile_image'] = f"<Image object: {type(profile_debug['profile_image'])}>"
    if 'profile_image_base64' in profile_debug:
        profile_debug['profile_image_base64'] = f"<Base64 string: {len(str(profile_debug['profile_image_base64']))} chars>"
    st.sidebar.json(profile_debug)
    st.sidebar.write("**Preferences:**")
    st.sidebar.json(get_user_preferences())
    st.sidebar.write(f"**Cart Items:** {len(get_cart())}")

def export_session_data():
    """Export session data as JSON (for debugging or backup)"""
    import json
    data = {
        'user_profile': st.session_state.get('user_profile', {}),
        'user_preferences': st.session_state.get('user_preferences', {}),
        'shopping_cart': st.session_state.get('shopping_cart', [])
    }
    # Remove image data from export (too large)
    if 'profile_image' in data['user_profile']:
        data['user_profile']['profile_image'] = "<Image data excluded>"
    if 'profile_image_base64' in data['user_profile']:
        data['user_profile']['profile_image_base64'] = "<Base64 data excluded>"
    
    return json.dumps(data, default=str, indent=2)