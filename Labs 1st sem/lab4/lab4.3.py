name=input("Enter message: ")
base=int(input("Enter base: "))
x=0
lname=int(len(name))
out=""
t=""
r_out=""
m=""
while x<lname:
    asci=int(ord(name[x]))
    #print(asci)
    r=asci
    out=""
    r_out = ""
    while r>0:
        remain=r%base
        r=r//base
        out=out+str(remain)
        #print(r)
        #print(out)
    for a in range(len(out)-1,-1,-1):
        r_out+=out[a]
        #print(r_out)
    m=m+r_out

    x=x+1
print(m)

