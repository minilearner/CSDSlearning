# 实际上树的解析那一章节中要求中序表达式没有多余的括号，所以不能直接使用树的解析
# 可以先把中序表达式转后序表达式，再把后序表达式转化为树，最后用树的遍历将树转化为没有多余括号的中序表达式
class TreeNode:
    def __init__(self,key= ""):
        self.key = key
        self.left = None
        self.right = None
def infix_to_postfix(expression):
    precedence = {"or":1,"and":2,"not":3,"(":0}
    op = []
    output = []

    for x in expression:
        if x in ["True","False"]:
            output.append(x)
        elif x in ["or","and","not"]:
            while op and precedence[op[-1]]>=precedence[x]:
                output.append(op.pop())
            op.append(x)
        elif x == "(":
            op.append(x)
        elif x == ")":
            while op and op[-1]!="(":
                output.append(op.pop())
            op.pop()

    output.extend(op[::-1])
    return output

def BuildTree(postexp):
    pstack = []
    for x in postexp:
        if x in ["True","False"]:
            s = TreeNode(x)
            pstack.append(s)
        elif x == "not":
            s = TreeNode(x)
            s.left = pstack.pop()
            pstack.append(s)
        else:
            s = TreeNode(x)
            s.right = pstack.pop()
            s.left = pstack.pop()
            pstack.append(s)
    return pstack[0]

def treetoinfix(tree):
    precedence = {"or": 1, "and": 2, "not": 3,"True":4,"False":4}
    output = []
    if tree:
        if tree.key in ["or","and"]:
            if precedence[tree.key]>precedence[tree.left.key]:
                opl = ["("]
                opl.extend(treetoinfix(tree.left))
                opl.append(")")
            else:
                opl = treetoinfix(tree.left)
            middle = [tree.key]
            if precedence[tree.key] > precedence[tree.right.key]:
                opr = ["("]
                opr.extend(treetoinfix(tree.right))
                opr.append(")")
            else:
                opr = treetoinfix(tree.right)
            output = opl
            output.extend(middle)
            output.extend(opr)
        elif tree.key in ["True","False"]:
            output = [tree.key]
        elif tree.key == "not":
            if precedence["not"]>precedence[tree.left.key]:
                output = ["not","("]
                output.extend(treetoinfix(tree.left))
                output.append(")")
            else:
                output = ["not"]
                output.extend(treetoinfix(tree.left))
    return output

s = input().split()
a = infix_to_postfix(s)


b = BuildTree(a)
c = treetoinfix(b)
print(" ".join(c))
