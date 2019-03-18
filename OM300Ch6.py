import numpy as np
import pandas as pd

STDoSD = lambda std, n: std/(n**(1/2))
#print(STDoSD(0.09,64))

UCL_nsig = lambda x, nsig, std, n: x + nsig*(STDoSD(std,n))
LCL_nsig = lambda x, nsig, std, n: x - nsig*(STDoSD(std,n))
#print(UCL_nsig(14, 3, 0.20, 35))
#print(LCL_nsig(14, 3, 0.20, 64))


UCL_x = lambda MoSM, MF, ARoS: MoSM + (MF*ARoS)
UCL_R = lambda aR, ARoS: aR*ARoS
LCL_x = lambda MoSM, MF, ARoS: MoSM - (MF*ARoS)
LCL_xMax = lambda MoSM, MF, ARoS: max([0,LCL_x(MoSM, MF, ARoS)])
LCL_R = lambda aR, ARoS: max([0, UCL_R(aR,ARoS)])
MoSM = 725
MF = 0.308
ARoS = 6
UR = 1.777
LR = 0.223
print(UCL_x(MoSM,MF,ARoS))
print(UCL_R(UR, ARoS))
print(LCL_xMax(MoSM,MF,ARoS))
print(LCL_R(LR, ARoS))