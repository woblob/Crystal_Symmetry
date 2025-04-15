import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

l = []
with open("wyniki zespolow/czasy.txt", "r") as f:
    for line in f:
        rekord = list(map(float ,line.split()))
        rekord[0] = int(rekord[0])
        l.append(rekord)

rekordy = l[1:]
for r in rekordy:
    r.append(r[1]/r[0])

for r in rekordy:
    print(r)

# X = [el[0] for el in rekordy]
# y = [el[1] for el in rekordy]
#
# plt.plot(X, y)
# plt.xlabel("numer grupy[-]")
# plt.ylabel("czas kumulatywny [min]")
# filename = "czas kumulatywny.pdf"
# with PdfPages(filename) as pp:
#     plt.savefig(pp, format='pdf')

# X = [el[0] for el in rekordy]
# y = [el[2] for el in rekordy]
#
# plt.plot(X, y)
# plt.xlabel("numer grupy[-]")
# plt.ylabel("czas na grupe [s]")
# filename = "czas na grupe.pdf"
# with PdfPages(filename) as pp:
#     plt.savefig(pp, format='pdf')
#



# X = [el[0] for el in rekordy]
# y = [el[3] for el in rekordy]
#
# plt.plot(X, y)
# plt.xlabel("numer grupy")
# plt.ylabel("ile minut minelo srednio na grupe kumulatywnie")
# with PdfPages("tendencja czasowa.pdf") as pp:
#     plt.savefig(pp, format='pdf')