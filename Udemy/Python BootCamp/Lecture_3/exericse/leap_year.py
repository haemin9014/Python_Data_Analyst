year = int(input("Which year do you want to check"));
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("it is a leap");
        else:
            print("it is not a leap");
    else:
        print("it is a leap");
else:
    print("it is not a leap");