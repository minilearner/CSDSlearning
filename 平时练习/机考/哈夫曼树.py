import heapq
from collections import deque
n = int(input())
class Node:
    def __init__(self,item,frec):
        self.item = item
        self.frec = frec
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.frec<other.frec:
            return True
        elif self.frec == other.frec and self.item<other.item:
            return True
        return False


def BuildHuffman(alpha):
    heapq.heapify(alpha)
    while len(alpha) > 1:
        left = heapq.heappop(alpha)
        right = heapq.heappop(alpha)

        mingle = Node(min(left.item,right.item), left.frec + right.frec)

        mingle.left = left
        mingle.right = right
        alpha.append(mingle)
    return alpha[0]

def bfs(tree,item):
    que = deque([[tree,""]])
    while que:
        s = que.popleft()
        L=s[0].left
        R = s[0].right

        if L and R:
            if L.left == None:
                if L.item == item:
                    return s[1]+"0"
            else:
                que.append([L,s[1]+"0"])
            if R.left == None:
                if R.item == item:
                    return s[1]+"1"
            else:
                que.append([R,s[1]+"1"])

alpha = []
for i in range(n):
    s,frec = input().split()

    alpha.append(Node(s,int(frec)))

Huff = BuildHuffman(alpha)
while True:
    try:
        expr = input()
    except EOFError:
        break
    else:
        if expr[0].isdigit():
            result = []
            current = Huff
            for x in expr:
                if x == "0":
                    current = current.left
                else:
                    current = current.right
                if current.left == None:
                    result.append(current.item)
                    current = Huff
            print("".join(result))
        else:
            result = []
            for x in expr:
                result.append(bfs(Huff,x))
            print("".join(result))


