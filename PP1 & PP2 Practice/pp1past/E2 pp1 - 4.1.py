word = input()
count = 1
chrlist = []
countlist = []
for i in range(1, len(word)):
    if word[i] == word[i - 1]:
        count = count + 1
    else:
        chrlist.append(word[i - 1])
        countlist.append(count)
        count = 1
chrlist.append(word[-1])
countlist.append(count)
for j in range(len(chrlist)):
    print(chrlist[j], " - ", countlist[j])
