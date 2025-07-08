class Employee:
    numberofhrs=40 #class attributes
    name = "ben"

e1=Employee()
print(e1.name)
print(e1.numberofhrs)
print(Employee.numberofhrs)
print('\n')

e2=Employee()
print(e2.name)
print(e2.numberofhrs)
e2.numberofhrs=45 #instance attributes
print(e2.numberofhrs)
print(Employee.numberofhrs)