import scipy as sy
import sympy as sym
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
print(V1.TLCC())

