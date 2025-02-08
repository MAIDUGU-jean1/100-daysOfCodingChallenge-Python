
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

choice1 = input('you\'re at a crossroad, where do you want to go? type "left" or "right". \n').lower()
if choice1 == "left" :
    choice2 = input('you\ve come to a lake. There is an island in the middle of the lake.type "Wait" to wait for a boat. Type "Swim" to Swim across \n').lower()
    if choice2 == "wait": 
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one Yellow and one blue. which colour do you choose? \n').lower()
        if choice3 == "red" or choice3 == "blue" :
                print("It's a room full of Fire. Game Over")
        elif choice3 == "yellow":
             print("You win You found the Treasure")
        else:
             print("You choose a Door that doesn't exist Game Over. ")

    else :
        print("You got attacked by an angry trout. Game Over")
else:
    print("You fell into the hole GameOver")