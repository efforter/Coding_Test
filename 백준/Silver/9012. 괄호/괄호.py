t = int(input())
for _ in range(t):
    sentence = input()
    stack = []
    check = True
    for s in sentence:
        if s=='(':
            stack.append(s)
        elif s==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                check = False
                break
    if len(stack) == 0 and check==True:
        print("YES")
    else:
        print("NO")