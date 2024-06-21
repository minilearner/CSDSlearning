class Node:
    def __init__(self):
        self.left = None
        self.right = None

def Treedepth(node):
    if node == None:
        return 0
    else:
        return max(Treedepth(node.left),Treedepth(node.right))+1

n = int(input())

Nodes = [Node() for i in range(n)]
parents = [True for i in range(n)]
for i in range(n):
    l,r = map(int,input().split())
    if l !=-1:
        Nodes[i].left = Nodes[l-1]
        parents[l-1]=False
    if r !=-1:
        Nodes[i].right = Nodes[r-1]
        parents[r-1]=False
s = parents.index(True)
print(Treedepth(Nodes[s]))