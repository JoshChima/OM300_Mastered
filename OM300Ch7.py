import numpy as np
import pandas as pd

BEP = lambda fcX, fcY, vcX, vcY: (fcY - fcX)/(vcY-vcX)
TotCost = lambda fc,vc,nu: fc+(vc*nu)
Profit = lambda fc,vc,nu,ppu: ppu*nu-TotCost(fc,vc,nu)
GPEbe = BEP(150000,200000,18,14)
FMSbe = BEP(200000,480000,14,13)
DMbe = BEP(480000, 200000, 13, 14)
Miy = BEP(65000,26000,12.5,18.5)


print(GPEbe)
print(FMSbe)
print(DMbe)
print(Miy)
print(Profit(83000,1.15,110000,2.3))
print(Profit(41000,1.5,110000,2.3))
print(TotCost(26000,18,365*50))
