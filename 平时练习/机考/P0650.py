# 只能构建二叉树了
from collections import deque
class TreeNode:
    def __init__(self,key = ""):
        self.key = key
        self.left = None
        self.right = None

def BuildTree(infix,post):
    if infix:
        root = TreeNode()
        key = post[-1]
        l = infix.index(key)
        root.key = key
        root.left = BuildTree(infix[:l],post[:l])
        root.right = BuildTree(infix[l+1:],post[l:-1])
        return root

def Traverse(tree):
    que = deque()
    que.append(tree)
    traverse = ""
    while que:
        for i in range(len(que)):
            s = que.popleft()
            if s.left:
                que.append(s.left)
            if s.right:
                que.append(s.right)
            traverse+=s.key
    return traverse

n=int(input())
for i in range(n):
    infix = input()
    post= input()
    tree = BuildTree(infix,post)
    print(Traverse(tree))
