a = list(range(6));
print(a);
b = tuple(range(6));
print(b);

def generateList(startvalue, endvalue):
    # Write your code here
    listRange = list(range(startvalue-1, endvalue+1));
    print(listRange[1:4]);
    print(listRange[-1:-6:-1]);
    print(listRange[1:len(listRange):4]);
    print(listRange[-1:0:-2]);