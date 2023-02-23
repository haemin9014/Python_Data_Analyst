import random;
import os;
wordlist = ["aardvark", "baboon", "camel"];
chosenword = wordlist[random.randint(0, len(wordlist)-1)].lower();
blank = [];
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
life = len(stages)-1;
#create _
for fill in range(0, len(chosenword)):
    blank.append("_");

while life >= 0:
    count = 0;
    check = 0;
    user_pick = "";
    print(blank)
    if life == 0:
        print("Game Over!");
        print(f"Answer was {chosenword}");
        print(f"{stages[life]}");
        break;

    print(f"{stages[life]}");
    while(len(user_pick) != 1):
        user_pick = input("Guess a letter: ").lower();
        os.system("clear");

    for vocab in chosenword:
        if vocab == user_pick:
            blank[count] = vocab;
            check += 1;
        count += 1;
    
    if blank.__contains__("_") == False:
        print("you win the game!")
        break;
    if check == 0:
        life -= 1;





