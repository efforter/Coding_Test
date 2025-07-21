from collections import deque

def solution(priorities, location):
    # [3,1,2,4,2] => D A C E B
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    sort_arr = sorted(priorities, reverse=True)
    answer = []
    
    while sort_arr:
        if queue[0][1] == sort_arr[0]:
            answer.append(queue.popleft())
            sort_arr.pop(0)
        else:
            queue.append(queue.popleft())
    
    for i in range(len(answer)):
        if answer[i][0]==location:
            return i+1