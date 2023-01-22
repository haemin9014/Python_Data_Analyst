def primegenerator(num, val):
    # Write your code here
    #making list for prime number
    primeNumber = [];
    primeNumber.append(2);
    for i in range(3, num):
        for j in range(2, i-1):
            if(i%j == 0):
                break;
        else:
            primeNumber.append(i);
                
    if val == 1:
        for element in range(0, len(primeNumber), 2):
            yield primeNumber[element];
    else:
        for element in range(1, len(primeNumber), 2):
            yield primeNumber[element];