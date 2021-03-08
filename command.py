from commands.add import Add
from commands.store import Store
from commands.load import Load
from commands.jump import Jump
from commands.compare import Compare
from commands.display import Display

class Command:

    def END(index = 0):
        return 'END'

    def add(indecies):
        return Add(indecies)
    
    def jump(indecies):
        return Jump(indecies)
        
    def store(indecies):
        return Store(indecies)

    def load(indecies):
        return Load(indecies)

    def compare(indecies):
        return Compare(indecies)

    def display(indecies):
        return Display(indecies)

        