# test_recommender.py
from data_processor import DataProcessor
from recommender import CatFoodRecommender
from utils import format_recommendations

def test_recommendation_system():
    print("Testing recommendation system...")
    
    # 初始化处理器和推荐器
    processor = DataProcessor()
    recommender = CatFoodRecommender()
    
    # 加载数据
    print("Loading data...")
    wet_food, dry_food, nutrition_research = processor.load_data()
    
    if wet_food is None:
        print("Error: Could not load data files")
        return
    
    print(f"Successfully loaded data:")
    print(f"Wet food samples: {len(wet_food)}")
    print(f"Dry food samples: {len(dry_food)}")
    
    # 预处理数据
    print("\nPreprocessing data...")
    wet_food_processed = processor.preprocess_data(wet_food)
    wet_food_features = processor.extract_features(wet_food_processed)
    
    # 训练推荐模型
    print("\nTraining recommendation model...")
    recommender.fit(wet_food_features)
    
    # 测试基于偏好的推荐
    print("\nTesting preference-based recommendations...")
    test_preferences = {
        'protein_content': 0.8,
        'fat_content': 0.6,
        'fiber_content': 0.4,
        'moisture_content': 0.9
    }
    
    recommendations = recommender.recommend_by_preferences(test_preferences)
    formatted_recommendations = format_recommendations(recommendations)
    
    print("\nTop 5 recommendations based on preferences:")
    for i, rec in enumerate(formatted_recommendations, 1):
        print(f"\n{i}. {rec['name']}")
        print(f"   Protein: {rec['protein']:.1f}%")
        print(f"   Fat: {rec['fat']:.1f}%")
        print(f"   Fiber: {rec['fiber']:.1f}%")
        print(f"   Moisture: {rec['moisture']:.1f}%")

if __name__ == "__main__":
    test_recommendation_system()