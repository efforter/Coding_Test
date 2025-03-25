import sys
input = sys.stdin.readline

while True:
    s = list(map(str, input().split()))
    find = s[0]
    target = s[1:]
    if find == '#':
        break
    print(find, str(target).lower().count(find))