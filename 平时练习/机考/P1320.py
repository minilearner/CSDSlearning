from collections import deque
class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def BuildTree(content):
    s = TreeNode(content[0])
    l = [x for x in content if x<s.key]
    r = [x for x in content if x>s.key]
    if l:
        s.left = BuildTree(l)
    if r:
        s.right = BuildTree(r)
    return s

def traverse(tree):
    que = deque([tree])
    traverse = []
    while que:
        for i in range(len(que)):
            s = que.popleft()
            if s.left:
                que.append(s.left)
            if s.right:
                que.append(s.right)
            traverse.append(str(s.key))
    return " ".join(traverse)

a = list(map(int,input().split()))
s = BuildTree(a)
print(traverse(s))




