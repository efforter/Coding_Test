def solution(a, b):
    dates = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    return days[(sum(dates[:a-1])+b)%7]