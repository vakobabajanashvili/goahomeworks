import random as rm

rock = '''
    
---'   )
      ()
      ()
      ()
---.()
'''

paper = '''
    
---'   )
          )
          )
         )
---.)
'''

scissors = '''
    
---'   )
          )
       )
      ()
---.(___)
'''
game_images = [rock,paper,scissors]

x = 0
y = 1
z = 2

user_choice = int(input(f"What do you choose.Type {x} to choose rock,Type {y} for paper or type {z} for scissors.\n"))
print(game_images[user_choice])

computer_choice = rm.randint(0, 2)
print("Computer choice: ")
print(game_images[computer_choice])
if  user_choice == 0 and  computer_choice == 2:
    print("you win")
elif user_choice == 2 and  computer_choice == 1:
    print("you win")
elif user_choice == 1 and  computer_choice == 0:
    print("you win")
elif user_choice == 2 and  computer_choice == 0: 
    print("you lose")
    exit()
elif user_choice == 1 and  computer_choice == 2:
    print("you lose")
    exit()
elif user_choice == 0 and  computer_choice == 1:
    print("you lose")
    exit()
elif user_choice == 1 and  computer_choice == 1 or user_choice == 2 and  computer_choice == 2 or user_choice == 3 and  computer_choice == 3:
    print("Its a draw")