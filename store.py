

class Store():

    def __init__(self, index):
        self.index = index

    def execute(self, cpu, ram):
        return 'STORE', str(self.index)