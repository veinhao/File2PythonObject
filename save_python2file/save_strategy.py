from abc import ABC, abstractmethod
import json
import pickle

from regex import F

class SaveStrategy(ABC):
    """保存策略的抽象基类"""
    
    @abstractmethod
    def save(self, data, filepath, write_mode):
        pass

class SaveJsonStrategy(SaveStrategy):
    """保存为JSON格式的策略"""
    
    def save(self, data, filepath, write_mode='a'):
        make_sure_file_exists(filepath, write_mode)
        with open(filepath, write_mode, encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class SaveTxtStrategy(SaveStrategy):
    """保存为文本格式的策略"""
    
    def save(self, data, filepath, write_mode='a'):
        make_sure_file_exists(filepath, write_mode)
        with open(filepath, write_mode, encoding='utf-8') as file:
            file.write(str(data)+'\n')

class SavePickleStrategy(SaveStrategy):
    """保存为Pickle格式的策略"""
    
    def save(self, data, filepath, write_mode='ab'):
        make_sure_file_exists(filepath, write_mode)
        with open(filepath, write_mode) as file:
            pickle.dump(data, file)

def make_sure_file_exists(filepath, write_mode):
    import os
    if 'w' not in write_mode and not os.path.exists(filepath):
        open(filepath, "w").close()
        
