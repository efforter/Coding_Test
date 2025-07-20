def solution(clothes):
    '''
    [
     ["yellow_hat", "headgear"],
     ["green_turban", "headgear"],
     ["blue_sunglasses", "eyewear"],
     ["white_sunglasses", "eyewear"],
     ["red_sunglasses", "eyewear"]
     ["blue_sunglasses", "face"],
     ["smoky_makeup", "face"]
     ]
     (2+1) * (3+1) * (2+1) - 1 = 35
    '''
    dic = {}
    for value, key in clothes:
        if key in dic:
            dic[key] += [value]
        else:
            dic[key] = [value]
    
    answer = 1
    for key, value in dic.items():
        answer *= len(value)+1

    return answer - 1