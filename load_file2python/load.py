from load_file2python.load_strategy import LoadStrategy

class LoadContext:
    """上下文类，用于根据不同策略加载数据"""
    
    def __init__(self, strategy: LoadStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: LoadStrategy):
        self._strategy = strategy
    
    def load(self, filepath):
        return self._strategy.load(filepath)