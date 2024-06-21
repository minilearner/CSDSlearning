infix = input()
post = input()
def preorder(infix,post):
    if infix:
        key = post[-1]
        l = infix.index(key)
        print(key,end="")
        preorder(infix[:l],post[:l])
        preorder(infix[l+1:],post[l:-1])
preorder(infix,post)