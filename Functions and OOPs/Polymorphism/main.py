#In the below shown example, you will find

#Improvised Employee class with two methods getSalary and getBonus.

#Definition of ContractEmployee class derived from Employee. It overrides functionality of getSalary and getBonus methods found in it's parent class Employee.

#Example
class Employee(Person):
    all_employees = EmployeesList ()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
    def getSalary(self):
        return 'You get Monthly salary.'
    def getBonus(self):
        return 'You are eligible for Bonus.'