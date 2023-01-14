a = (12, 13,);
b = (123, 12.23, "demo");
print(b[1]);

def tuplefunction(list1, list2, string1, n):
    # Write your code here
    tuple1 = tuple(list1);
    tuple2 = tuple(list2);
    tuples = tuple1 + tuple2;
    print(tuples);
    print(tuples[4]);
    nestedTuple = (tuple1,tuple2);
    print(nestedTuple);
    print(len(nestedTuple));
    tuple3 = ((string1,) * n);
    print(tuple3);
    print(max(tuple1));
