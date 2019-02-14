name = ["A", "B", "C", "D", "E", "F", "G"]
time = [3, 5, 1, 10, 4, 5, 10]

Sheet = {}
IP = []
ES = {}
EF = {}
LS = {}
LF = {}

def Relation(Main, Branch):
    mn = Main
    br = []
    MainR = mn
    for rch in Branch:
        BranchR = rch
        br.append(BranchR)
    MB = [MainR, br]
    IP.append(MB)
    
def Activity():
    if len(name) != len(time):
        if len(name) > len(time):
            print("Missing Time Value.")
        elif len(time) > len(name):
            print("Missing Name value.")
    else:
        for num in range(len(name)):
            n = name[num]
            t = time[num]
            Sheet[f'{n}'] = t


print(Activity())
print('Sheet = ' + str(Sheet))
Relation("D", ["B"])
Relation("E", ["A", "D"])
Relation("F", ["C"])
Relation("G", ["E", "F"])
print('IP = ' + str(IP))


def ESfinder():
    for n in range(len(name)):
        print(name[n])
        rell = []
        for rel in range(len(IP)):
            tion = IP[rel][0]
            zion = IP[rel][1]
            #print(tion)
            if tion == name[n]:
                print("Relations")
                for rolo in range(len(zion)):
                    val = Sheet[zion[rolo]]
                    rell.append(val)
            else:
                valnull = 0
                rell.append(valnull)
                #print("none")
            if max(rell) == 0:
                ES[f'{name[n]}'] = max(rell)
                EF[f'{name[n]}'] = max(rell) + time[n]
            elif any(x > 0 for x in rell):
                ES[f'{name[n]}'] = max(rell)
                EF[f'{name[n]}'] = max(rell) + time[n]
            print(rell)
            
            #if len(rell) > 0:
             #   print("SIII")
              #  ES[f'{name[n]}'] = 1
            #elif len(rell) == 0:
             #   ES[f'{name[n]}'] = 0
              #  continue


print(ESfinder())
print('ES = ' + str(ES))
print('EF = ' + str(EF))
