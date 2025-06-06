import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Optional

class CatFoodRecommender:
    def __init__(self, data_dir="../data/processed"):
        """初始化推荐器"""
        self.data_dir = Path(data_dir)
        self.data = None
        self.scaler = MinMaxScaler()
        self.original_data = None  # 保存原始数据
        
    def load_data(self):
        """加载数据"""
        try:
            self.data = pd.read_csv(self.data_dir / "Cleaned Data 3.csv")
            self.original_data = self.data.copy()  # 保存原始数据
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
            
    def preprocess_data(self):
        """预处理数据"""
        if self.data is None:
            return False
            
        # 处理价格数据 - 移除 '$' 符号并转换为浮点数
        if 'price_per_oz' in self.data.columns:
            self.data['price_per_oz'] = self.data['price_per_oz'].str.replace('$', '').astype(float)
            
        # 处理数值型特征
        numeric_features = ['protein_content', 'fat_content', 'carb_content', 
                          'fiber_content', 'moisture_content', 'price_per_oz']
        
        # 标准化数值特征
        self.data[numeric_features] = self.scaler.fit_transform(self.data[numeric_features])
        
        return True
        
    def get_recommendations(self, preferences: Dict, top_n: int = 5) -> List[Dict]:
        """
        基于用户偏好推荐猫粮
        
        参数:
        preferences: 字典，包含用户偏好
            {
                'food_type': 'wet' 或 'dry',
                'protein_content': 0.4,  # 期望的蛋白质含量
                'fat_content': 0.2,     # 期望的脂肪含量
                'carb_content': 0.1,    # 期望的碳水化合物含量
                'fiber_content': 0.05,  # 期望的纤维含量
                'moisture_content': 0.8, # 期望的水分含量
                'price_per_oz': 0.5,    # 期望的价格（每盎司）
                'special_features': ['Grain-Free']  # 特殊需求
            }
        top_n: 返回的推荐数量
        """
        if self.data is None:
            return None
            
        # 设置用户偏好
        numeric_features = ['protein_content', 'fat_content', 'carb_content', 
                          'fiber_content', 'moisture_content', 'price_per_oz']
        
        # 创建用户偏好向量
        user_preferences = np.zeros((1, len(numeric_features)))
        for i, feature in enumerate(numeric_features):
            if feature in preferences:
                user_preferences[0, i] = preferences[feature]
        
        # 标准化用户偏好
        user_preferences = self.scaler.transform(user_preferences)
        
        # 计算相似度
        similarities = []
        for idx, row in self.data.iterrows():
            # 检查食物类型匹配
            if preferences.get('food_type') and row['food_type'] != preferences['food_type']:
                continue
                
            # 检查特殊特征匹配
            if preferences.get('special_features'):
                if not any(feature in str(row['special_features']) for feature in preferences['special_features']):
                    continue
            
            # 计算余弦相似度
            product_vector = row[numeric_features].values.reshape(1, -1)
            similarity = cosine_similarity(user_preferences, product_vector)[0][0]
            similarities.append((idx, similarity))
        
        # 排序并返回top_n推荐
        similarities.sort(key=lambda x: x[1], reverse=True)
        recommendations = []
        
        for idx, similarity in similarities[:top_n]:
            product = self.data.iloc[idx]
            original_product = self.original_data.iloc[idx]  # 使用原始数据
            recommendations.append({
                'name': original_product['name'],
                'food_type': original_product['food_type'],
                'protein_content': original_product['protein_content'],
                'fat_content': original_product['fat_content'],
                'carb_content': original_product['carb_content'],
                'fiber_content': original_product['fiber_content'],
                'moisture_content': original_product['moisture_content'],
                'price_per_oz': original_product['price_per_oz'],
                'special_features': original_product['special_features'],
                'image_path': original_product['image_path'],
                'similarity_score': similarity
            })
        
        return recommendations

# 测试代码
if __name__ == "__main__":
    # 初始化推荐器
    recommender = CatFoodRecommender()
    
    # 加载数据
    if not recommender.load_data():
        print("Failed to load data")
        exit()
    
    # 预处理数据
    if not recommender.preprocess_data():
        print("Failed to preprocess data")
        exit()
    
    # 测试推荐
    preferences = {
        'food_type': 'wet',
        'protein_content': 0.4,
        'fat_content': 0.2,
        'carb_content': 0.1,
        'fiber_content': 0.05,
        'moisture_content': 0.8,
        'price_per_oz': 0.5,
        'special_features': ['Grain-Free']
    }
    
    recommendations = recommender.get_recommendations(preferences, top_n=5)
    
    print("\nTop 5 Recommendations:")
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec['name']}")
        print(f"   Food Type: {rec['food_type']}")
        print(f"   Protein: {rec['protein_content']:.2%}")
        print(f"   Fat: {rec['fat_content']:.2%}")
        print(f"   Carbs: {rec['carb_content']:.2%}")
        print(f"   Fiber: {rec['fiber_content']:.2%}")
        print(f"   Moisture: {rec['moisture_content']:.2%}")
        # 处理价格显示
        try:
            price = float(rec['price_per_oz'].replace('$', ''))
            print(f"   Price per oz: ${price:.2f}")
        except (ValueError, AttributeError):
            print(f"   Price per oz: {rec['price_per_oz']}")
        print(f"   Special Features: {rec['special_features']}")
        print(f"   Similarity Score: {rec['similarity_score']:.2f}")