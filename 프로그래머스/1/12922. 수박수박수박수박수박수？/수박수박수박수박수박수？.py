def solution(n):
    letter = "수박"
    if n%2==0:
        return letter*(n//2)
    else:
        return letter*(n//2) + "수"