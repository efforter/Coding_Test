def solution(price, money, count):
    temp = 0
    for i in range(1,count+1):
        temp += i
    result = price * temp
    return 0 if result <= money else result - money
    