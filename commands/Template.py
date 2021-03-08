
class Template:

    def __init__(self, indecies):
        self.indecies = indecies

    def __repr__(self, name):
        append_string = ''
        for item in self.indecies:
            append_string += ' ' + str(item)
        return str(name + append_string)

    def execute(self, cpu, ram):
        pass
        