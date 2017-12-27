lst=[]
minlst=[]
maxlst=[]
rstlst=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    lst.append([score,name])
mini=min(lst)
maxi=max(lst)
for i in range(0,len(lst)):
    if lst[i][0]==mini[0]:
        minlst.append(lst[i])
    elif lst[i][0]==maxi[0]:
        maxlst.append(lst[i])
    else:
        rstlst.append(lst[i])
sortedlst=sorted(rstlst)
if len(sortedlst)==0:
    for i in range(0,len(maxlst)):
        print maxlst[i][1]
else:
    minrstlst=min(sortedlst)
    for i in range(0,len(sortedlst)):
        if sortedlst[i][0]==minrstlst[0]:
            print sortedlst[i][1]
        else:
            exit(0)