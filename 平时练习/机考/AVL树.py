
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        #所有结点刚加入树的时候，一定是高度为1的

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root = self._insert(value,self.root)

    def _insert(self, value, node):
        if not node:
            return Node(value)
        elif value<node.value:
            # 去平衡的插入左子树
            node.left = self._insert(value,node.left)
        else:
            node.right = self._insert(value,node.right)
        # 目前为止，node的字节点已经平衡好了，开始考察node本身的平衡
        balance = self._get_balance(node)
        node.height = 1+max(self._get_height(node.left),self._get_height(node.right))
        if balance>1:
            #初步判定是L
            if value<node.left.value:
                #LL
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return  self._rotate_right(node)
        elif balance<-1:
            if value>=node.right.value:
                return self._rotate_left(node)
            else:
                node.right=self._rotate_right(node.right)
                return  self._rotate_left(node)
        return node



    def _get_height(self, node):
        if node:
            return node.height
        else:
            return 0

    def _get_balance(self, node):
        if node:
            return self._get_height(node.left)-self._get_height(node.right)


    def _rotate_left(self, z):
        y = z.right
        T = y.left
        y.left = z
        z.right = T
        #小心这里更新的顺序，一定先更新子树的高度
        z.height = max(self._get_height(z.left), self._get_height(z.right)) + 1
        y.height = max(self._get_height(y.left),self._get_height(y.right))+1

        return y




    def _rotate_right(self, y):
        z = y.left
        T = z.right
        z.right = y
        y.left = T
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        z.height = max(self._get_height(z.left), self._get_height(z.right)) + 1
        return z



    def preorder(self):
        return self._preorder(self.root)
    def _preorder(self, node):
        if not node:
            return []
        return [node.value]+self._preorder(node.left)+self._preorder(node.right)

n = int(input().strip())
sequence = list(map(int, input().strip().split()))

avl = AVL()
for value in sequence:
    avl.insert(value)

print(' '.join(map(str, avl.preorder())))
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1:
            if value < node.left.value:	# 树形是 LL
                return self._rotate_right(node)
            else:	# 树形是 LR
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if value > node.right.value:	# 树形是 RR
                return self._rotate_left(node)
            else:	# 树形是 RL
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if not node:
            return []
        return [node.value] + self._preorder(node.left) + self._preorder(node.right)

n = int(input().strip())
sequence = list(map(int, input().strip().split()))

avl = AVL()
for value in sequence:
    avl.insert(value)

print(' '.join(map(str, avl.preorder())))
"""