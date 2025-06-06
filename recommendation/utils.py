import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class CatFoodRecommender:
    def __init__(self):
        self.model = None
        self.food_data = None
        self.similarity_matrix = None
        
    def fit(self, food_data):
        """训练推荐模型"""
        self.food_data = food_data
        self.similarity_matrix = cosine_similarity(food_data)
        
    def recommend(self, food_id, n_recommendations=5):
        """基于特定食品推荐相似食品"""
        if self.food_data is None:
            return None
            
        food_idx = self.food_data.index.get_loc(food_id)
        similarity_scores = self.similarity_matrix[food_idx]
        similar_indices = similarity_scores.argsort()[::-1][1:n_recommendations+1]
        
        return self.food_data.iloc[similar_indices]
    
    def recommend_by_preferences(self, preferences, n_recommendations=5):
        """基于用户偏好推荐"""
        if self.food_data is None:
            return None
            
        match_scores = []
        for idx, food in self.food_data.iterrows():
            score = 0
            for feature, preference in preferences.items():
                if feature in food:
                    score += food[feature] * preference
            match_scores.append(score)
        
        top_indices = np.argsort(match_scores)[::-1][:n_recommendations]
        return self.food_data.iloc[top_indices]

def format_recommendations(recommendations):
    """格式化推荐结果"""
    formatted = []
    for rec in recommendations:
        formatted.append({
            'name': rec['name'],
            'protein': rec['protein'],
            'fat': rec['fat'],
            'fiber': rec['fiber'],
            'moisture': rec['moisture'],
            'similarity_score': rec['similarity_score']
        })
    return formatted

def calculate_nutrition_score(food):
    """计算营养评分"""
    # 基础分数
    score = 0
    
    # 蛋白质评分 (理想范围: 30-40%)
    protein = food.get('protein', 0)
    if 30 <= protein <= 40:
        score += 3
    elif 25 <= protein < 30 or 40 < protein <= 45:
        score += 2
    elif 20 <= protein < 25 or 45 < protein <= 50:
        score += 1
        
    # 脂肪评分 (理想范围: 15-20%)
    fat = food.get('fat', 0)
    if 15 <= fat <= 20:
        score += 3
    elif 12 <= fat < 15 or 20 < fat <= 25:
        score += 2
    elif 10 <= fat < 12 or 25 < fat <= 30:
        score += 1
        
    # 纤维评分 (理想范围: 2-4%)
    fiber = food.get('fiber', 0)
    if 2 <= fiber <= 4:
        score += 3
    elif 1 <= fiber < 2 or 4 < fiber <= 6:
        score += 2
    elif 0.5 <= fiber < 1 or 6 < fiber <= 8:
        score += 1
        
    # 水分评分 (湿粮理想范围: 75-85%)
    moisture = food.get('moisture', 0)
    if 75 <= moisture <= 85:
        score += 3
    elif 70 <= moisture < 75 or 85 < moisture <= 90:
        score += 2
    elif 65 <= moisture < 70 or 90 < moisture <= 95:
        score += 1
        
    return score

def get_nutrition_grade(score):
    """根据营养评分返回等级"""
    if score >= 10:
        return "A"
    elif score >= 8:
        return "B"
    elif score >= 6:
        return "C"
    elif score >= 4:
        return "D"
    else:
        return "F"