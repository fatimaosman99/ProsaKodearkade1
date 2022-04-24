import time
def nipnapper():
    print("***(*)*** Welcome to Paper Fortune Teller (Easter themed) ***(*)***")
    time.sleep(2)
    print("Choose habibi between Eggs, Rabbits or if you are so horrible Monster ugh")
    user_input = input()
    if user_input == "Eggs":
        print("Nice choice! I love eggs too. Now lemme flip this whirlybird ..::..::...:::...")
        time.sleep(3)
        print("So tell me eighth wonder: Pink or Blue or Red")
        time.sleep(2)
        print("Think carefully this is the last step before I reveal the fortune to you :D ")
        second_choice = input()
        if second_choice == "Pink":
            time.sleep(1)
            print("You are my Favorite Fantastic Human!")
        elif second_choice == "Blue":
            time.sleep(1)
            print("Am blue da be da ba daaaa")
        elif second_choice == "Red":
            time.sleep(1)
            print("AGLET, Tie the world together!")
        else:
            print("Invalid input, habibi.")
    elif user_input == "Rabbits":
        print("Now my friend, choose between Bugs Bunny, Easter Bunny or Hare")
        third_input = input() #can i reuse same variable
        if third_input == "Bugs Bunny":
            print("What's up Dawg?")
        elif third_input == "Easter Bunny":
            print("Happy Easter darling")
        elif third_input == "Hare":
            print("I swear am not a rabbit!")
        else:
            print("Invalid input, habibi")

    elif user_input == "Monster":
        print("O_____O")
        time.sleep(1)
        print("UnBeLiEvAbLe")
        time.sleep(1)
        print("One-eyed or Zombie or Mummy")
        fourth_input = input()
        if fourth_input == "One-eyed":
            print("You have Diamond eyes")
        elif fourth_input == "Zombie":
            print("You are both alive & dead")
        elif fourth_input == "Mummy":
            print("The pharoahs are after you!")
        else:
            print("Invalid input, habibi")



    else:
        print("What do you say? you have to choose sth!")
         
    
    return


nipnapper()