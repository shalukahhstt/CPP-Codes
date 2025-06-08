number = input()
def char(a,b,num):
    print(chr(int(num[a:b]) + 96), end="")

if len(number)==4:
    for i in number:
        if int(i)>0:
            print(chr(int(i)+96),end="")

    for j in range(2):
        print(" ",end="")
        if int(number[:2])<27 and int(number[:2])>0:
            char(0,2,number)
        if int(number[3:])<27 and j==0 and int(number[3:])>0:
            char(2,4,number)
        else:
            if int(number[2])>0:
                print(chr(int(number[2])+96),end="")
            if int(number[3])>0:
                print(chr(int(number[3])+96),end="")
            break
    if int(number[1:3]) < 27 and int(number[1:3])>0:
        print(" ", end="")
        if int(number[0])>0:
            print(chr(int(number[0]) + 96), end="")
        char(1,3,number)
        if int(number[3])>0:
            print(chr(int(number[3]) + 96), end="")
    else:pass
    if int(number[2:]) < 27 and int(number[2:])>0:
        print(" ", end="")
        if int(number[0])>0:
            print(chr(int(number[0]) + 96), end="")
        if int(number[1])>0:
            print(chr(int(number[1]) + 96), end="")
        char(2,4,number)

    else:pass
