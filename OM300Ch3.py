name = []
time = []
Ip = []
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