import random
print("Welcome to the stone paper scissors game")

stone = '''
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

image_list = [stone, paper, scissors]

#program for user to select stone paper scissors
user = int(input("Choose stone paper or scissors for stone 0, paper 1, and scissors 2:\n"))

if user >= 0 and user <= 2:
    print (image_list[user])


#program for computer to select stone paper scissors
computer = random.randint(0,2)
print("Computer chooses")
print (image_list[computer])

if user == 0 and computer == 1:
    print ("You lose")
elif user == 1 and computer == 0:
    print("You won")
elif user == 0 and computer == 2:
    print ("You won")
elif user == 2 and computer == 0:
    print ("You lose")
elif user == 1 and computer == 2:
    print("You lose")
elif user == 2 and computer == 1:
    print("You won")
elif user == computer:
    print("Game is Drawn")
else:
    print("Invalid input")
