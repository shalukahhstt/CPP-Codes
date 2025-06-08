S= "aaabbbsssvvvdddbbbfffbbbgggjjjmmm"
N= 3
X=len(S)//N+1
for i in range(X*N-len(S)):
    S+="*"
Matrix=[["*" for i in range(X)] for j in range(N)]

count=0
for i in range(X):
    for j in range(N):
        Matrix[j][i]=S[count]
        count+=1
for i in Matrix:
    print("".join(i),end="")