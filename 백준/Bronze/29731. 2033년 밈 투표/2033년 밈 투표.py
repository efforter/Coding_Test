import sys
input = sys.stdin.readline

n = int(input())
ary = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you',
'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']

count = 0
for _ in range(n):
       s = input().rstrip()
       if s not in ary:
              count = 1
if count == 0:
       print("No")
else:
       print("Yes")