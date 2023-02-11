class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

#Employee class is derived from Person.
class Employee(Person):
    all_employees = []
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
    
p1 = Person('George', 'smith')
print(p1.fname, '-', p1.lname)
e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('John', 'williams', 123656)
print(e1.fname, '-', e1.empid)
print(e2.fname, '-', e2.empid)

#n the above example, Employee class utilizes __init __ method of the parent class Person to create its object.

#Inheritance feature can be also used to extend the built-in classes like list or dict.
#The following example extends list and creates EmployeesList, which can identify employees, 
#having a given search word in their first name.

class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in Employee.all_employees:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees


#Extending Built-in Types EmployeesList object can be used to store all employee objects, 
#just by replacing statement all_employees = [] with all_employees = EmployeesList().
all_employees = EmployeesList()
def __init__(self, fname, lname, empid):
    Person.__init__(self, fname, lname)
    self.empid = empid
    Employee.all_employees.append(self)

e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('George', 'Brown', 656721)
print(Employee.all_employees.search('or'))
