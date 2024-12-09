from load_file2python.load_strategy import LoadJsonlStrategy,LoadJsonStrategy,LoadTxtStrategy,LoadPickleStrategy
from load_file2python.load import LoadContext
import os

def load_data_from_file(directory, extension=None):
    """
        directory: eg. /root/autodl-tmp/wwh/vdd/a.txt

        you must add 'r' before the directory if your directory type is windows
        to make sure uniting the path correctly
    """
    if extension is None:
        extension = os.path.splitext(directory)[1]

    strategy_map = {
        '.json': LoadJsonStrategy(),
        '.txt': LoadTxtStrategy(),
        '.pkl': LoadPickleStrategy(),
        '.jsonl':LoadJsonlStrategy()
    }
    
    if extension not in strategy_map:
        raise ValueError(f"Unsupported file extension: {extension}")
    
    context = LoadContext(strategy_map[extension])
    data = context.load(directory)
    return data