number = input().split(',')
list1 = []
for i in number:
    list1.append(int(i+i[::-1]))
print(sum(list1))