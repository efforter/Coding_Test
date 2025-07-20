import re

def solution(new_id):
    # step1
    answer = str.lower(new_id)
    # step2
    answer = re.sub(r'[^a-z0-9\-_.]','',answer)
    # step3
    answer = re.sub(r'\.+','.',answer)
    # step4
    answer = re.sub('^[.]|[.]$','',answer)
    # step5
    answer = 'a' if not answer else answer
    # step6
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = re.sub('[.]$','',answer)
    
    # step7
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer