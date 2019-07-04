def conn(f,groups):
    for grp in groups:
        if f[0] in grp and f[1] in grp:
            return 'Yes'
    return 'No'
f='a'

tlist =[]
while( f !='-1'):
    f= input('enter pairs or enter -1  to end input:')
    if f !='-1':
        tlist.append(set(f.split(',')))
groups = []
for pair in tlist:
    f=0
    com = []
    for grp in groups:
        if pair & grp != set():
            com.append(grp)
            f=1
    if f==0:
        groups.append(pair)
    else:
        merge =pair
        for c in com:
            merge = merge|c
            groups.remove(c)
        groups.append(merge)

print(groups)
f= input('enter pair:')
f=list(f.split(','))
print(conn(f,groups))


        
            

