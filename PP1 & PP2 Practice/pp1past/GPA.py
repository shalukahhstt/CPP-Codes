inputs = input().split()
n = inputs[0]
m = inputs[1]
weight = []
up = 0
down = 0
y = []
grades = input().split()
p = input().split()
if len(grades)!=int(n) or len(p)!=int(n):
    print("Wrong Number Of Subjects")
else:
    for i in range(int(m)):
        weight.append(input().split())
    for j in range(len(grades)):
        for k in weight:
            if k[0]==grades[j] :

                up = up + (float(k[1])*float(p[j]))
                down = down + float(p[j])

            else: continue

    GPA = round(up/down,2)
    print(GPA)
    for z in weight:
        if GPA > float(z[1]):
            x=GPA-float(z[1])
            y.append(x)

        else:
            x = float(z[1])-GPA
            y.append(x)

    g_index=int(y.index(min(y)))
    print(grades[g_index])
