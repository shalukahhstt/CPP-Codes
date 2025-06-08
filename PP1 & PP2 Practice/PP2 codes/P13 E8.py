name=input()
input_f=open(name,'r')
line=input_f.readlines()
for i in line:
    word=i.split()
    str1=word[0]
    str2=word[1]
    x=0
    if len(str1)>=len(str2):
        for i in range(len(str2)):
            if str1[i]==str2[i]:
                continue
            elif ord(str1[i])>ord(str2[i]):
                x=1
                break
            elif ord(str2[i])>ord(str1[i]):
                x=2
                break
        if x==1:
            print(str2+" "+str1)
        elif x==2:
            print(str1 + " " + str2)
        elif x==0:
            print(str2 + " " + str1)
    elif len(str1)<len(str2):
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                continue
            elif ord(str1[i]) > ord(str2[i]):
                x = 1
                break
            elif ord(str2[i]) > ord(str1[i]):
                x = 2
                break
        if x == 1:
            print(str2 + " " + str1)
        elif x == 2:
            print(str1 + " " + str2)
        elif x==0:
            print(str1 + " " + str2)