name = input()
f_input = open(name,'r')
line = f_input.readlines()
capt = line[0].split()
output=open("output.txt",'w')
for i in range(1,len(line)):
    data = line[i].split()
    score=0
    for j in range(1,len(data)):
        if str(capt[j]) == 'Dots':
            pass
        elif str(capt[j]) == 'Ones':
            score=score+int(data[j])*1
        elif str(capt[j]) == 'Twos':
            score=score+int(data[j])*2
        elif str(capt[j]) == 'Threes':
            score=score+int(data[j])*3
        elif str(capt[j]) == 'Fours':
            score=score+int(data[j])*4
        elif str(capt[j]) == 'Sixes':
            score=score+int(data[j])*6
    result=data[0]+" "+str(score)
    output.write(result+'\n')
output.close()
f_input.close()

