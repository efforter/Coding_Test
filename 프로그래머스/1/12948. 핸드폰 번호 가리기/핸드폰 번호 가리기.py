def solution(phone_number):
    result = ""
    for i in range(len(phone_number)-4):
        result += "*"
    return result + phone_number[-4:]