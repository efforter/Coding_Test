def solution(answers):
    student_1 = [1,2,3,4,5] * (len(answers)//5+1)
    student_2 = [2,1,2,3,2,4,2,5] * (len(answers)//8+1)
    student_3 = [3,3,1,1,2,2,4,4,5,5] * (len(answers)//10+1)
    
    answer = [0,0,0]

    for i in range(len(answers)):
        if answers[i]==student_1[i]: answer[0] += 1
        if answers[i]==student_2[i]: answer[1] += 1
        if answers[i]==student_3[i]: answer[2] += 1
    
    maxi = max(answer)
    temp = []
    for i in range(len(answer)):
        answer[i] -= maxi
        if answer[i] == 0:
            temp.append(i+1)

    return temp