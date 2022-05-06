

class student:
    def __init__(self):
        self.name="hai"
        self.rollno=20
        self.lap=self.Laptop()

    def show(self):
      print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8

s1=student()
s1.show()
lap1=s1.lap
print(lap1.brand)
