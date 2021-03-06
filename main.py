from file_reader import FileReader as fr
from CPU import CPU
from RAM import RAM

r = RAM(0)
r.load_memory(fr.read_commands())

c = CPU()
c.load_ram(r)

c.run()
