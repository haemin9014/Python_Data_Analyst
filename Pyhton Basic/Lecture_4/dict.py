#unorder but it have key and value
a = {"John": 15000, "mac": 20000};
print(a["John"]);

#it is able to change the value
a["John"] = 90000;
a["mac"] = 80000;
print(a);
del a["mac"];
print(a);
a["Ray"] = 100000;
print(a);
print(a.keys());
print(a.values());

def myDict(key1, value1, key2, value2, value3, key3):
    # Write your code here
    dictValue = {key1: value1};
    print(dictValue);
    dictValue[key2]= value2;
    print(dictValue);
    dictValue[key1] = value3;
    print(dictValue);
    dictValue.pop(key3);
    return dictValue;