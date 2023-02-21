import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pwd = "";
pwd2 = [];
print("Welcome to the PyPassword Generator!");
letters_length = int(input("How many letters would you like in your password?"));
symobols_length = int(input("How many symbols would you like?"));
numbers_length = int(input("How many numbers would you like?"));

for i in range(0, letters_length+1):
    pwd += letters[random.randint(0, len(letters))-1];
    pwd2 += random.choice(letters);

for i in range(0, symobols_length+1):
    pwd += symbols[random.randint(0, len(symbols))-1];
    pwd2 += random.choice(symbols);

for i in range(0, numbers_length+1):
    pwd += numbers[random.randint(0, len(numbers))-1];
    pwd2 += random.choice(numbers);


pwd = ''.join(random.sample(pwd, len(pwd)));
print("first sample just using string for result")
print(pwd);
print("");
print("second samples using list")
random.shuffle(pwd2);
print(pwd2);
