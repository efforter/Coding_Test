def solution(s, n):
    letter = ''
    for i in s:
        if i==' ':
            letter += i
        else:
            if i.isupper():
                letter += chr((ord(i)-ord('A')+n)%26 + ord('A'))
            elif i.islower():
                letter += chr((ord(i)-ord('a')+n)%26 + ord('a'))
    return letter