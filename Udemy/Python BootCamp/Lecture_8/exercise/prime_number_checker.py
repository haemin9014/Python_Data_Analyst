n = int(input("Check this number: "));

def prime_checker(number):
    numb = number-1;
    is_prime = True;
    if number <= 1:
        print("It's not a prime number");        
    while numb > 1:
        if number % numb == 0:
            print("It's not a prime number");
            is_prime = False;
            break;
        else:
            numb -= 1;
    if is_prime == True:
        print("It's a prime number")

prime_checker(number = n);