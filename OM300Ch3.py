name = ['A','B','C','D','E','F','G']
time = [3,5,1,10,4,5,10]
Ip = [[False], [False], [False], ['B'], ['A','D'], ['C'], ['E','F']]
Activities = []
If = []
Es = {}
Ef = {}
Ls = {}
Lf = {}

def ActInput(name, time, Ip):
    Activity = {}
    Activity.update({'name':'%s'%(name), 'time':'%d'%(time), 'Ip': Ip})
    Activities.append(Activity)
def MActInput(nlst, tlst, Iplst):
    if len(tlst) != len(nlst):
        print('RangeError, length of time does not match length of names')
    elif len(Iplst) != len(nlst):
                print('RangeError, length of Ip does not match length of names')
    else:
        for x in range(len(nlst)):
            nx = nlst[x]
            tx = tlst[x]
            Ipx = Iplst[x]
            ActInput(nx,tx,Ipx)


ActInput('A', 3, ['B','C'])
ActInput('B', 6, ['D'])

print(Activities)


#test = [{"tname":3}, {"tname":6}, {"tname":8}]
#def pick(x):
    #return test[x]['tname']
#def ptest():
 #   ans = []
  #  for x in range(len(test)):
   #     px = pick(x)
    #    ans.append(px)
    #return ans
#print(ptest()) returns [3,6,8]