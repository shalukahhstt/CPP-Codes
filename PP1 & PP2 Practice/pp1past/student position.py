student_list = input().split()
card_list = input().split()
student_list2 = list(student_list)
id=''
for i in range(len(card_list)):
    id = int(student_list.index(student_list[i]))

    card=card_list[i]
    if card[0]== 'L':
        element=student_list[i]
        position = int(card[1]) + int(student_list2.index(element))

        student_list2.remove(element)
        student_list2.insert(position,element)

    elif card[0] == 'R':
        element = student_list[i]
        position = int(student_list2.index(element))-int(card[1])

        student_list2.remove(element)
        student_list2.insert(position, element)

for i in range(len(student_list2)):
    element2 = student_list[i]
    place = int(student_list2.index(element2))+1
    print(place,end=" ")
