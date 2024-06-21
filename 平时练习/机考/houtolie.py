from collections import deque

# 创造结点类型
class TreeNode:
    def __init__(self,item):
        self.key = item
        self.left = None
        self.right = None

# 把后序表达式转化为树状图
def BuildTree(plist):
    pstack = [] # 用来模拟运算过程
    for x in plist:
        node = TreeNode(x)
        if x.isupper():
            node.right = pstack.pop()
            node.left = pstack.pop()
        pstack.append(node)
    return pstack[0]

# 从树状图中读取列序
def listorder(node):
    que = deque()
    traversal = []
    que.append(node)
    while que:
        for x in range(len(que)):
            s = que.popleft()
            traversal.append(s.key)
            if s.left:
                que.append(s.left)
            if s.right:
                que.append(s.right)

    return traversal

n = int(input())

for _ in range(n):
    string = input()
    result = listorder(BuildTree(string))
    result.reverse()
    print("".join(result))


