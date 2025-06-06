#This Program calculate Total & Average of 4 Subjects Of A Student
tot=0
avg=0
marks=0
i=0
name=(input("Name Of The Student :"))
while i<=3:
    marks=int(input('Input Marks : '))
    tot=tot+marks
    i=i+1
print("\nTotal Marks Of ",name," is ",tot,"\n")
avg=tot/4
print("Average is ",avg)
input("\n Press Enter To Exit")
