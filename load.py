

class Load():

    def __init__(self, index):
        self.index = index

    def execute(self):
        return 'LOAD', str(self.index)
        