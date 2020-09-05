"""

"""

from SYMfunc import *
from cif_parsing import *

# filename = '1100043.cif'
# FUNC = Crystal.from_cif
filename = 1100043
SIZE = 2
SUMOFVACANCIES = 2
FUNC = Crystal.from_cod

# Size = 2, Vacancies = 2, atoms in unitcell = 18 --> time ~ 10[s]

SUPERCELL, BASE = getSCell(FUNC, filename, size = SIZE)
Options = checkAllCells(SUPERCELL,BASE,sumVac = SUMOFVACANCIES) 

saveOutput(Options, filename = "OUTPUT.txt")