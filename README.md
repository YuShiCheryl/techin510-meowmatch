# MeowMatch - Cat Food Recommendation System 🐱

MeowMatch is a web application that helps cat owners find the perfect food recommendations for their beloved feline friends. The application features a modern, user-friendly interface with personalized food suggestions and product showcases.

## Features ✨

- Modern and responsive user interface
- Featured product showcase
- Personalized food recommendations
- Beautiful design with smooth animations
- Mobile-friendly layout


## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/jhuang404/techin510-project.git
cd techin510-project
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage 💻

To run the application locally:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Technologies Used 🛠️

- Python
- Streamlit
- PIL (Python Imaging Library)
- HTML/CSS

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact 📧

Yu Shi - [GitHub Profile](https://github.com/YuShiCheryl)

Project Link: [https://github.com/jhuang404/techin510-project](https://github.com/jhuang404/techin510-project)

---

## 1. Project Scope

MeowMatch is a platform that offers personalized cat food and canned meal recommendations. The idea is to evaluate nutritional content, compare ingredients across brands, and track the cat's flavor preferences to ensure that future suggestions align with each pet's dietary needs based on their age, weight, health, and activity level.

The project is dedicated to helping cat owners make informed feeding choices tailored to their pet's unique needs.

---

## 2. Target Users

**Cat Owners**  
Especially new owners or those highly conscious about their cat's health.

**Owners with Special Requirements**  
Those managing pets with dietary challenges such as sensitive stomachs, obesity, or chronic conditions.

---

## 3. Key Features

### 🥩 Ingredients & Comparison

- Ingredient listings and descriptions with benefits and risks.
- Nutritional comparison tools (protein, fat, carbs, vitamins, etc.).
- Side-by-side product comparisons for informed decision-making.

### 🏥 Health Data Input

- Age, weight, and activity level inputs.
- Support for cats with allergies or chronic conditions.
- Personalized recommendations based on health metrics.

### 😺 Taste and Budget Considerations

- Taste profiling (likes/dislikes).
- Budget filters to match product recommendations within spending limits.
- Value-for-money analysis.

### 🔍 Advanced Search & Popularity

- Search/filter by ingredient or nutrients.
- Popularity metrics (ratings, trends).

### 🎯 Informed, Tailored Recommendations

- Algorithmic matching of nutritional needs and user preferences.
- System that improves with continuous user feedback.

### 🤝 Social & Community Features

- Match with other owners with similar dietary needs.
- Trade products within the community for sustainability and connection.

---

## 4. Project Timeline and Milestones

| Week | Focus | Milestone |
|------|-------|-----------|
| 2 | Discovery & Planning | Map user journey, define features |
| 3 | Low-Fidelity UX | Sketch core screens, Figma prototyping |
| 4 | Data Integration | Build product database & mock backend |
| 5 | Basic Logic | Static views & rules-based recommendations |
| 6 | Hi-fi & Frontend | Final UI design & implement flavor tracker |
| 7 | Testing & Iteration | User testing and final refinement |

---

## 5. Progress

✅ Set up virtual environment  
✅ Created basic project structure  
✅ Implemented homepage using Streamlit with:
- Hero section (intro and call to action)
- Featured product cards with pricing
- Feature summary cards (Ingredients, Health, Budget)  
✅ Integrated basic styling with custom CSS  
✅ Placeholder data generated using PIL (image mock)  
🟡 Next: Add user input (health profile, dislikes)  
🟡 Next: Implement backend recommendation logic  
🟡 Next: Integrate ingredient database and real products  
🟡 Next: Connect community features (matching, trading)

---

## 6. How to Run Locally

```bash
# 1. Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install streamlit pillow numpy

# 3. Run the app
streamlit run app.py
