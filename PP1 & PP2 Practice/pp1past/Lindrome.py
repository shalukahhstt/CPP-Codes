x=0
while x==0:
    word = input()
    if word=='0':
        x=1
        break
    else:
        if len(word)==1:
            print("NO")
        else:
            if len(word)%2==0:
                lhs=word[0:int(len(word)/2)]
                rhs=word[int(len(word)/2):int(len(word))]
            else:
                lhs = word[0:int(len(word) / 2)]
                rhs = word[int(len(word) / 2)+1:int(len(word))]
            if lhs==rhs or lhs==rhs[::-1]:
                print("YES")
            else:
                print("NO")