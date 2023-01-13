nums = [25, 12, 36, 95, 14];
print(nums[0]);

#list could have different data
#example
values = [9.5, 'Navin', 25];

doubleList = [[1,2,3,4,5],['a','b','c','d','e','f']];

print(doubleList);
#nums.insert()
#nums.append()
#nums.remove()
#nums.pop()
#del nums[2:];
#nums.extend

def List_Op(Mylist, Mylist2):
    # Write your code here
    print(Mylist);
    print(Mylist[1]);
    print(Mylist[len(Mylist) - 1]);
    Mylist.append(3);
    Mylist[3] = 60;
    print(Mylist);
    print(Mylist[1:5]);
    Mylist.append(Mylist2);
    print(Mylist);
    Mylist.extend(Mylist2);
    print(Mylist);
    Mylist.pop();
    print(Mylist);
    print(len(Mylist));
