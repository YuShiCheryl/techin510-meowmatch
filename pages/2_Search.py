import streamlit as st

st.title('Search Page')

# Ingredient filter
ingredient = st.text_input('Filter by Ingredient')

# Taste filter
taste = st.selectbox('Filter by Taste', ['Sweet', 'Sour', 'Bitter', 'Salty', 'Umami'])

# Display results based on filters
if ingredient or taste:
    st.write(f'Showing results for Ingredient: {ingredient}, Taste: {taste}')
else:
    st.write('Please enter an ingredient or select a taste to filter results.') 