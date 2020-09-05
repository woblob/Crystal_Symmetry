# def powerset(iterable, maxnr):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(maxnr))



def usunkoor_mod_3(koorZEW):#, Matrixes):
    mat = MM.generateSymetryBaseQUAD() #przesia symetrie dla idealnej siecie krysstalicznej
    allsyms = MM.makelist(mat)
    hhhdict = MM.hashingPoints(koorZEW)
    for p in koorZEW:
        if MM.searchforpoint(hhhdict, *p):
            for os0, os1 in allsyms:
                for x, y, z in MM.listadous(mat[os0][os1], p):
                    hhhdict[x][y][z] = False
    return hhhdict

def usunkoor_mod_3(koorZEW):#, Matrixes):
  mat = MM.generateSymetryBaseQUAD() #przesia symetrie dla idealnej siecie krysstalicznej
  allsyms = MM.makelist(mat)
  hhhdict = MM.hashingPoints(koorZEW)
  for p in koorZEW:
    if MM.searchforpoint(hhhdict, *p):
      for os0, os1 in allsyms:
        for x, y, z in MM.listadous(mat[os0][os1], p):
          hhhdict[x][y][z] = False
  return hhhdict

%timeit -r 10 -n 100 d3 = usunkoor_mod_3(SUPERCELL2)


def usunkoor_mod_2(koorZEW):#, Matrixes):
  mat = MM.generateSymetryBaseQUAD() #przesia symetrie dla idealnej siecie krysstalicznej
  allsyms = MM.makelist(mat)
  hhhdict = MM.hashingPoints(koorZEW)
  for p in koorZEW:
    if MM.searchforpoint(hhhdict, *p):
      for os0, os1 in allsyms:
        for x, y, z in MM.listadous(mat[os0][os1], p):                
          hhhdict[x][y][z] = False
  return hhhdict

%time d2 = usunkoor_mod_2(SUPERCELL2)