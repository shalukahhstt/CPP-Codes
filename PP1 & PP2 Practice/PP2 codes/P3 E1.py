f_name = input()
input_f = open(f_name,'r')
line_list = input_f.readlines()
def find_f(i,f,m):
    if int(i) in f:
        return f[int(i)]
    else:
        f[int(i)] = int(i)-find_m(find_f(int(i)-1,f,m),f,m)
        return f[int(i)]
def find_m(i,f,m):
    if int(i) in m:
        return m[int(i)]
    else:
        m[int(i)] = int(i)-find_f(find_m(int(i)-1,f,m),f,m)
        return m[int(i)]

f = {0:1}
m = {0:0}
output_f = open("output.txt",'w')
for i in line_list:
    output_f.write(str(int(i))+": F="+str(find_f(i,f,m))+" M="+str(find_m(i,f,m))+'\n')
    #print(str(int(i))+": F="+str(find_f(i,f,m))+" M="+str(find_m(i,f,m)))