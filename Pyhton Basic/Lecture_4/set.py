#all element is unique
#we use when order of data odes not matter and it must be unique

#Accessing set
a = set([1,4,3,'abc',5]);
b = {1,2,3};
c = set();
print(a);
print(b);
print(c);
#Finding length/ accessing
len(a);

for x in a:
    print(x);

#adding/updating
#add single
c.add(3);

#add multiple
c.update([2, 'abc', 3]);
#removing deleting
#delete one
c.remove(3);
#when we are not sure if we have that element.
c.discard(1);
#delete the random value.
c.pop();

#union
print(a|b);
print(a|b|c);
print(a.union(b));
print(a.union(b,c));

#Intersection(which both of them have it)
print(a&b);
print(a.intersection(b,c));

#Difference
print(a-b);
print(a.difference(b,c));

#frozne sets which value can not be modify
d = frozenset(a);

def setOperation(seta, setb):
    # Write your code here
    seta = set(seta);
    setb = set(setb);
    setUnion = seta.union(setb);
    setIntersection = seta&setb;
    setDifference1 = seta-setb;
    setDifference2 = setb-seta;
    setSysDifference = seta.symmetric_difference(setb);
    setFrozen = frozenset(seta);
    return (setUnion, setIntersection, setDifference1, setDifference2, setSysDifference, setFrozen);
