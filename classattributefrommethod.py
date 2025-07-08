class Car:
    """declaration using method"""
    def set_name(self,name):
        self.name=name

    def display(self):
        print("car name is {}".format(self.name))

c1=Car()
c1.set_name("wagonr")
c1.display()

c2=Car()
c2.set_name("ferrari")
c2.display()