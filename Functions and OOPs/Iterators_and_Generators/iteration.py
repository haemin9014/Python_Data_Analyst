#navigating all the items from sequence.
#list also can be called as interator.
lst1 =[1,2,3,4];
# for i in lst1:
#     print(i);

#it is anything that iterate through ony be one all the elements.
iter1 = iter([1,2,3]);

for i in iter1:
    print("printing out iter: %s" %i);

iter2 = iter([1,2,3]);
print("using first next() : %s" %next(iter2));
print("using second next() : %s" %next(iter2));
print("using third next() : %s" %next(iter2));

iter3 = iter([1,2,3]);
print("Printing out iteration using while loop and next()")
while True:
    try:
        print(next(iter3));
    except StopIteration:
        break;