n = int(input())
dic = list(input())
sum = 0
s = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    if dic[i] in s:
        sum += (s.index(dic[i])+1) * pow(31,i)
print(sum % 1234567891)