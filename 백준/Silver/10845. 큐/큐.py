import re
import sys
input = sys.stdin.readline

queue = []

def push(number):
    queue.append(number)

def pop():
    if queue:
        print(queue[0])
        queue.remove(queue[0])
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
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
    elif 'front' in s:
        front()
    else:
        back()