import sys
input = sys.stdin.readline

n = int(input())
tree = dict()

for _ in range(n):
    v,l,r = input().strip().split()
    tree[v] = [l,r]

def preorder(s):
    if s != '.':
        print(s, end='')
        preorder(tree[s][0])
        preorder(tree[s][1])

def inorder(s):
    if s != '.':
        inorder(tree[s][0])
        print(s, end='')
        inorder(tree[s][1])

def postorder(s):
    if s != '.':
        postorder(tree[s][0])
        postorder(tree[s][1])
        print(s, end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')