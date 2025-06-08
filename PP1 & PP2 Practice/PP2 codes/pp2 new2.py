data=["0101","0101"]
str1,str2=list(data[0]),list(data[1])
def checker(str1,str2):
    while len(str2)>0:
        if str2[0]=="0" and str1[0]=="0":
            str2.pop(0)
            str1.pop(0)
        elif str2[0]=="1" and str1[0]=="1":
            str2.pop(0)
            str1.pop(0)
        elif str2[0]=="1" and int(str1[0])+int(str1[1])==0:
            str2.pop(0)
            str1.pop(0)
            str1.pop(0)
        else:
            return "No"
        if len(str1)==0 and len(str1)>0:
            return "No"
    if len(str1) > 0:
        return "No"
    return "Yes"
print(checker(str1,str2))