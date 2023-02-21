givenNumber = 0;
while givenNumber < 1:
    givenNumber = int(input("Please enter the Number which is > 1\n"));

print("");

for number in range(1, givenNumber+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz");
    elif number % 3 == 0:
        print("Fizz");
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number);
