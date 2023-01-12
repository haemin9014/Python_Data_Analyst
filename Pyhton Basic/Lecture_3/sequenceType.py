# String is an immutable object.
def stringoperation(fn, ln, para, number):
    # Write your code here
    print(fn+'\n'*number, end ="");
    print(ln);
    print(fn + " " + ln);
    print(fn*number);
    print("The sentence is %s" %para);

def Escape(s1, s2, s3):
    # Write your code here
    s = "Python\tRaw\nString\tConcept";
    print(s1 + "\n" +s2 + "\n" +s3);
    print(s1 + "\t" +s2 + "\t" +s3);
    print(s);
    # to print raw string, we need to put r front of string
    s = r"Python\tRaw\nString\tConcept";
    print(s);

def resume(first, second, parent, city, phone, start, strfind, string1):
    # Write your code here
    print(first.strip().capitalize() + " " + second.strip().capitalize() + " " + parent.strip().capitalize() + " " + city.strip());
    print(phone.isdigit());
    print(phone.startswith(start));
    print(first.count(strfind) + second.count(strfind) + parent.count(strfind) + city.count(strfind));
    print(string1.split());
    print(city.find(strfind));