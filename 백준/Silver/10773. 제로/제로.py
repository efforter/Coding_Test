k = int(input())
ary = []
for i in range(k):
    value = int(input())
    if value > 0:
        ary.append(value)
    else:
        ary.pop()
print(sum(ary))