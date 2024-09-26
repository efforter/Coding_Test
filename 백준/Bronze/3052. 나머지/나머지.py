list_ = []
for i in range(10):
    a = int(input())
    list_.append(a%42)
print(len(set(list_)))