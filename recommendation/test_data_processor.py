import pandas as pd
import numpy as np
from pathlib import Path
from data_processor import DataProcessor

def test_data_processor():
    print("Testing data processing...")
    
    # 获取当前文件所在目录的父目录（项目根目录）
    current_dir = Path(__file__).parent
    project_root = current_dir.parent
    
    # 初始化数据处理器，使用绝对路径
    processor = DataProcessor(data_dir=str(project_root / "data" / "processed"))
    
    print("\nLoading data...")
    df = processor.load_data()
    if df is None:
        print("Error: Could not load data")
        return
    
    print("\nPreprocessing data...")
    df = processor.preprocess_data(df)
    if df is None:
        print("Error: Could not preprocess data")
        return
    
    print("\nExtracting features...")
    features = processor.extract_features(df)
    if features is None:
        print("Error: Could not extract features")
        return
    
    print("\nData processing completed successfully!")
    print("\nSample of processed data:")
    print(features.head())
    print("\nData shape:", features.shape)

if __name__ == "__main__":
    test_data_processor()