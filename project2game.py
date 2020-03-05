#Project 2
#Author : Jordan Jolo
#March 2 2020

def UserInputInfo():# get user input and return name and characteristic trait
    name = input("Enter your name: ")
    trait = input ("Enter an adjective that describes you the most: ")
    return name, trait

def introduction(name, trait): # showing introduction of the game, title and backstory
    title = (        "\n              Magic Night At New York City ?\n"
                     "      ======================================================\n")
    IntroStory = ("You mysteriously wake up from a bad dream and you found yourself in "
             "in the middle of New York City's airport : JFK. However, this is not the same NYC you know."
             "The city has entirely changed, the areas, district, places are located differently - 'MAGIC' ? probably !!!"
             "This is your first time in this 'new' NYC. You do not have any means of communication, you are all on your own, "
             "and the city is full of adventurous, amazing and surpising things to discover along the night. "
             "This city can also be very dangerous, your job is to get to your hotel "
             "safe and sound. Having said that, let's start playing! As a quick reminder, "
             "your current location is JFK Airport......." )
    print(title+"\n")
    print('\n') 
    print("Welcome to the 'Magic Night at NYC' game, "+name+" the "+ trait +"!!! \n\n")
    print(IntroStory+"\n")
    input("Press Enter to continue")
    print('\n')

    
def locations(): # function with the list of the description of different location 
    descriptions = [
        ("                CENTRAL PARK\n"
         "You are walking at in the infamous New Yorker park: Central Park. It is very dark, there is barely any lights."
         "The trees are very tall, the grass seems wet as if it has been raining the whole day."
         "The park has a strange smell, dogs and wild animals are staring at you from behing the three. Weird noise are being louder and louder."
         "Watch out! This is not very safe in this place. You probably should left this place ASAP ... ")
        , ("           PRISON: RIKERS ISLAND\n"
           "Ohohohoh !!! You just landed at the worst location in NYC ever: Rikers Island, the home to New York City's main prison complex. "
           "You are now with the most dangerous felons and individuals located in New York state."
           "You have no means of communication, no way to escape apart from the ferry who is about to leave this nighmare island in a few minutes. "
           "Jump on the Ferry quickly or your life is ended soon.")
        , ("              BAR\n"
           "You arrived just arrived at a bar called Miss Lily's. there are people waiting in line to enter the bar."
           "The music is very nice. The entrance to the bar is free for new foreign. That's perfect for you, especially since you don't have "
           "your wallet with you. You can either decide to stay and have fun for a bit but you may still endanger "
           "your life, OR you just continue to explore the different areas of NYC untill you find your hotel. ")
        ,  ("             ELLIS ISLAND : THE STATUTE OF LIBERTY \n"
           "You are now facing the beautful and magnificent Statute of Liberty at Ellis Island. You are very happy. This is "
           "your first time looking at the statue with your own eyes. You are now very hopefful that you will get home safe "
           "as you look into her eyes, you see a symbol of freedom, victory and hope."
           "Attention to you !! Don't let the statute distract you from your mission : to get home safe. Ellis Island "
           "is a very inspiring place but you must stay focus. You choose what you want to de next. ")
        ,  ("             MUSEUM\n"
           "Welcome to one of the most beautiful and famous museum in the world: the Metropolitan Museum of Art of New York City, "
           "also called the MET. This amazing museum is an house of the most beautiful piece of artworks And crafts. You can hear a stranger voice telling: "
           "This art piece are magical in their own way, you can feel their presence nearby you, you can enjoy the colors and forms and figures. "
           "You are feeling inspired! You now thinking that you should have been an artist so you can tell your own stories through paintings or "
           "photographs, architectures or crafting. While you are feeling empowered and inspire, you continue to explore the gigantic museum. "
           "You are now so inspired after staring at all these art pieces that you are now very motivated to continue to explore more about the city and "
           "find your hotel. ")
        , ("               MEMORIAL\n" 
           "You are standing in front of the biggest memorial of the word : the 9/11 memorial (Ground Zero). You can feel the sad stories, the "
           "memories of this tragic event of 9/11. You don't want to leave, instead you want to commemorate the lives of those who died on this tragic day ."
           "this place is haunting your soul, your deepest thoughts and your worst nighmare. You want to come back to your family and friends "
           "to tell them how much you value, cherish and love them so much. You now make a mission to come back to your hotel so you can call them and "
           "join them once again. You are very emotional and cannot think clearly. Stay on your guard, something or someone has been following you "
           "this entire time. You must leave now and continue your journey in the streets of New York. ")
        , ( "                HOTEL\n"
            "This skyscraper is one of the tallest in town. From outside, you can see the front door, you are now arrived to the Roosevelt Hotel. "
            "You are running as you can hear weird noises following you along the way. You entered the enters and give your booking information "
            "to the front desk. While you're waiting to get your room, your explore the hotel. You can see from this enormous window glasses the dark, "
            "yet amazing streets of new york city. You also go to the top and discover this humongous rooftop bar with this outstanding swimming pool. ")
        , ( "                JOHN F. KENNEDY AIRPORT\n"
            "You have just arrived at the busiest international airport in North America: JFK Airport. This airport is very big, it is easy to get lost while "
            "trying to find a way out. It's night time, hence, there aren't much people to help you find the nearest 'EXIT' door. You have to figure it out on "
            "your own! Read the signs and instructions carefully but you must hurry up because some shadows have been following you since you've arrived at the airport. "
            "Don't forget your objective is to arrive to your hotel safe and sound. Don't waste too much time here because, as of right now, you have "
            "a long journey ahead of you. Good luck, mate! I hope you will find a way out of this gigantic airport. ")
        ]
    # indexing locations 
    park = 0
    prison = 1
    bar = 2
    island = 3
    museum = 4
    memorial = 5
    hotel = 6
    airport = 7
    
    
    return descriptions, park, prison, bar, island, museum, memorial, hotel, airport # return locations and descriptions

def conclude(score, name): # show copyright and show scores
    end = "\nCongratulations! You made it to your hotel. \nNow you can rest and tell your family and friends about your magic nights in NYC! "
    copyRight =  "Copyright (C) 2020 Jordan Jolo"
    print(end+"\n")
    print('Well done, '+name+'! You have finished the game. \n')
    print("Your final score is:" , score,"\n")
    print(copyRight)

def location_scorefunc(current_location, score, descriptions, name): # function that will calculated the score and print the current location description
    print(descriptions[current_location]) # print the description of the current location
    print()
    score += 10
    print(name, ", your current score is:", score, "\n" )
    return score

def visitIsland(current_location, island, score, descriptions, name):
    print("Welcome to Ellis Island \n")
    current_location = island
    score = location_scorefunc(current_location, score, descriptions, name)
    return score, current_location

def visitPrison(current_location, prison, score, descriptions, name):
    print("Sad,", name, "you are in prison now !\n")
    current_location = prison
    score = location_scorefunc(current_location, score, descriptions, name)
    return score, current_location

def visitMuseum(current_location, museum, score, descriptions, name):
    print("Welcome to the MET Museum. \n")
    current_location = museum
    score = location_scorefunc(current_location, score, descriptions, name)
    return score, current_location

def visitCentralPark(current_location, park, score, descriptions, name):
    print("Welcome to Central Park! \n")
    current_location = park
    score = location_scorefunc(current_location, score, descriptions, name)
    return score, current_location

def visitMemorial(current_location, memorial, score, descriptions, name):
    print("You have now arrived at the 9/11 memorial! \n")
    current_location = memorial
    score = location_scorefunc(current_location, score, descriptions, name)
    return score

def visitHotel(current_location, hotel, score, descriptions, name):
    print("You made it to the Hotel on time! \n")
    current_location = hotel
    score = location_scorefunc(current_location, score, descriptions, name)
    return score, current_location

def visitBar(current_location, bar, score, descriptions, name):
    print("Welcome to Miss Lily's Rooftop Bar! \n")
    current_location = bar
    score = location_scorefunc(current_location, score, descriptions, name)
    return score, current_location

def visitAirport(current_location, airport, score, descriptions, name):
    print("Back at your initial destination! \nSorry, you must start all over again! \nGood luck! \n")
    current_location = airport
    score = location_scorefunc(current_location, score, descriptions, name)
    return score, current_location


def gameloop(name): #this function is the game loop

    descriptions, park, prison, bar, island, museum, memorial, hotel, airport = locations()
    askforhelp = "You can only move 'north', 'east', 'west' or 'south' from your current location. \nPlease enter either of these four options. " # this is the help string
    no_new_move = "You have not moved! You still are at the same location! Be careful! \n" 

    current_location = airport
    print(descriptions[current_location]) #print the current initial location (the airport) before starting the loop
    score = 0  #score set up at 0
    
    while True :   #beginning of the game loop
        direction = input("\nEnter type which location you would like to go (north, south, east or west) or ask for 'help' or 'quit' : ").strip().lower()
        print("\n")
        if direction in ["north", "east", "south", "west"]:   
            if current_location == airport:  # location path if user is located at the airport
                if direction == "south":
                    print(no_new_move)
                elif direction == "north":
                    visitIsland(current_location, island, score, descriptions, name)
                elif direction == "east":
                    visitPrison(current_location, prison, score, descriptions, name)
                elif direction == "west":
                    visitMuseum(current_location, museum, score, descriptions, name)
                    
            elif current_location == prison: # location path if user is located at the prison
                if direction in ["east", "south"]:
                    print(no_new_move)
                elif direction == "north":
                    visitCentralPark(current_location, park, score, descriptions, name)
                elif direction == "west":
                    visitAirport(current_location, airport, score, descriptions, name)
                
                
            elif current_location == park: # location path if user is located at the park
                if direction == "east" :
                    print (no_new_move)
                elif direction == "north":
                    visitBar(current_location, bar, score, descriptions, name)
                elif direction == "west":
                    visitIsland(current_location, island, score, descriptions, name)
                elif direction == "south":
                    visitPrison(current_location, prison, score, descriptions, name)
                 
            elif current_location == island: # location path if user is located at ellis island
                if direction == "north":
                    print(no_new_move)
                elif direction == "east":
                    visitCentralPark(current_location, park, score, descriptions, name)
                elif direction == "south":
                    visitAirport(current_location, airport, score, descriptions, name)
                elif direction == "west":
                    visitMemorial(current_location, memorial, score, descriptions, name)
                
            elif current_location == museum:  # location path if user is located at the MET museum
                if direction in ["west", "south"]:
                    print(no_new_move)
                elif direction == "north":
                    visitMemorial(current_location, memorial, score, descriptions, name)
                elif direction == "east":
                    visitAirport(current_location, airport, score, descriptions, name)
                
            elif current_location == bar: # location path if user is located at the bar
                if direction in ["north", "east"]:
                    print (no_new_move)
                elif direction in "south":
                    visitCentralPark(current_location, park, score, descriptions, name)
                elif direction == "west":
                    visitHotel(current_location, hotel, score, descriptions, name)
                    
            elif current_location == memorial: # location path if user is located at the 9/11 memorial
                if direction == "west":
                    print(no_new_move)
                elif direction == "east":
                    visitIsland(current_location, island, score, descriptions, name)
                elif direction == "south":
                    visitMuseum(current_location, museum, score, descriptions, name)
                elif direction == "north":
                    visitHotel(current_location, hotel, score, descriptions, name)
                    
            if current_location == hotel: # location path if user is located at the museum then the loops ends sicne user arrived at final destination
                break
            
    
        elif direction == "help":   # print the 'help' statement if the user input 'help'
            print(askforhelp)
            
        elif direction == "quit":   # print the 'ending' statement if user unput 'quit'
            print("You have exited the game. \n")
            print("Your final score is ", score)
            return
        else:
            print ("Invalid input has been entered. \n") # if the user enter an invalid input other than 'quit','help','north','south','east',west'
    conclude(score, name) #calling the 'conclude' function to print the ending message and copyright statement
        
def main():     #main function
    name, trait = UserInputInfo()   #calling the userimputfunction to ask user for his information
    introduction(name, trait)       # callign the introduction
    gameloop(name)                  #running the loop


main()
