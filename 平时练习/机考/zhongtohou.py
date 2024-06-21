# shunting yard algorithm 烂熟于心

def infix_to_postfix(expression):
    precedence = {"+":1,"-":1,"*":2,"/":2,"(":0}
    op = []
    output = []

    for x in expression:
        if x.isdigit() or x == ".":
            output.append(x)
        elif x in "+-*/":
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

n = int(input())
for _ in range(n):
    temp  = infix_to_postfix(input())
    output = []
    for i in range(len(temp)-1):
        if temp[i].isdigit() and temp[i+1]!=".":
            output.append(temp[i])
            output.append(" ")
        elif temp[i].isdigit() and temp[i+1]==".":
            output.append(temp[i])
        elif temp[i] in "+-*/":
            output.append(temp[i])
            output.append(" ")
        elif temp[i]==".":
            output.append(".")
    output.append(temp[-1])
    s = "".join(output)
    print(s.rstrip())





