
def postorder(infix,pre):
    if infix:
        key = pre[0]
        l = infix.index(key)
        postorder(infix[:l],pre[1:l+1])
        postorder(infix[l+1:],pre[l+1:])
        print(key,end = "")

while True:
    try:
        pre = input()
        infix = input()
    except EOFError:
        break
    else:
        postorder(infix,pre)
        print("")
