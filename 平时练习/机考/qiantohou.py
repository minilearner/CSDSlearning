n = int(input())
# 根据前序遍历构造树，再从树得到后序遍历，easy
s = list(map(int,input().split()))
def postorder(preorder):
    if preorder:
        key = preorder[0]
        left = [x for x in preorder if x<key]
        right = [x for x in preorder if x>key]
        postorder(left)
        postorder(right)
        print(key,end = " ")
postorder(s)