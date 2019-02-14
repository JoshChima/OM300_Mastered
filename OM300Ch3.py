name = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
time = [3,5,1,10,4,5,10]
Ip = [['None'], ['None'], ['None'], ['B'], ['A','D'], ['C'], ['E','F']]
Activities = []
timelib = {}
Iplib = {}
If = []
Es = {}
Ef = {}
Ls = {}
Lf = {}

def ActInput(name, time, Ip):
    Activity = {}
    Activity.update({'name':'%s'%(name), 'time':'%d'%(time), 'Ip': Ip})
    timelib.update({'%s'%(name):'%d'%(time)})
    Iplib.update({'%s'%(name): Ip})
    Activities.append(Activity)
def ESoutput(Anum):
    if timelib[Anum] == 'None':
        ES = 0
    elif timelib[Anum] > 0 and len(timelib[Anum]) == 1:
        Ipnu = Iplib[Anum]
        IpEf = Ef[Ipnu]
        ES = IpEf
    else:
        IpEfs = []
        for k in Iplib[Anum]:
            Ipnu = Iplib[Anum][k]
            IpEf = Ef[Ipnu]
            IpEfs.append(IpEf)
        ES = max(IpEfs)
        
    Esn = Activities[Anum]['name']
    Est = timelib[Anum]
    EsIp = Iplib[Anum]
def MActInput(nlst, tlst, Iplst):
    if len(tlst) != len(nlst):
        print('RangeError, length of time does not match length of names')
    elif len(Iplst) != len(nlst):
        print('RangeError, length of Ip does not match length of names')
    else:
        x = 0
        while x in range(0, len(nlst)):
            nx = nlst[x]
            tx = tlst[x]
            Ipx = Iplst[x]
            x += 1
            ActInput(nx,tx,Ipx)
def Actmove(nlst, tlst, Iplst):
    MActInput(nlst, tlst, Iplst)
    for x in name:
        if timelib[x] == 'None':
            


#ActInput('A', 3, ['B','C'])
#ActInput('B', 6, ['D'])

print(MActInput(name, time, Ip))
print(Activities)
print(timelib)
print(Iplib)

#test = [{"tname":3}, {"tname":6}, {"tname":8}]
#lndtest = {'T1':[3,4], 'T2':[8,6], 'T3':[7,9]}
#def pick(x):
    #return test[x]['tname']
#def ptest():
 #   ans = []
  #  for x in range(len(test)):
   #     px = pick(x)
    #    ans.append(px)
    #return ans
#print(ptest()) returns [3,6,8]
#testd = test[0]['tname']
#print(testd)
#print(lndtest['T1'][1]) returns [4]
