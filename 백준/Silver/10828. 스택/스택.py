import re
import sys
input = sys.stdin.readline

stack = []

def push(number):
    stack.append(number)

def pop():
    if stack:
        print(stack[-1])
        stack.pop()
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

n = int(input())
for i in range(n):
    s = input()
    if 'push' in s:
        a = re.findall(r'\d+', s)
        push(int(*a))
    elif 'pop' in s:
        pop()
    elif 'size' in s:
        size()
    elif 'empty' in s:
        empty()
    else:
        top()