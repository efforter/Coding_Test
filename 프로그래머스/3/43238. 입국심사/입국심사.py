def solution(n, times):
    # T // 7 + T // 10 >= n
    left = 1
    right = max(times)*n
    answer = 0
    
    while left <= right:
        mid = (left+right)//2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
            
    return answer