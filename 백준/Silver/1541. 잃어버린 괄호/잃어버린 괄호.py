import sys
input = sys.stdin.readline

cal = input()
sen = cal.split('-')
# print(sen)
count = 0
for i in range(len(sen)):
    if '+' in sen[i]:
        a = list(map(int,sen[i].split('+')))
        sen[i] = sum(a)
    if i==0:
        count = int(sen[i])
    else:
        count -= int(sen[i])
# print(sen)
print(count)