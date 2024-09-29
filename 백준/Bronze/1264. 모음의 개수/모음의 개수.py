import sys
input = sys.stdin.readline

while True:
    sentence = input()
    count = 0
    for s in sentence:
        if s=='#':
            exit(0)
        if s.upper()=='a' or s.lower()=='a' or s.upper()=='e' or s.lower()=='e' or s.upper()=='i' or s.lower()=='i' or s.upper()=='o' or s.lower()=='o' or s.upper()=='u' or s.lower()=='u':
            count+=1
    print(count)