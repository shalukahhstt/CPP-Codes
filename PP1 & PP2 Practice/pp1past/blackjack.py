card_dealer = input().split()
card_player = input().split()
dealer_sum = 0
player_sum = 0
d_count = 0
p_count = 0
for i in card_dealer:

    if i[1:] == '10' or i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
        dealer_sum = dealer_sum + 10
    elif i[1] == 'A':
        d_count = d_count + 1
    elif int(i[1]) < 10:
        dealer_sum = dealer_sum+int(i[1])

for i in card_player:

    if i[1:] == '10' or i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
        player_sum = player_sum + 10
    elif i[1] == 'A':
        p_count = p_count + 1
    elif int(i[1:]) < 10:
        player_sum = player_sum+int(i[1])

if p_count==2 or d_count > 1:
    print("Lose")
elif d_count==0:
    if p_count==0:
        if player_sum > dealer_sum:
            print("Won")
        elif player_sum == dealer_sum:
            print("Hit")
        else:
            print("Lost")
    elif p_count == 1:
        if player_sum+11==21:
            print("Won")
        elif player_sum+11>dealer_sum:
            print("Won")
        elif player_sum+11==dealer_sum or player_sum+1 == dealer_sum :
            print("Hit")
        else:
            print("Lose")
elif d_count==1:
    if dealer_sum+11==21:
        print("Lose")
    elif p_count==0:
        if dealer_sum+1<player_sum:
            print("Won")
        elif dealer_sum+1==player_sum:
            print("Hit")
        else:
            print("Lose")
    elif p_count==1:
        if dealer_sum==player_sum:
            print("Hit")
        elif dealer_sum < player_sum:
            print("Won")
        else:
            print("Lose")
