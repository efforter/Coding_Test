t = int(input())
for a in range(t):
    k = int(input())
    n = int(input())
    floor_0 = [x for x in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            floor_0[i] += floor_0[i-1]
    print(floor_0[-1])