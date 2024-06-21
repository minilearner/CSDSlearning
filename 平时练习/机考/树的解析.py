class Node:
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def addl(self,item=None):
        t = Node(item)
        t.parent = self
        self.left = t

    def addr(self,item = None):
        t = Node(item)
        t.parent = self
        self.right = t

def build_parseTree(express):
    fexp = express.split()
    result = Node()
    result.parent = result
    currentTree = result
    for x in fexp:
        if x == "(":
            currentTree.addl()
            currentTree = currentTree.left
        elif x in ["+","-","*","/"]:
            currentTree.key = x
            currentTree.addr()
            currentTree = currentTree.right
        elif x == ")":
            currentTree = currentTree.parent
        else:
            currentTree.key = x
            currentTree = currentTree.parent
    return result

def Traverse(Tree,methods = "preorder"):
    if Tree:
        if methods == "preorder":
            print(Tree.key,end = " ")
        Traverse(Tree.left,methods)
        if methods == "inorder":
            print(Tree.key,end = " ")
        Traverse(Tree.right,methods)
        if methods == "postorder":
            print(Tree.key,end = " ")

exp = "( ( 7 + 3 ) * ( 5 - 2 ) )"
s = build_parseTree(exp)
for mode in ["preorder","inorder","postorder"]:
    Traverse(s,mode)
    print("")




