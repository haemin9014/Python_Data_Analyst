# len(4837) this will call error because len doesn't like to work with Integer
num_char = len(input("What is your name?\n"));
print(type(num_char));
#type conversion
covert_num_char = str(num_char)

score = 0;
height = 1.9;
isWinning = True

#to print out this use f-String
print(f"your score is {score} and your height is {height}, at last, you are winning is {isWinning}");


