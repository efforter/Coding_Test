while True:
    text = input()
    if text =='.':
        break
    stack = []
    count = 1
    for s in text:
        if s=='(' or s=='[':
            stack.append(s)
        elif s==')':
            if '(' in stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    count = 0
                    break
            else:
                count = 0
                break
        elif s==']':
            if '[' in stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    count = 0
                    break
            else:
                count = 0
                break
    if count==1 and len(stack) == 0:
        print("yes")
    else:
        print("no")