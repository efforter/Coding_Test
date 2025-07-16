def solution(n, arr1, arr2):
    decode_arr1 = []
    decode_arr2 = []
    result = []
    
    for a in arr1:
        temp = ""
        for i in range(n,0,-1):
            if 2**(i-1) <= a:
                a -= 2**(i-1)
                temp += str(1)
            else:
                temp += str(0)
        decode_arr1.append(temp)

    for a in arr2:
        temp = ""
        for i in range(n,0,-1):
            if 2**(i-1) <= a:
                a -= 2**(i-1)
                temp += str(1)
            else:
                temp += str(0)
        decode_arr2.append(temp)
    
    for i in range(n):
        temp = ""
        for j in range(n):
            if int(decode_arr1[i][j]) or int(decode_arr2[i][j])==1:
                temp += "#"
            else:
                temp += " "
        result.append(temp)

    return result