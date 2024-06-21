class disjSet:
    def __init__(self,n):
        self.rank = [1 for i in range(n)]
        self.parent = [i for i in range(n)]

    def find(i):
        if self.parent[i]!=i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def Union(self,i,j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        else:
            if self.rank[irep]<self.rank[jrep]:
                self.parent[irep]=jrep

            elif self.rank[jrep]<self.rank[irep]:
                self.parent[jrep]=irep

            else:
                self.parent[jrep]=irep
                self.rank[irep]+=1


