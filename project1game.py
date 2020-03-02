#By Jordan Jolo
# Feb 10 2020
#This is a text based adventure game titled "A dreamy night out in New York City
#I have worked alone

def visitLocale(locale, score, prompt):
    print(locale)
    print("Score:", score)
    print()
    input(prompt)
    print()

def main():
    title = "Welcome to the Best Nightout between Friends! Be ready to party and have fun! \n\nLet's start ... \n"
    print(title)

    name_prompt = "Please enter your name: "
    name = input(name_prompt)
    age_prompt = "Please enter your age: "
    age = input(age_prompt)
    loveinterest_prompt = "Please enter your love interest name: "
    loveinterest = input(loveinterest_prompt)
    prompt = "Press Enter to continue..."


    welcome_user = "Nice to meet you"+ name +"! You are"+ age+" which means that you can start playing."
    print(welcome_user)

    introduction = "Hi "+ name+", the aim of this game is for you to score as many points as possible in order to get "+ loveinterest +" to go back with you! "\
                   "You have arrived in New York City to party all night long at your favorite bar. " \
                   "For everything decision and direction you take, you now score a total of 50 points."

    locale1 = "You have arrived at the bar and are now waiting in line. Guess, Who is also here? : "+ loveinterest +" ! "\
              'You decide to go up to her and say "Hi!". Because of your bold initiative, '\
              "you now scored 50 points. \nIt's quite cold outside, let's now get inside the bar!"
    
    
    locale2 = "It's Mardi Gras and you see that there is an exclusive offer : BUY 5 SHOTS, GET 5 FOR FREE. \n"\
              "You therefore decide to grab two of your friends and "+ loveinterest+" to get the exclusive offer. "\
              "Smart choice! Well done! That was a very smart move! "\
              "Everyone is happy after these 10 shots. You now earns 50 more points for this next move."
    
    locale3 = '"Yeah, Im gonna take my horse to the old town road" \n"Im gonna ride til I cant no more" \n"Im gonna take my horse to the old town road"\n'\
              "Your favorite song is now playing on the dancefloor on the side of the part. You decide to go dance there and you bring "+ loveinterest+" "\
              "with you. Very clever "+ name+"!!! You just scored an extra 50 points for your enthousiasm."
    
    locale4 = "Everyone is happy and dancing all together. You guys are having a great night. "\
              "When the night is over, you all decide to go to the nearest diner to have some milkshares to end the night perfectly. "\
              "It's your two bestfriends you came with, "+ loveinterest +"'s bestfriends and obviously you and " + loveinterest +". \n"\
              "50 ADDITIONAL POINTS HAVE BEEN ADDED TO YOUR TOTAL SCORE." 


    score = 0


    print() # Prints a blank line
    visitLocale(introduction, score, prompt)
    score = score + 50

    visitLocale(locale1, score, prompt)
    score = score + 50

    visitLocale(locale2, score, prompt)
    score = score + 50

    visitLocale(locale3, score, prompt)
    score = score + 50

    visitLocale(locale4, score, prompt)
    score = score + 50

    win = "Congratulations "+ name+"!\nYou have officially won the game!\n\n"+ name+" + "+ loveinterest +" = LOVE \n\n :-)"
    print(win)

    copyright = "Copyright (C) 2020 Jordan Jolo"
    print(copyright)

main()
