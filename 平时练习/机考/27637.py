class TreeNode:
    def __init__(self,key = ""):
        self.key = key
        self.left = None
        self.right = None
alphabet = [chr(x) for x in range(65,91)]
def BuildTree(expression):
    pstack = []
    if expression!="*":
        for x in expression:
            if x in alphabet :
                s = TreeNode(x)
                pstack.append(s)
            elif x == "*":
                pstack.append("*")
            elif x == "(":
                pstack.append("(")
            elif x == ")":
                if pstack[-2]=="(":
                    pstack[-3].left = pstack[-1]
                    pstack.pop()
                    pstack.pop()
                elif pstack[-3]=="(":
                    if pstack[-2] == "*":
                        pstack[-4].right = pstack[-1]
                        pstack.pop()
                        pstack.pop()
                        pstack.pop()
                    elif pstack[-1]=="*":
                        pstack[-4].left = pstack[-2]
                        pstack.pop()
                        pstack.pop()
                        pstack.pop()
                    else:
                        pstack[-4].right = pstack[-1]
                        pstack[-4].left = pstack[-2]
                        pstack.pop()
                        pstack.pop()
                        pstack.pop()
        return pstack[0]
    else:
        return None

def preorder(tree):
    if tree:
        print(tree.key,end = "")
        preorder(tree.left)
        preorder(tree.right)

def infixorder(tree):
    if tree:
        infixorder(tree.left)
        print(tree.key, end="")
        infixorder(tree.right)

n = int(input())
for i in range(n):
    s = BuildTree(input())
    preorder(s)
    print("")
    infixorder(s)
    print("")

