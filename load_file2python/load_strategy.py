import json
import pickle
from abc import ABC, abstractmethod

class LoadStrategy(ABC):
    """加载策略的抽象基类"""
    
    @abstractmethod
    def load(self, filepath):
        pass

class LoadJsonStrategy(LoadStrategy):
    """加载JSON格式的策略"""
    
    def load(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

class LoadJsonlStrategy(LoadStrategy):
    """加载JSON Lines格式的策略"""
    
    def load(self, filepath):
        data = []
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                data.append(json.loads(line))
        return data

class LoadTxtStrategy(LoadStrategy):
    """加载文本格式的策略"""
    
    def load(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            return content

class LoadPickleStrategy(LoadStrategy):
    """加载Pickle格式的策略"""
    
    def load(self, filepath):
        with open(filepath, 'rb') as file:
            return pickle.load(file)