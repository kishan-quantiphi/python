def last(n):
    return n[-1]   
def sort(tlist):
    return sorted(tlist, key=last)
f='a'
tlist =[]
while( f !='-1'):
    f= input('enter tuple elements or enter -1  to end input:')
    if f !='-1':
        tlist.append(tuple(map(int,f.split(','))))
print(sort(tlist))