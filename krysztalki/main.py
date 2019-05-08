from SYMfunc import *
from cifParsing import *

# filename = '1100043.cif'
# FUNC = Crystal.from_cif
filename = 1100043
FUNC = Crystal.from_cod

SUPERCELL = getSCell(FUNC, filename, size = 2)
Options = abcde(SUPERCELL,sumVac = 2) 

saveOutput(Options)