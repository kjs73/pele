import numpy as np

import fortran.ljcut as _ljcut
from pele.potentials.potential import BasePotentialAtomistic

__all__ = ["LJCut"]

class LJCut(BasePotentialAtomistic):
    """
    lennard jones potential with a cutoff that is continuous and smooth
    """
    def __init__(self, eps=1.0, sig=1.0, rcut = 2.5, boxl=None):
        self.sig = sig
        self.eps = eps
        self.rcut = rcut
        self.boxl = boxl
        if self.boxl is None:
            self.periodic = False
            self.boxl = 100000.
        else:
            self.periodic = True
        
        if False:
            print "using Lennard-Jones potential", self.sig, self.eps, 
            print "with cutoff", self.rcut,
            if self.periodic: 
                print "periodic with boxl ", self.boxl
            else:
                print ""
        
    def getEnergy(self, coords):
        E = _ljcut.ljenergy(
                coords, self.eps, self.sig, self.periodic, self.boxl,
                self.rcut)
        return E

    def getEnergyGradient(self, coords):
        E, grad = _ljcut.ljenergy_gradient(
                coords, self.eps, self.sig, self.periodic, self.boxl,
                self.rcut)
        return E, grad 
    
    def getEnergyList(self, coords, ilist):
        #ilist = ilist_i.getNPilist()
        #ilist += 1 #fortran indexing
        E = _ljcut.energy_ilist(
                coords, self.eps, self.sig, ilist.reshape(-1), self.periodic, 
                self.boxl, self.rcut)
        #ilist -= 1
        return E
    
    def getEnergyGradientList(self, coords, ilist):
        #ilist = ilist_i.getNPilist()
        #ilist += 1 #fortran indexing
        E, grad = _ljcut.energy_gradient_ilist(
                coords, self.eps, self.sig, ilist.reshape(-1), self.periodic, 
                self.boxl, self.rcut)
        #ilist -= 1
        return E, grad 

#
# only testing stuff below here
#


def test():
    natoms = 10
    coords = np.random.uniform(-1,1.,3*natoms) * natoms**(-1./3)
    pot = LJCut()
    E = pot.getEnergy(coords)
    Egrad, grad = pot.getEnergyGradient(coords)
    print E, Egrad
    print grad


if __name__ == "__main__":
    test()
