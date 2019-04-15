import numpy as np

#df = np.array([1.1,.85,.8,.75],[0.5,0.7,0.6,1.5],[0.4,0.8,0.3,1.9],[0.6,0.7,0.8,2.0],[0.4,0.6,0.5,1.7],[0.4,0.8,0.6,1.5])
#Average_T = np.average(times)
P_rating = 1.1
Normal_T = lambda A_T,P_r: A_T*P_r
Standard_T = lambda N_T,A_f: N_T/(1-A_f)
#print(Average_T)
#print(Normal_T(Average_T,P_rating))
#print(Normal_T(12,1.1))
#print(Standard_T(Normal_T(12,1.1),0.18))

df = np.array([[1,2,3,4],[1.15,0.85,0.9,0.75],[0.6,0.6,0.5,1.5],[0.3,0.8,0.3,1.9],[0.7,0.7,0.7,2.0],[0.4,0.7,0.6,1.6],[0.5,0.8,0.5,1.5]], dtype=np.float)
dft = df.transpose()
allowance = sum([0.07,0.08,0.03])
print(dft)
#print(dft[0][2:])
average_df = [np.average(dft[x][2:]) for x in range(len(dft))]
normal_df = [Normal_T(average_df[x],dft[x][1]) for x in range(len(dft))]
print(average_df)
print(normal_df)
print(sum(normal_df))
print(allowance)
print(Standard_T(sum(normal_df), allowance))

