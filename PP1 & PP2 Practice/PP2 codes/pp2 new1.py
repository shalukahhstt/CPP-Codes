def missingNumbers(arr,brr):
    n=0
    x=[]
    for i in arr:
        for j in range(n,len(brr)):
            if i == brr[j]:
                n = j + 1
                break
            else:
                x.append(brr[j])
    y=list(set(map(int,x)))
    y.sort()
    return y

f_name = input()
input_f = open(f_name,'r')
lines = input_f.readlines()
arr = lines[0].split()
brr = lines[1].split()

y = missingNumbers(arr,brr)
result = " ".join(list(map(str,y)))
out = open("output.txt",'w')
out.write(str(result)+'\n')
out.close()
input_f.close()


