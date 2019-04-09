import scipy as sy
import sympy as sym
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

#LCpU = Labor Cost per Unit

LCpU = lambda LC,L,PUpD: (LC*L)/PUpD
BEP = lambda fcA, fcB, vcA, vcB: (fcA - fcB)/(vcB-vcA)

#print(LCpU(3,6,42))
#print(LCpU(2.25,9,45))
#print(LCpU(57,3,105))

#print((2000/200)/8)
Weights = [.2,.25,.25,.15,.15]
Maitland = [65,45,50,55,75]
Baptist_C = [65,80,75,75,20]
Northside_M = [85,35,55,35,85]

def WAS(Loc,Weights):
    WSL = []
    SoW = sum(Weights)
    for x in range(len(Loc)):
        WS = Loc[x] * Weights[x]
        WSL.append(WS)
    return sum(WSL)/SoW

#print(WAS(Maitland,Weights))
#print(WAS(Baptist_C,Weights))
#print(WAS(Northside_M,Weights))

print(BEP(960000,800000,13800,28000))
print(BEP(960000,0,13800,-28000))

X = [10,3,4,15,13,1,5]
Y = [5,8,7,10,3,12,5]
Popu = [3,3,2,6,5,3,10]

def X_Cord(P,X):
    WXL = []
    for r in range(len(X)):
        WX = X[r]*Popu[r]
        WXL.append(WX)
    return sum(WXL)

#print((sum(X)*X_Cord(Popu,X))/sum(Popu))
#print((sum(Y)*X_Cord(Popu,Y))/sum(Popu))


print(sum(Popu))
print(X_Cord(Popu,X)/sum(Popu))
print(X_Cord(Popu,Y)/sum(Popu))
#print(BEP(820000,960000,15000,14000))

#print(960000/(29000-14000))     
