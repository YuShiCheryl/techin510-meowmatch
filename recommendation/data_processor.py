import pandas as pd
import numpy as np
from pathlib import Path

class DataProcessor:
    def __init__(self, data_dir="data/processed"):
        """初始化数据处理器"""
        self.data_dir = Path(data_dir)
        self.images_dir = Path("data/images/products")
    
    def load_data(self):
        """加载数据文件"""
        try:
            # 加载数据
            df = pd.read_csv(self.data_dir / "Cleaned Data 3.csv")
            
            # 添加图片路径 - 直接使用name列作为图片文件名
            df['image_path'] = df['name'].apply(lambda x: str(self.images_dir / f"{x}.jpg"))
            
            # 保存更新后的数据
            df.to_csv(self.data_dir / "Cleaned Data 3.csv", index=False)
            print("Data saved with image paths")
            
            # 处理价格（转换为每公斤价格）
            if 'price_per_oz' in df.columns:
                # 确保价格是数值类型
                df['price_per_oz'] = pd.to_numeric(df['price_per_oz'].str.replace('$', ''), errors='coerce')
                df['price_per_kg'] = df['price_per_oz'] * 35.274  # 1 kg = 35.274 oz
            
            # 处理卡路里（转换为每100克的卡路里）
            if 'kcalories_per_oz' in df.columns:
                # 确保卡路里是数值类型
                df['kcalories_per_oz'] = pd.to_numeric(df['kcalories_per_oz'], errors='coerce')
                df['calories_per_100g'] = df['kcalories_per_oz'] * 3.5274  # 1 oz = 28.35g, 所以 100g = 3.5274 oz
            
            # 确保 food_type 列没有空值
            df['food_type'] = df['food_type'].fillna('unknown')
            
            # 处理特殊特征
            df['special_features'] = df['special_features'].fillna('none')
            
            return df
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    def preprocess_data(self, df):
        """预处理数据"""
        if df is None:
            return None
            
        # 处理缺失值
        numeric_columns = ['protein_content', 'fat_content', 'carb_content', 
                         'fiber_content', 'moisture_content', 'price_per_oz', 
                         'kcalories_per_oz']
        
        for col in numeric_columns:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].mean())
        
        return df
    
    def extract_features(self, df):
        """提取特征"""
        if df is None:
            return None
            
        # 使用数据中实际的所有列，包括新添加的图片路径
        features = ['food_type', 'name', 'protein_sources', 'texture', 'ingredients',
                   'oz', 'price', 'price_per_oz', 'kcalories_per_oz', 'protein_content',
                   'fat_content', 'carb_content', 'fiber_content', 'moisture_content',
                   'special_features', 'image_path']
        
        # 确保所有需要的列都存在
        for feature in features:
            if feature not in df.columns:
                print(f"Warning: {feature} not found in data")
                return None
        
        return df[features]