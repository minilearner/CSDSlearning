
class Node:
    def __init__(self):
        self.left = None
        self.right = None
# 求出以node为根结点子树的高度
def Treeheight(node):
    if node == None:
        return -1
    else:
        return max(Treeheight(node.left),Treeheight(node.right))+1
# 数出树中结点的个数
def Countleaves(node):
    if node == None:
        return 0
    l = node.left
    r = node.right
    if l == None and r == None:
        return 1
    else:
        return Countleaves(node.left)+Countleaves(node.right)

n = int(input())
if n == 0:
    print(-1,0)
    exit()
Nodes = [Node() for i in range(n)]
parents = [True for i in range(n)]
for i in range(n):
    l,r = map(int,input().split())
    if l !=-1:
        Nodes[i].left = Nodes[l]
        parents[l]=False
    if r !=-1:
        Nodes[i].right = Nodes[r]
        parents[r]=False
s = parents.index(True)
print(Treeheight(Nodes[s]),Countleaves(Nodes[s]))


