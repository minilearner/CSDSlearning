class Node:
    def __init__(self):
        self.son = []
        self.content=None
Nodes = [Node() for i in range(26)]
Alphabet = [chr(i) for i in range(65,91)]
for i in range(26):
    Nodes[i].content=Alphabet[i]
def buildTree(string):
    s = list(string)
    stack = []
    cnt = 0
    for item in s:
        if item in Alphabet:
            stack.append(item)
        if item == "(":
            cnt+=1
            stack.append("(")
        elif item == ")":
            sons = []
            while stack[-1]!="(":
                sons.append(ord(stack.pop())-65)
            stack.pop()
            sons.reverse()
            father = ord(stack[-1])-65
            Nodes[father].son.extend(sons)
def preorder(node):
    output = [node.content]
    for x in node.son:
        output.append(preorder(Nodes[x]))
    return "".join(output)

def postorder(node):
    output=[]
    for x in node.son:
        output.append(postorder(Nodes[x]))
    output.append(node.content)
    return "".join(output)

str = input()
buildTree(str)
print(preorder(Nodes[ord(str[0])-65]))
print(postorder(Nodes[ord(str[0])-65]))



