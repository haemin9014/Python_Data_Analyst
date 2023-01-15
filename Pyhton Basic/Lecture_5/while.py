sum = 0;
i = 0;
while i < 10:
    sum = sum + i;
    print(sum);
    i = i + 1;

def calculateNTetrahedralNumber(startvalue, endvalue):
    # Write your code here
    start = startvalue;
    end = endvalue;
    finalResult = [];
    while start <= end:
        result = (start*(start+1)*(start+2))/6
        finalResult.append(math.trunc(result));
        start = start + 1;
    
    return finalResult;