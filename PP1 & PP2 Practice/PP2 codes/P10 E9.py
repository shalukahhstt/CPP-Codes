f_name=input()
input_f = open(f_name,'r')
line=input_f.readlines()
for i in line:
    words=i.split()
    str1=list(words[0])
    str2=list(words[1])
    if len(str1)!=len(str2):
        print(' Not Anagram')
    else:
        for k in str1:
            if k in str2:
                str2.remove(k)
                x=1
            else:
                print('Not Anagram')
                x=0
                break
        if x==1:
            print("Anagram")
