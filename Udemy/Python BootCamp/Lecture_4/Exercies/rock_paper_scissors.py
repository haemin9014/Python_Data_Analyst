import random;
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
user_choice = int(input("What do you chose? Type 0 for Rock,  1 for Paper, 2 for scissors"));

gamelist = [rock, paper, scissors];

computer_choice = random.randint(0,2);

print(f"user choice is {gamelist[user_choice]}");
print(f"computer choice is {gamelist[computer_choice]}");

if user_choice == 1 and computer_choice == 3:
    print("User win!")
elif user_choice == 2 and computer_choice == 1:
    print("User win!")
elif user_choice == 3 and computer_choice == 2:
    print("user win!")
elif user_choice == computer_choice:
    print("tie!")
else:
    print("user loose!");