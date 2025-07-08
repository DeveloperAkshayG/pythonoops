class Car:
    name = "Mercedes"

    def accelerate(self):
        print("accelerating car {}".format(self.name))

m1=Car()
print(m1.name)
m1.accelerate()
m2=Car()
"""declaration from main method"""
m2.name = "Audi"
m2.accelerate()