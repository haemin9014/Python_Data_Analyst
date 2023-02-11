#class <ClassName>(<parent1>, ... ):
#    class_body

class Person:
    pass
#p1 = Person()      # Creating the object 'p1'
#print(p1)            # -> '<__main__.Person object at 0x0A...>'
# p1.fname = 'Jack'
# p1.lname = 'Simmons'
# print(p1.fname, '-', p1.lname)  # -> 'Jack - Simmons'

#or
#this might be more easier way to do.
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
p1 = Person('George', 'Smith')   
print(p1.fname, '-', p1.lname)           # -> 'George - Smith'