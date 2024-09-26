t = int(input())
for i in range(t):
    h, w, n = map(int,input().split())
    floor = int(n%h)
    room = int(n/h) + 1
    print(h*100 + room-1 if floor==0 else floor*100 + room)