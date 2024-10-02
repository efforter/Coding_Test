def solution(s):
    p_count = y_count = 0
    for x in s:
        if x.lower()=='p':
            p_count += 1
        elif x.lower()=='y':
            y_count += 1
    if p_count==y_count:
        return True
    else:
        return False