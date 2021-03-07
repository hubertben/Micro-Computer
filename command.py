from add import Add
from store import Store
from load import Load
from jump import Jump

class Command:

    def add(index):
        return Add(index)
    
    def jump(index):
        return Jump(index)
        
    def store(index):
        return Store(index)

    def load(index):
        return Load(index)