word = input()
list1=list(word)
main=[]
dup = []
count= []
for i in list1:
    if i in main:
        dup.append(i)
    else:
        main.append(i)
        count.append(list1.count(i))
for i in range( len(main)):
    print(main[i]," - ",count[i])