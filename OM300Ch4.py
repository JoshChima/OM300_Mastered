import numpy as np

alst = np.array([460,495,516,566,580], dtype=float)
forlst = np.array([490.33,525.67,554], dtype=float)

alpha = 0.5
sectalst = alst[3:]
weights = np.array([.1,.1,.1,.2,.2,.3], dtype=float)
moving_ave = '\n{:0.2f}.\n'.format(np.average(sectalst))
def MAD(actualst, foreclst, n):
    l = len(actualst)
    print(n)
    aflst = []
    nelst = np.array(actualst[n:len(actualst)])
    print(nelst)
    for x in range(len(nelst)):
        AF = abs(nelst[x] - foreclst[x])
        aflst.append(AF)
    print(aflst)
    MADsol = (float(sum(aflst)))/l
    return MADsol
def exp_smooth(alpha, F_t1, A_t1):
    AF = A_t1 - F_t1
    F_t = (alpha * (AF)) + F_t1
    return F_t
def naive(lst):
    nlst = []
    for x in range(len(lst)):
        if x == 0:
            continue
        else:
            n = lst[x-1]
            nlst.append(n)
    return nlst
#fix Mexp so that it can place an f value in more than just the first spot.
def Mexp_smooth(f, fpoint):
    flst = np.zeros(len(alst))
    fflst = f
    for x in range(0, fpoint):
        continue
    for x in range(fpoint, len(alst)):
        if x == fpoint:
            F_t1 = fflst
            A_t1 = alst[x-1]
            F_t = exp_smooth(alpha, F_t1, A_t1)
            flst[x]=F_t
        else:
            F_t1 = flst[x-1]
            A_t1 = alst[x-1]
            F_t = exp_smooth(alpha, F_t1, A_t1)
            flst[x]=F_t
    return(flst[1:])
def Move_ave(lst, n, ytype):
    mlst = []
    for x in range(n-1, len(lst)+1):
        salst = lst[x-ytype:x]
        moving_ave = '{:0.2f}'.format(np.average(salst))
        mlst.append(moving_ave)
    return mlst
def Weight_ave(lst, weightlst, n, ytype):
    wlst = []
    for x in range(n-1, len(lst)+1):
        salst = lst[x-ytype:x]
        weighted_ave = '{:0.2f}'.format(np.average(salst, weights=weightlst))
        wlst.append(weighted_ave)
    return wlst
#weighted_ave = '\n{:0.2f}.\n'.format(np.average(sectalst, weights=weights))
#print(moving_ave)
#print(weighted_ave)
#print(Mexp_smooth(21, 8))
#print(exp_smooth(alpha, 3690.625, 3800))
#print(sectalst)
print(Move_ave(alst, 1, 3))
#print(Weight_ave(alst, weights, 7, 6))
print(MAD(alst, forlst, 2))
