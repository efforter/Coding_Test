def solution(progresses, speeds):
    stack = []
    for progress, speed in zip(progresses,speeds):
        temp = 1
        while speed * temp + progress < 100:
            temp+=1
        stack.append(temp)
        
    print(stack)
    max_num = 0
    count = 1
    answer = []

    for i in range(len(stack)-1):
        max_num = max(stack[i],max_num)
        if max_num < stack[i+1]:
            answer.append(count)
            count = 1
        else:
            count += 1
        if i==len(stack)-2:
            answer.append(count)

    # print(answer)
    
    return answer