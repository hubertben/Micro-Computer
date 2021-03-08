from commands.add import Add
from commands.store import Store
from commands.load import Load
from commands.jump import Jump
from commands.compare import Compare

class Command:

    def END(index):
        return 'END'

    def add(index):
        return Add(index)
    
    def jump(index):
        return Jump(index)
        
    def store(index):
        return Store(index)

    def load(index):
        return Load(index)

    def compare(index):
        return Compare(index)

        