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

#Write your code below this line 👇
import random
choice = int(input("Choose 1 for scissor, 2 for rock, 3 for paper \n"))
if choice == 1:
  print(scissors)
elif choice == 2:
  print(rock)
else:
  print(paper) 
computer_choice = random.randint(1,3)
if computer_choice == 1:
  print(scissors)
elif computer_choice == 2:
  print(rock)
else:
  print(paper)
if choice == 1 and computer_choice == 1:
  print("It is a tie")
elif choice == 1 and computer_choice == 2:
  print("You loose")
elif choice == 1 and computer_choice == 3:
  print("You Win")
elif choice == 2 and computer_choice == 1:
  print("You win")
elif choice == 2 and computer_choice == 2:
  print("It is a tie")
elif choice == 2 and computer_choice == 3:
  print("You loose")
elif choice == 3 and computer_choice == 1:
  print("You loose")
elif choice == 3 and computer_choice == 2:
  print("You win")
else:
  print("It is a tie")