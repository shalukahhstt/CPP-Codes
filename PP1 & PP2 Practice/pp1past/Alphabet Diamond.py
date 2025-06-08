letter = ord(input())
if letter>95:
    end=letter-32
else:
    end=letter
for i in range(65,end+1):
    print(" "*(end-i),end="")
    for j in range(65,i+1):
        print(chr(j),end="")
    for j in range(i-1,64,-1):
        print(chr(j),end="")
    print("")
for i in range(end-1,64,-1):
    print(" "*(end-i),end="")
    for j in range(65,i+1):
        print(chr(j),end="")
    for j in range(i-1,64,-1):
        print(chr(j),end="")
    print("")