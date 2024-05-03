# syms =['["2_x00"]', '["2_0y0"]', '["2_00z"]',
# '["2_xx0"]', '["2_x0x"]', '["2_0yy"]',
# '["2_xmx0"]', '["2_mx0x"]', '["2_0myy"]',
#
# '["3_xxx"]', '["3_xmxmx"]',
# '["3_mxxmx"]', '["3_mxmxx"]',
#
# '["m3_xxx"]', '["m3_xmxmx"]',
# '["m3_mxxmx"]', '["m3_mxmxx"]',
#
# '["4_x00"]', '["4_0y0"]', '["4_00z"]',
#
# '["-4_x00"]', '["-4_0y0"]', '["-4_00z"]']

syms_hex = [
    '["i_000"]',
    '["hex_m_x2xz"]',
    '["hex_m_2xxz"]',
    '["hex_m_x0z"]',
    '["hex_m_0yz"]',
    '["hex_2_x00"]',
    '["hex_2_0y0"]',
    '["hex_2_x2x0"]',
    '["hex_2_2xx0"]',
    '["3_00z"]',
    '["m3_00z"]',
    '["6_00z"]',
    '["m6_00z"]',
]


text = """import matrices_new_extended as mne
import numpy as np
import sympy as sp
from equality_check import Point

x, y, z = sp.symbols("x y z")
Point.unchanged = np.array([ x, y, z, 1])


class Test_Axis_"""

inner = """
    def test_matrix_{0}(self):
        assert Point([ x, y, z, 1]).is_got_by(mne._matrix_{0})
"""


inner_test = """
    def test{0}(self):
        assert Point([ x, y, z, 1]).is_got_by(mne.{0})
        #{1}"""


for sym in syms_hex:
    name = sym.strip('["]')
    new_file = f"test_matrices_like_{name}.py"
    # proba = f"test.py"
    with open(new_file, "w") as write_file:
        write_file.write(text + name + ":\n")
        write_file.write(inner.format(name))
        with open("../matrices_new_extended_hexx.py") as read_file:
            for line in read_file:
                if sym in line:
                    separator = f" = matrices_dict_hex{sym}"
                    matrix, slide = line.split(separator)
                    write_file.write(inner_test.format(matrix, slide.replace("+", "")))
