class Employee:
    name = "sayali"

    def changename(self):
        Employee.name = "Akshay"

e1=Employee()
print(e1.name)
e1.changename()
print(e1.name)