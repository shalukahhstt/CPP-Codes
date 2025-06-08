#Input the sports we love into a list
sport_list=input().split()
#Input subjects and verbs in a list
subject = ["I", "We"]
verb = ["play", "watch"]
#Start the loop for subject
for i in range(0,len(subject)):
    #start the loop for verb
    for j in range(0,len(verb)):
        #start the loop for sports
        for k in range(0, len(sport_list)):
            #output the sentence
            print(subject[i]+" "+verb[j]+" "+sport_list[k]+".")
