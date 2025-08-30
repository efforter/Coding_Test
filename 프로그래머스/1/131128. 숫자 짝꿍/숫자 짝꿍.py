from collections import Counter

def solution(X, Y):
    answer = ''
    x = Counter(X)
    y = Counter(Y)
    
    for i in range(9,-1,-1):
        if x[f"{i}"] != 0 and y[f"{i}"] != 0:
            temp = min(x[str(i)],y[str(i)])
            answer += str(i) * temp
    
    if not answer:
        return "-1"
    elif answer.startswith("0"):
        return "0"
    else:
        return answer
    
    
        
    # return answer