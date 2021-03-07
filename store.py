

class Store():

    def __init__(self, index):
        self.index = index

    def execute(self):
        return 'STORE', str(self.index)