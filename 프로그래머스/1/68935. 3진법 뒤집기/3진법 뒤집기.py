def change_10_to_3(n):
    temp = 1
    number = 0
    answer = ''
    while temp <= n/3:
        temp *= 3
        number+=1
    for i in range(number,-1,-1):
        a = 0
        while n >= 3**i:
            a+=1
            n -= 3**i
        answer += str(a)
    return answer

# def reverse_3(answer):
#     return answer[::-1]

def chage_3_to_10(answer):
    result = 0
    for i in range(len(answer)):
        result += int(answer[i]) * 3**(i)
    return result


def solution(n):
    answer = change_10_to_3(n)
    # print("n (3진법) : ", answer)
    # answer = reverse_3(answer)
    # print("앞뒤 반전 (3진법) : ", answer)
    answer = chage_3_to_10(answer)
    
    return answer