
class FileReader:

    def __init__(self):
        return

    def read_commands(path = 'commands/__commands.txt'):
        with open(path, "r") as txt_file:
            return txt_file.read().splitlines()
    
    
        

