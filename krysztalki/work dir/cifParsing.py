from crystals import Crystal
import numpy as np

class FROM():
  CIF = Crystal.from_cif
  COD = Crystal.from_cod
#   ASE = Crystal.from_ase
#   PWSCF = Crystal.from_pwscf

def millerORweber(ITN):
    """
    Determine which coordinates to choose.
    All numbers between [143-194] are for hexagonal groups.
    """
    if ITN > 194 or ITN < 143:
        return "m" #"rest"
    return "w"    #"hP, hR"

def allEqPoints(POINT,SIZE):
  mPOINT = POINT.copy()
  for i in range(mPOINT[0].size):
    zera = np.where(mPOINT[:,i] == 0)[0]
    mylist = []
    for nr in range(len(mPOINT[zera])):
      NP = mPOINT[zera][nr].copy()
      NP[i] += SIZE
      mylist.append(NP)
    mPOINT = np.append(mPOINT,np.array(mylist),axis=0)
  return np.unique(mPOINT,axis=0)

  
def getSCell(fromwhere, filename, size): 
    """
    Get cell from cod/cif/else. 
    Expand it to supercell size.
    Place points between -1 and less than 1
    Add missing walls of a cell.
    """
    file = fromwhere(filename)
    basetype = millerORweber(file.symmetry()['international_number'])
    points = file.supercell(size,size,size).itersorted() 
    mylist = np.array([point.coords_fractional for point in points])
    mylist = np.around(allEqPoints(mylist,size)/(size/2)-1,6)
    return np.unique(mylist,axis=0), basetype