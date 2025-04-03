import sys
input = sys.stdin.readline

sen = input()
for s in sen:
    if s.isupper():
        print(s.lower(),end='')
    else:
        print(s.upper(),end='')