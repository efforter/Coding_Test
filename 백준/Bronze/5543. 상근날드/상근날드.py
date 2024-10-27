import sys
input = sys.stdin.readline

ham = 2001
for i in range(3):
    a = int(input())
    if a<ham:
        ham = a

drink = 2001
for i in range(2):
    b = int(input())
    if b<drink:
        drink = b
print(ham+drink-50)