import os
from save_python2file.save_strategy import SaveStrategy

class SaveContext:
    """上下文类，用于根据不同策略保存数据"""
    
    def __init__(self, strategy: SaveStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SaveStrategy):
        self._strategy = strategy
    
    def save(self, data, filename, filepath):
        os.makedirs(filepath, exist_ok=True)  # 确保目录存在
        full_path = os.path.join(filepath, filename)
        self._strategy.save(data, full_path)