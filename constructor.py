class Car:
    def __init__(self,name="Audi"):
        self.name = name

    def display(self):
        print("car is {}".format(self.name))

    @staticmethod
    def repair():
        print("service the car when you need")

c1=Car("Ferrari")
c1.display()
c1.repair()

c2=Car("Mercedes")
c2.display()
c2.repair()

c3=Car()
c3.display()


c4=Car("alto")
c4.display()

c5=Car()
c5.name="jaguar"
c5.display()
c5.repair()