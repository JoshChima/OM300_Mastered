name = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
time = [3,5,1,10,4,5,10]
Ip = ['None', 'None', 'None', ['B'], ['A','D'], ['C'], ['E','F']]
Activities = []
timelib = {}
Iplib = {}
Iflib = {}
Es = {}
Ef = {}
Ls = {}
Lf = {}
Slack = {}
Criticalpath = []

def ActInput(name, time, Ip):
    Activity = {}
    Activity.update({'name':'%s'%(name), 'time':'%d'%(time), 'Ip': Ip})
    timelib.update({'%s'%(name):time})
    Iplib.update({'%s'%(name): Ip})
    Activities.append(Activity)
def Ifoutput(Anum):
    for z in name:
        for y in range(len(Iplib[z])):
            if Iplib[z][y] == Anum:
                Iflib.update({'%s'%(Anum): z})
def ESoutput(Anum):
    if Iplib[Anum] == 'None':
        ES = 0
        Es.update({'%s'%(Anum):ES})
    elif Iplib[Anum] != 'None' and len(Iplib[Anum]) == 1:
        Ipnu = Iplib[Anum][0]
        IpEf = Ef[Ipnu]
        Es.update({'%s'%(Anum):IpEf})
    else:
        IpEfs = []
        for k in Iplib[Anum]:
            IpEf = Ef[k]
            IpEfs.append(IpEf)
        ES = max(IpEfs)
        Es.update({'%s'%(Anum):ES})
def EFoutput(Anum):
    EF = int(Es[Anum]) + int(timelib[Anum])
    Ef.update({'%s'%(Anum):EF})
def LSoutput(Anum):
    if Iflib.get(Anum) == None:
        LS = Es[Anum]
        Ls.update({'%s'%(Anum):LS})
    else:
        LS = int(Lf[Anum]) - int(timelib[Anum])
        Ls.update({'%s'%(Anum):LS})
def LFoutput(Anum):
    if Iflib.get(Anum) == None:
        IfLf = Ef[Anum]
        Lf.update({'%s'%(Anum):IfLf})
    else:
        Ifnu = Iflib[Anum]
        IfLs = Ls[Ifnu]
        Lf.update({'%s'%(Anum):IfLs})
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
def Criticalpth(Anum):
    Slck = int(Ls[Anum]) - int(Es[Anum])
    Slack.update({'%s'%(Anum):Slck})
    if Slck == 0:
        Criticalpath.append(Anum)
def Actmove1(nlst, tlst, Iplst):
    MActInput(nlst, tlst, Iplst)
    for x in name:
        Ifoutput(x)
        if Iplib[x] == 'None':
            ESoutput(x)
            EFoutput(x)            
        if Iplib[x] != 'None':
            ESoutput(x)
            EFoutput(x)
    for y in reversed(name):
        LFoutput(y)
        LSoutput(y)
    for z in name:
        Criticalpth(z)
    print('ES:')
    print(Es)
    print('EF:')
    print(Ef)
    print('LS:')
    print(Ls)
    print('LF:')
    print(Lf)
    print('Critical Path:')
    print(Criticalpath)
print(Actmove1(name, time, Ip))
#print(Activities)
#print(timelib)
#print(Iplib)
#print(Iflib)
