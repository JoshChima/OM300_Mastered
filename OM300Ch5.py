import scipy as sy
import sympy as sym
from scipy.optimize import fsolve
import numpy as np
class Total_Life_Cycle_Cost:
    
    def __init__(self, VPCost, VOcost, ULoV, MpY, MpG, AveFPpG):
        self.VPCost = VPCost
        self.VOcost = VOcost
        self.ULoV = ULoV
        self.MpY = MpY
        self.MpG = MpG
        self.AveFPpG = AveFPpG

    def LCCoF(self):
        Ms = float(self.MpY) / float(self.MpG)
        return Ms * float(self.AveFPpG) * float(self.ULoV)
    def LCOC(self):
        return float(self.MpY) * float(self.VOcost) * float(self.ULoV)
    def TLCC(self):
        return float(self.VPCost) + float(self.LCCoF()) + float(self.LCOC())

V1 = Total_Life_Cycle_Cost(18000, 0.15, 16, 15500, 31, 3.66)
#print(V1.TLCC())

V2 = Total_Life_Cycle_Cost(18000, 0.14, 15, 15500, 33, 3.77)
V3 = Total_Life_Cycle_Cost(19500, 0.08, 15, 15500, 35, 3.77)

M = np.array(range(0, 300))
#VV2 = V2.VPCost + ((V2.AveFPpG/V2.MpG) + V2.VOcost) * M
#VV3 = V3.VPCost + ((V3.AveFPpG/V3.MpG) + V3.VOcost) * M
difl = []
for m in range(len(M)):
    x = M[m]
    VV2 = (V2.AveFPpG/V2.MpG) + V2.VOcost
    VV3 = (V3.AveFPpG/V3.MpG) + V3.VOcost
    func1 = V2.VPCost + (float(x) * VV2)
    func2 = V3.VPCost + (float(x) * VV3)
    dif = abs(func1 - func2)
    difl.append(dif)
    if func1 == func2:
        print(x)
    #elif difl[m] == min(difl):
        #print(difl[m])
        #print(x)
    else:
        continue
print(difl)
print(min(difl))
#VV23A = sym.geometry.in

#print(VV23A)