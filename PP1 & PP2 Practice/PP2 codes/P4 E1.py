def swap(index1,index2,listx):
    listx[index1],listx[index2] = listx[index2],listx[index1]

def find_index(list1,y_list,x_list,x,y):
    for j in range(len(list1)):
        if int(list1[j])==x:
            x_list.append(j)
        elif int(list1[j])==y:
            y_list.append(j)

f_name=input()
input_f =open(f_name,'r')
line_list = input_f.readlines()
output_f=open("output.txt",'w')
for i in line_list:
    data = i.split()
    list1 = data[0][1:len(data[0])-1].split(',')
    x = int(data[1])
    y = int(data[2])
    x_list=[]
    y_list = []
    find_index(list1, y_list, x_list, x, y)
    for k in range(len(x_list)):
        swap(int(x_list[k])+1,int(y_list[k]),list1)
    output_f.write(str(list(map(int,list1)))+'\n')
    print(list1)
