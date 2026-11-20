import random  
print("welcome to rock paper scissors game")
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
user_choice = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("invalid choice")


random_choice = random.randint(0, 2)
if random_choice == 0:
    print(rock)
elif random_choice == 1:
    print(paper)
else:
    print(scissors)
if user_choice == random_choice:
    print("draw")
elif (user_choice == 0 and random_choice == 2)or\
     (user_choice == 2 and random_choice == 1)or\
     (user_choice == 1 and random_choice == 0):
    print("you win")  
else:
    print("you lose")



