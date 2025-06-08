f_name = input()
input_f = open(f_name,'r')
line_list = input_f.readlines()

def calc(k,d,n):
    for i in range(len(d)):
        x=1
        while x!=0:
            if k%d[i]==0:
                k=(k/d[i])*n[i]
            else:
                x=0
    for j in range(len(d)):
        if k % d[j] == 0:
            k=calc(k,d,n)
        else:
            continue
    return int(k)
output_f=open("output.txt",'w')
for i in line_list:
    n = []
    d = []
    integer = int(i.split('|')[0])
    fraction_list = i.split('|')[1].split(',')
    for i in fraction_list:
        n.append(int(i.strip().split('/')[0]))
        d.append(int(i.strip().split('/')[1]))
    result=calc(integer,d,n)
    output_f.write(str(result)+'\n')
