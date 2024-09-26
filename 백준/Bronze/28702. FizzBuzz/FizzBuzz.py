def change(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0 and num % 5 != 0:
        return "Fizz"
    elif num % 3 != 0 and num % 5 == 0:
        return "Buzz"
    else:
        return num

ary = [0] * 3
for i in range(3):
    ary[i] = input()
    if(ary[i].isdigit() == True):
        check = i

if(check==0):
    print(change(int(ary[check])+3))
elif(check==1):
    print(change(int(ary[check])+2))
else:
    print(change(int(ary[check])+1))
