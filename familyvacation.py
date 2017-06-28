start = '''
Your family has been stressed out these past few months and you are stressed out with them. You decide to take a vacation with your family.
To start your vacation, you must choose a destination.
'''
#EndGame
endgame = "Game Over."
print(start)


print("Type 'forest', 'beach', or 'town'.")
user_input = input()
#Forest
if user_input == "forest":
    print("You chose to hike through a forest with your family.")
    print("You come across a lake, but you also see a mountain in the distance.")
    answer2 = input("Type 'lake' or 'mountain' to continue.")
    #Lake
    if answer2 == "lake":
        print("Your family wants to swim deeper into the lake. Do you stay on the shoreline or venture deeper?")
        answer3 = input("Type'shoreline' or 'venture deeper' to continue.")
        #Shoreline
        if answer3 == "shoreline":
            print("Mermaids emerge from the lake and greet you on the shoreline.")
            print("It's getting late. The mermaids invited you to stay after dark. What will you do?")
            answer4 = input("Type 'stay after dark' or 'leave now'.")
                #stay after dark
            if answer4 == "stay after dark":
                print("Your family turn into fish and flop about on the shoreline.")
                print("You die gasping for oxygen. Nice.")
                print(endgame)
                #leave now
            elif answer4 == "leave now":
                print("The mermaids cast a spell on you as you leave.")
                print("As you drive home, your family crashes into a car on the other lane.")
                print(endgame)
        #Venture Deeper
        elif answer3 == "venture deeper":
            print("Your family ventures deeper into the lake and sees a shadowy figure emerging from beneath you.")
            print("It's Nessy! The Loch Ness Monster!")
            print("In reflex, you splash water at Nessy hoping it would distract Nessy long enough for your family to escape.")
            print("Your attempts at distraction angered Nessy and in response, it whiplashed its tail and your family flies through the air and hits a tree.")
            print(endgame)
    #Mountain
    elif answer2 == "mountain":
        print("You decide to walk towards the mountain, catching the scenery on the way there.")
        print("Along the way, you discover a mystical cave. Would you like to venture into the cave?")
        answer5 = input("Type 'yes' or 'no'.")
        #go_into_cave
        if answer5 == "yes":
            print("You encounter trolls dancing around the fire. On closer inspection, you realize there is a human boy turning on a spit.")
            print("Do you save the boy or trade places with him?")
            answer6 = input("Type 'save the boy' or 'trade places'.")
            #savethe_boy
            if answer6 == "save the boy":
                answer7 = input("Type 'negotiate' or 'fight'.")
                #negotiate_trolls
                if answer7 == "negotiate":
                    print("You call attention to yourself but the trolls don't understand you.")
                    print("The only option is to fight the trolls. You end up losing the fight.")
                    print(endgame)
                #Fight_trolls
                elif answer7 == "fight":
                    print("You fought well, but it just wasn't enough. You have severe battle wounds and you end up bleeding out.")
                    print(endgame)
            elif answer6 == "trade places":
                print(endgame)
        if answer5 == "no":
            print("You decide to continue walking to the top of the mountain, catching sight of a majestic bird.")
            print("Observing the bird from afar, you approach the animal and discover its a phoenix.")
            print("Your children would like to keep the bird as a pet. You decide to volunter to capture the phoenix and during your attempt you burn to death.")
            print(endgame)

#Beach
elif user_input == "beach":
    print("You chose to drive to the prettiest beach.")
    print("Once you arrive, your children are arguing how to spend the day. One would like to build a sand castle, while the other would like to go swimming.")
    answer8 = input("Type 'build sandcastle' or 'swim'.")
    #sandcastle
    if answer8 == "build sandcastle":
        print("As you begin to build your sandcastle, you see a red shiny red shell sifting below the sand. You discover it is a GIANT crab.")
        answer9 = input("Type 'eat the crab' or 'observe'.")
        #eat_the_crab
        if answer9 == "eat the crab":
            print("After cooking and eating up your delicious crab, you don't feel so well. Eventually you find out that you and your family have food poisoning.")
            print(endgame)
        elif answer9 == "observe":
            print("The GIANT crab has no concerns for your beautiful sand castle and destroys your creation.")
            print("Your children are very upset and cry all the way home.")
            print(endgame)
    elif answer8 == "swim":
        print("Your children have always been competitive. When you arrive to the beach, your children spot a buoy far off in the ocean.")
        print("The children decide to see who can reach the buoy first.")
        print("Would you be a neglectful parent and let them swim out by themselves? Or will you be an irresponsible adult and join them?")
        answer10 = input("Type 'neglect' or 'join'.")
            if answer10 == "neglect":
                print("As your children swim out to sea, they get swept up by pelicans and you never see them again.")
                print("Your children then grow-up to be fledgling pelicans.")
                print(endgame)
            elif answer10 == "join":
                print("Due to your physical physique, you get to the buoy before your kids.")
                print("they get bery angry, claiming that you cheated. They pile on top of you, not realizing your drowning.")
                print(endgame)

#Town
elif user_input == "town":
    print("You chose to drive to town in the next state over.")
    print("After driving for 5 hours straight, you eventually arrive at the town. The town doesn't have much to offer, but you ask the locals about the most attractive spots in town.")
    print("They suggest several locations and your family is interested in visiting the bowling alley and the ice cream parlor.")
    print("Due to having a long drive back home, you could only chose one.")
    answer11 = input("Type 'bowling alley' or 'ice cream'.")
        if answer11
