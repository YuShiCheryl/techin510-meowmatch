MeowMatch - Cat Food Recommendation System 🐱
MeowMatch is a web application that helps cat owners find the perfect food recommendations for their beloved feline friends. The application features a modern, user-friendly interface with personalized food suggestions and product showcases.

Features ✨
Modern and responsive user interface
Featured product showcase
Personalized food recommendations based on cat profiles
Product comparison with nutritional analysis
Ingredient-based search functionality
Beautiful design with smooth animations
Mobile-friendly layout
1. Project Scope
MeowMatch is a platform that offers personalized cat food and canned meal recommendations. The idea is to evaluate nutritional content, compare ingredients across brands, and track the cat's flavor preferences to ensure that future suggestions align with each pet's dietary needs based on their age, weight, health, and activity level.

The project is dedicated to helping cat owners make informed feeding choices tailored to their pet's unique needs.

2. Target Users
Cat Owners
Especially new owners or those highly conscious about their cat's health.

Owners with Special Requirements
Those managing pets with dietary challenges such as sensitive stomachs, obesity, or chronic conditions.

3. Key Features
🥩 Ingredients & Comparison
Ingredient listings and descriptions with benefits and risks.
Nutritional comparison tools (protein, fat, carbs, vitamins, etc.).
Side-by-side product comparisons for informed decision-making.
🏥 Health Data Input
Age, weight, and activity level inputs.
Support for cats with allergies or chronic conditions.
Personalized recommendations based on health metrics.
😺 Taste and Budget Considerations
Taste profiling (likes/dislikes).
Budget filters to match product recommendations within spending limits.
Value-for-money analysis.
🔍 Advanced Search & Popularity
Search/filter by ingredient or nutrients.
Popularity metrics (ratings, trends).
🎯 Informed, Tailored Recommendations
Algorithmic matching of nutritional needs and user preferences.
System that improves with continuous user feedback.
🤝 Social & Community Features (Future)
Match with other owners with similar dietary needs.
Trade products within the community for sustainability and connection.
4. Project Timeline and Milestones
Week	Focus	Milestone
2	Discovery & Planning	Map user journey, define features
3	Low-Fidelity UX	Sketch core screens, Figma prototyping
4	Data Integration	Build product database & mock backend
5	Basic Logic	Static views & rules-based recommendations
6	Hi-fi & Frontend	Final UI design & implement flavor tracker
7	Testing & Iteration	User testing and final refinement
5. Progress
Completed ✅
Set up virtual environment
Created basic project structure
Implemented homepage using Streamlit with:
Hero section (intro and call to action)
Featured product cards with pricing
Feature summary cards (Ingredients, Health, Budget)
Completed profile page with:
Pet information form
Health statistics display
Medical history tracking
Diet preferences and feeding schedule
Implemented search page with:
Ingredient-based filtering
Taste preference selection
Clean results display with product cards
Created compare page for side-by-side product analysis:
Nutritional information comparison
Pros and cons analysis
Recommendation engine
Developed recommendation page:
Personalized food suggestions
Match percentage indicators
Filtering options
Product grid display
Collected cat food ingredient database from various sources
Unified design system across all pages for consistent user experience
Applied responsive design principles for better usability
In Progress 🔄
Connecting profile form input to backend state management
Improving mobile responsiveness of comparison page
Refining the recommendation algorithm
Enhancing error handling and form validation
Next Steps 🟡
Implement user authentication for saving profiles and preferences
Add favorites/saved products functionality
Create loading states for smoother transitions
Add tooltips for nutritional information
Integrate ingredient database with recommendation algorithm
Replace placeholder product data with real items
Fix reported bugs in search filters and profile image upload
6. Known Issues
Profile Page: Image upload occasionally fails to display properly
Search Page: Filter chips sometimes remain after clearing filters
Search Page: Results occasionally show duplicate items
Compare Page: Product selection dropdowns need clearer prompts
Compare Page: Limited mobile responsiveness
Recommendation Page: Match percentage calculation needs refinement
Recommendation Page: Refresh button occasionally doesn't update the recommendations
Installation 🚀
Clone the repository:
bash
git clone https://github.com/jhuang404/techin510-meowmatch.git
cd techin510-meowmatch
Create and activate a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
Install the required packages:
bash
pip install -r requirements.txt
Usage 💻
To run the application locally:

bash
streamlit run app.py
The application will open in your default web browser at http://localhost:8501.

Page Navigation
Homepage: This is the landing page with featured products and key benefits
Profile Page: Create and manage your cat's profile and preferences (/Profile)
Search Page: Find cat food by specific ingredients or attributes (/Search)
Compare Page: Side-by-side comparison of cat food products (/Compare)
Recommendation Page: View personalized food suggestions based on your cat's profile (/Recommendation)
Project Structure
techin510-meowmatch/
├── app.py                  # Main application file
├── pages/                  # Streamlit multipage app structure
│   ├── Profile.py          # Cat profile management page
│   ├── Search.py           # Search and filtering page
│   ├── Compare.py          # Product comparison page
│   └── Recommendation.py   # Personalized recommendations page
├── data/                   # Data files
│   └── cat_food_db.json    # Sample cat food database
├── assets/                 # Static assets
│   └── images/             # Image files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
Contributing 🤝
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
Future Work 🔮
Implement user accounts for saving preferences
Add machine learning model to improve recommendations over time
Develop a mobile app version
Create a community feature for cat owners to share experiences
Integrate with online retailers for direct purchasing
