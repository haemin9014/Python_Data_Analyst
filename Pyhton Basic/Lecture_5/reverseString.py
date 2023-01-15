# 3 ways how we can reverse String.
inputStr = "reverseString"

result = "";

for i in range(len(inputStr) -1, -1, -1):
    result += inputStr[i];

print(result);

result = "";

print("Empty result: %s" %result);

revsersedChar = reversed(inputStr)
print(''.join(revsersedChar));

print(inputStr[-1::-1]);