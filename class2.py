class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def achieveddistinction(self):
        if self.grade >60 and self.grade <75:
            print("{} has achieved first class with percentage of {}".format(self.name,self.grade))
        elif self.grade >70:
            print("{} has achieved distinction with percentage of {}".format(self.name,self.grade))
        else:
            print("{} did not achieved first class".format(self.name))

s1=Student("Akshay",65)
print(s1.name)
print(s1.grade)
s1.achieveddistinction()

s2=Student("sayali",96)
print(s2.name)
print(s2.grade)
s2.achieveddistinction()

s3=Student("chhayesh",50)
print(s3.name)
print(s3.grade)
s3.achieveddistinction()
