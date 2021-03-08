from file_reader import FileReader as fr
from CPU import CPU
from RAM import RAM

r = RAM(0)
r.load_memory(fr.read_commands())
r.display_registers()

c = CPU()
c.load_ram(r)

c.loop(100)
