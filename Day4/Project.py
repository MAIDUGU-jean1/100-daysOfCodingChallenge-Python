import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [ rock , paper , scissors]

#Write your code below this line 👇

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors. "))
print(game_images[my_choice])
computer_choice = random.randint(0,2)
if my_choice >= 3 or computer_choice < 0:
    print("invalid")
else:

    print(" Computer chooses:")
    print(game_images[computer_choice])


    if my_choice == 2 and computer_choice == 0:
        print(" you loose ")

    elif my_choice == 0 and computer_choice == 2:
        print(" you win ")
    elif computer_choice > my_choice:
        print(" You loss ")
    elif my_choice > computer_choice:
        print(" You win ")
    elif computer_choice == my_choice :
        print(" Its a draw ")
