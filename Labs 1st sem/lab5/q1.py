#Make a lists for numbers in float type
num_list1=[]

#input 10 numbers
num_list2 = input().split()

#input numbers to the list as float
for j in num_list2:
    num_list1.append(float(j))

#check whether the number has a decimal point or not
for i in range(0,len(num_list2)):
    if str(num_list1[i]) != num_list2[i] :
        num_list1[i] = int(num_list1[i])

#output maximum and minimum numbers
print("Minimum = ",min(num_list1))
print("Maximum = ",max(num_list1))

