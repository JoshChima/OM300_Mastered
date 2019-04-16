import numpy as np
import math
#df = np.array([1.1,.85,.8,.75],[0.5,0.7,0.6,1.5],[0.4,0.8,0.3,1.9],[0.6,0.7,0.8,2.0],[0.4,0.6,0.5,1.7],[0.4,0.8,0.6,1.5])
#Average_T = np.average(times)
P_rating = 1.1
Normal_T = lambda A_T,P_r: A_T*P_r
Standard_T = lambda N_T,A_f: N_T/(1-A_f)
Requires_Sample_Size = lambda z,s,x_bar,h: ((z*s)/(h*x_bar))**2
def S(xlst):
    sm = []
    x_bar = np.average(xlst)
    for x in xlst:
        sm.append((x-x_bar)**2)
    return x_bar,sum(sm)
Bob = lambda Obs,TObs: (Obs/TObs)*100
Ss = lambda z,p,h: ((z**2)*p*(1-p))/(h**2)
#print(Average_T)
#print(Normal_T(Average_T,P_rating))
#print(Normal_T(12,1.1))
#print(Standard_T(Normal_T(12,1.1),0.18))
P_r_df = [1.25,1.15,0.95,0.90]
df = [[34,41,34,43,40],[13,11,15,13],[3,3,4,6,3],[16,17,22,16]]
df_whl = df[1]+df[2]+df[0]+df[3]
allowance = 0.18
#print(dft[0][2:])
average_df = [round(np.average(x), ndigits=2) for x in df]
normal_df = [round(Normal_T(average_df[x],P_r_df[x]),ndigits=2) for x in range(0,len(P_r_df))]
s,x_b = S(df_whl)
print(average_df)
print(normal_df)
print(Standard_T(sum(normal_df),.18))
print(df_whl)
print(Requires_Sample_Size(1.96,x_b,18.56,.05))
