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

    
def locations(): # holding list discriptions and lacation valiables signed to indexes, return locations and descriptions
    descriptions = [
        ("                CENTRAL PARK\n"
         "You are walking at in the infamous New Yorker park: Central Park. It is very dark, there is barely any lights."
         "The trees are very tall, the grass seems wet as if it has been raining the whole day."
         "The park has a strange smell, dogs and wild animals are staring at you from behing the three. Weird noise are being louder and louder."
         "Watch out! This is not very safe in this place. You probably should left this place ASAP ... ")
        , ("           PRISON: RIKERS ISLAND\n"
           "Ohohohoh !!! You just landed at the worst location in NYC ever: Rikers Island, the home to New York City's main prison complex. "
           "You are now with the most dangerous felons and individuals located in New York state."
           "You have no means of communication, no way to escape apart from the ferry who is about to leave this nighmare island in a few minutes."
           "Jump on the Ferry quickly or your life is ended soon.")
        , ("              BAR\n"
           "You arrived just arrived at a bar called Miss Lilys. there are people waiting in line to enter the bar."
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
            "trying to find a way out. It's night time, hence, there aren't much people to hear to find an 'EXIT' door. You have to figure it out on "
            "your own. Read the signs and instructions carefully but you must hurry up because some shadows has been following you since you arrived at the airport. "
            "Don't forget your objective is to arrive to your hotel safe and sound. Don't waste too much time here because, as of right now, you have "
            "a long journey ahead of you. Good luck. I hope you will find a way out of this gigantic airport. ")
        ]
    park = 0
    prison = 1
    bar = 2
    island = 3
    museum = 4
    memorial = 5
    hotel = 6
    airport = 7
    
    
    return descriptions, park, prison, bar, island, museum, memorial, hotel, airport

def conclude(score, name): # show copyright and show scores
    end = "\nCongratulations! You made it to your hotel. \nNow you can rest and tell your family and friends about your magic nights in NYC! "
    copyRight =  "Copyright (C) 2020 Jordan Jolo"
    print(end+"\n")
    print('Well done, '+name+'! You have finished the game. \n')
    print("Your final score is:" , score,"\n")
    print(copyRight)

def location_scorefunc(current_location, score, descriptions):
        score +=10 # add 10 on the score 
        print(descriptions[current_location]) # print the description of the current location
        return score 


def gameloop(name):

    descriptions, park, prison, bar, island, museum, memorial, hotel, airport = locations()
    askforhelp = "You can only move 'north', 'east', 'west' or 'south' from your current location. \nPlease enter either of these four options. "
    current_location = airport
    location_visited = [current_location]
    print(descriptions[7])
    score = 0
    while True :
        print("\n")
        print(name, ", your current score is:", score, "\n" )
        direction = input("Enter type which location you would like to go (north, south, east or west) or ask for 'help' or 'quit' : ").strip().lower()
        print("\n")
        if direction in ["north", "east", "south", "west"]:
            if current_location == airport:
                if direction == "south":
                    print("You are still at the same location, JFK airport, you must get out soon! \n")
                elif direction == "north":
                    print("Welcome to Ellis Island \n")
                    current_location = island
                elif direction == "east":
                    print("Oops, you just got yourself stuck in jail. \n")
                    current_location = prison
                elif direction == "west":
                    print("You are arrived in the museum! \n")
                    current_location = museum
                score = location_scorefunc(current_location, score, descriptions)
                    
            elif current_location == prison:
                if direction in ["east", "south"]:
                    print("You haven't move, you are still inside the prison. \nTime is running! Be Careful! \n")
                elif direction == "north":
                    print("Welcome to Central Park! \n")
                    current_location = park
                elif direction == "west":
                    print("Back to square one, you are in the airport. \n" )
                    current_location = airport
                score = location_scorefunc(current_location, score, descriptions)
                
            elif current_location == park:
                if direction == "east" :
                    print ("Still in central park! Sorry!\n")
                elif direction == "north":
                    print("You have arrived at a bar.\n")
                    current_location = bar
                elif direction == "west":
                    print("You are now at Ellis Island to see the statute of liberty.\n")
                    current_location = island
                elif direction == "south":
                    print("Back to Prison")
                    current_location = prison
                score = location_scorefunc(current_location, score, descriptions)
                 
            elif current_location == island:
                if direction == "north":
                    print("you are still on the island. \n")
                elif direction == "east":
                    print("Central Park is a beautiful place to chill, right? \n")
                    current_location = park
                elif direction == "south":
                    print("you are back at the airport. Hurry up !\n")
                    current_location = airport
                elif direction == "west":
                    print("Welcome to the 9/11 memorial. \nLet's take a moment of silence for those lifes that died on that tragic day. \n")
                    current_location = memorial
                score = location_scorefunc(current_location, score, descriptions)
                
            elif current_location == museum:
                if direction in ["west", "south"]:
                    print("You haven't move. I see that you like this musem a lot! \nTime is running! Be Careful! \n")
                elif direction == "north":
                    print("You just arrived to the 9/11 memorial. \n")
                    current_location = memorial
                elif direction == "east":
                    print("You are back to the airport. Hurry to get to the hotel. \n" )
                    current_location = airport
                score = location_scorefunc(current_location, score, descriptions)
                
            elif current_location == bar:
                if direction in ["north", "east"]:
                    print ("You are having a lot of fun at the bar. You haven't left yet! \n")
                elif direction in "south":
                    print("You are back to Central Park. \n")
                    current_location = park
                elif direction == "west":
                    current_location = hotel
                score = location_scorefunc(current_location, score, descriptions)
                    
            elif current_location == memorial:
                if direction == "west":
                    print("You are still at the memorial! \n")
                elif direction == "east":
                    print("You are now looking at the statute of liberty.\n")
                    current_location = island
                elif direction == "south":
                    print("Back at the MET Museum! \n")
                    current_location = museum
                elif direction == "north":
                    current_location = hotel
                score = location_scorefunc(current_location, score, descriptions)
                    
            if current_location == hotel:
                break
            
        elif direction == "help":
            print(askforhelp)
            
        elif direction == "quit":
            print("You have exited the game. \n")
            print("Your final score is ", score)
            return
        else:
            print ("Invalid input has been entered. \n")
    conclude(score, name)
        
def main():
    name, trait = UserInputInfo()
    introduction(name, trait)
    gameloop(name)


main()      
                    
                    
                    

        
    

