import scipy as sy
import sympy as sym
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
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
V2 = Total_Life_Cycle_Cost(21000, 0.09, 11, 30000, 30, 2.28)
V3 = Total_Life_Cycle_Cost(25000, 0.06, 11, 30000, 43, 2.28)

VV2 = (V2.AveFPpG / V2.MpG) + V2.VOcost
VV3 = (V3.AveFPpG / V3.MpG) + V3.VOcost
Crossover_point_M = (V3.VPCost - V2.VPCost) / (VV2 - VV3)
Crossover_point_Y = Crossover_point_M / V2.MpY
print(Crossover_point_M)
print(V2.TLCC())
print(V3.TLCC())
#def Tcost(Price, DpY, NoY, OCpM, mileage, CpG):
    #Total_Ocost = DpY * NoY * OCpM
    #Total_Fcost = ((DpY * NoY) / mileage) * CpG
    #Totalcost = Price + Total_Ocost + Total_Fcost
    #print(Totalcost)

Totalcost = 94000 + 0.47 * 11 * 32000 + ((32000 * 11) / 12) * 3
#print(Totalcost)

def New_Crpoint(CrPM, MpY):
    print(CrPM / MpY)

New_Crpoint(68548, 24000)