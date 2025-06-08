f_name = input()
input_f = open(f_name,'r')
line = input_f.readlines()
matrix=[]
matrix2=[]
dimension = int(line[0].split()[1])
word = line[0].split()[0]
row = []
for i in range(len(word)):
    row.append(word[i])
    if len(row)==dimension:
        matrix.append(row)
        row=[]
transpose2 = list(zip(*matrix))
transpose2 = [list(row) for row in transpose2]
matrix.append(row)
transpose1 = list(zip(*matrix))
transpose1 = [list(row) for row in transpose1]
r1=""
r2=""
for i in transpose1:
    r1=r1+"".join(i)
if len(transpose1)==0:
    for j in range(len(transpose1),len(transpose2)):
        r2=r2+"".join(transpose2[j])

else:
    for j in range(len(transpose1),len(transpose2)):
        r2=r2+"".join(transpose2[j])
        r2=r2+"*"
result=r1+r2
print(result[0:len(result)-1])

