from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class FoodType(Enum):
    WET = "wet"
    DRY = "dry"

class HealthCondition(Enum):
    NORMAL = "normal"
    OVERWEIGHT = "overweight"
    UNDERWEIGHT = "underweight"
    DIABETIC = "diabetic"
    KIDNEY_DISEASE = "kidney_disease"
    URINARY = "urinary"
    SENSITIVE_STOMACH = "sensitive_stomach"

class ActivityLevel(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"

@dataclass
class CatProfile:
    age: float  # 年龄（岁）
    weight: float  # 体重（kg）
    activity_level: ActivityLevel  # 活动水平
    health_condition: HealthCondition  # 健康状况
    food_preference: Optional[FoodType] = None  # 食物偏好（可选）
    special_needs: List[str] = None  # 特殊需求（可选）

@dataclass
class CatFood:
    name: str
    food_type: FoodType
    protein_content: float
    fat_content: float
    carb_content: float
    fiber_content: float
    moisture_content: float
    price_per_oz: float
    special_features: List[str]
    image_path: str

class CatFoodRecommender:
    def __init__(self):
        self.foods = []
    
    def calculate_daily_calories(self, cat_profile: CatProfile) -> float:
        """计算猫咪每日所需卡路里"""
        # 基础代谢率 (BMR) 计算
        if cat_profile.age < 1:  # 幼猫
            bmr = 100 * cat_profile.weight
        else:  # 成年猫
            bmr = 70 * (cat_profile.weight ** 0.75)
        
        # 根据活动水平调整
        activity_multiplier = {
            ActivityLevel.LOW: 1.2,
            ActivityLevel.MODERATE: 1.4,
            ActivityLevel.HIGH: 1.6
        }
        
        # 根据健康状况调整
        health_multiplier = {
            HealthCondition.NORMAL: 1.0,
            HealthCondition.OVERWEIGHT: 0.8,
            HealthCondition.UNDERWEIGHT: 1.2,
            HealthCondition.DIABETIC: 0.9,
            HealthCondition.KIDNEY_DISEASE: 0.8,
            HealthCondition.URINARY: 1.0,
            HealthCondition.SENSITIVE_STOMACH: 1.0
        }
        
        daily_calories = bmr * activity_multiplier[cat_profile.activity_level] * health_multiplier[cat_profile.health_condition]
        return daily_calories
    
    def load_foods(self, foods: List[CatFood]):
        """加载猫粮数据"""
        self.foods = foods
    
    def get_recommendations(self, cat_profile: CatProfile, top_n: int = 5) -> List[CatFood]:
        """获取推荐"""
        if not self.foods:
            return []
        
        # 计算每日所需卡路里
        daily_calories = self.calculate_daily_calories(cat_profile)
        
        # 计算每个食物的匹配分数
        scored_foods = []
        for food in self.foods:
            score = 0
            
            # 食物类型匹配
            if cat_profile.food_preference and food.food_type == cat_profile.food_preference:
                score += 2
            
            # 特殊需求匹配
            if cat_profile.special_needs:
                for need in cat_profile.special_needs:
                    if need in food.special_features:
                        score += 1
            
            # 营养成分匹配
            if cat_profile.health_condition == HealthCondition.OVERWEIGHT:
                if food.protein_content > 0.4 and food.fat_content < 0.2:
                    score += 2
            elif cat_profile.health_condition == HealthCondition.UNDERWEIGHT:
                if food.protein_content > 0.35 and food.fat_content > 0.2:
                    score += 2
            elif cat_profile.health_condition == HealthCondition.DIABETIC:
                if food.carb_content < 0.1:
                    score += 2
            elif cat_profile.health_condition == HealthCondition.KIDNEY_DISEASE:
                if food.protein_content < 0.3:
                    score += 2
            elif cat_profile.health_condition == HealthCondition.URINARY:
                if food.moisture_content > 0.75:
                    score += 2
            elif cat_profile.health_condition == HealthCondition.SENSITIVE_STOMACH:
                if "Grain-Free" in food.special_features:
                    score += 2
            
            scored_foods.append((food, score))
        
        # 按分数排序并返回前N个推荐
        scored_foods.sort(key=lambda x: x[1], reverse=True)
        return [food for food, _ in scored_foods[:top_n]]