word=list(input().lower())
vowels='aeiou'
for i in word:
    if i in vowels:
        place=word.index(i)
        word.remove(i)
        word.insert(place,i.upper())

    else:continue

for j in word:
    print(j,end="")