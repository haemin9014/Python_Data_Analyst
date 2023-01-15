a = ["banana", "apple", "microsoft"];
for i in a:
    print(i);

b= [20, 10, 5]

total = 0;
for i in b:
    total += i;

print("Total will be %s" %total);
rangeNumber = list(range(1,5));

print(rangeNumber);

for i in range(1,5):
    print("Setting for loop using range i will be %s" %i);

sumOfMod = 0;

for i in range(1, 8):
    if i%3 :
        sumOfMod += i

print("sum of mod %s" %sumOfMod);

def sumOfNFibonacciNumbers(n):
    # Write your code here
    start = 0;
    afterStart = 1;
    result = 1;
    if n  != 0 and n != 1:
        for i in range (2, n):
            sumOf = start + afterStart;
            result += sumOf;
            start = afterStart;
            afterStart = sumOf
        return result;
    return 0