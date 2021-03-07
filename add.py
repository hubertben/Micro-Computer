

class Add():

    def __init__(self, index):
        self.index = index

    def execute(self):
        return 'ADD', str(self.index)