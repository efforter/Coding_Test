while True:
    ary = list(map(int,input()))
    if ary == [0]:
        break
    if ary == list(reversed(ary)):
        print("yes")
    else:
        print("no")