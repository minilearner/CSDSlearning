N,k = map(int,input())
def find(i):
    if parent[i]!=i:
        parent[i]=find(parent[i])
    return parent[i]

def union(i,j):
    irep = parent[i]
    jrep = parent[j]
    if irep == jrep:
        return
    else:
        parent[irep]=jrep
        type[irep] = type[jrep]

parent = [i for i in range(N)]
type = [None for i in range(N)]

cnt = 0
flag = False
for i in range(K):
    re,x,y = map(int,input())
    if re == 1:
        type[y]="A"
        union(x,y)

