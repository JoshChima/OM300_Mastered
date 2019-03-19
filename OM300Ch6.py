import numpy as np
import pandas as pd

STDoSD = lambda std, n: std/(n**(1/2))
#print(STDoSD(1.36,50))

UCL_nsig = lambda x, nsig, std, n: x + nsig*(STDoSD(std,n))
LCL_nsig = lambda x, nsig, std, n: x - nsig*(STDoSD(std,n))
#print(UCL_nsig(420, 3, 30, 25))
#print(LCL_nsig(420, 3, 30, 25))


UCL_x = lambda MoSM, MF, ARoS: MoSM + (MF*ARoS)
UCL_R = lambda aR, ARoS: aR*ARoS
LCL_x = lambda MoSM, MF, ARoS: MoSM - (MF*ARoS)
LCL_xMax = lambda MoSM, MF, ARoS: max([0,LCL_x(MoSM, MF, ARoS)])
LCL_R = lambda aR, ARoS: max([0, UCL_R(aR,ARoS)])
MoSM = 4
MF = 0.1
ARoS = 3
UR = 4.1
LR = 3.9
#print(MoSM)
#print(MoSM+3*(MoSM**0.5))
#print(MoSM-3*(MoSM**0.5))
#print(UCL_x(MoSM,MF,ARoS))
#print(LCL_x(MoSM,MF,ARoS))
#print(UCL_R(UR,ARoS))
#print(LCL_R(LR,ARoS))


#print(ARoS)
#print(UCL_x(MoSM,MF,ARoS))
#print(UCL_R(UR, ARoS))
#print(LCL_xMax(MoSM,MF,ARoS))
#print(LCL_R(LR, ARoS))


MFdefp = lambda Dlst, Ssz, n:(sum(Dlst)/(Ssz*n))
STDoSDp = lambda p, n: (p*(1-p)/n)**0.5
pm = MFdefp([6,5,6,4,3,4,5,3,6,3,7,5,4,3,4,5,6,5,4,3,7],100,21)
z = 3
Op = STDoSDp(pm,100)
print(pm)
print(Op)
print(pm+(z*Op))
print(pm-(z*Op))