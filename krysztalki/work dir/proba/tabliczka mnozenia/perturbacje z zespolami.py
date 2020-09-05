import pickle
import pathlib
from wyznaczanie_podrup_z_generatorow import Grupa

# with open("wyniki zespolow/zespol 2", "rb") as f:
#     data = pickle.load(f)

# l = []
# # el.konstruktory
#
# for el in data:
#     for u in el.all_syms:
#         if "t_" in u:
#             # break
#             pass
#     else:
#         if "ID_000"  in el.all_syms:
#             l.append(el)
#

# for el in l:
#     print(el)

# print(len(data))

p = pathlib.Path("./wyniki zespolow")

c = 0

d = dict()

for f in p.iterdir():
    if f.suffix != ".txt":
        with open(f'wyniki zespolow/{f.name}', "rb") as file:
            num = f.name.split()[1]
            data = pickle.load(file)
            d[num] = data


with open("./wyniki zespolow/zespoly_wszystkie.pickle", "wb") as f:
    pickle.dump(d, f)