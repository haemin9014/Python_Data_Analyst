#slice int
my_list = [0, 1, 2, 3, 4, 5, 6 ,7];

print(my_list[0:5]);
print(my_list[-4:-1]);
print(my_list[3:]);
print(my_list[2:-1:2]);
print(my_list[-2:1:-1]);
print(my_list[::-1]);

#slice String
sample_url = 'http://coreyms.com'
print(sample_url);

print(sample_url[-4:]);

def sliceit(mylist):
    # Write your code here
    print(mylist[1:3]);
    print(mylist[1:len(mylist):2]);
    print(mylist[-1:-4:-1]);
