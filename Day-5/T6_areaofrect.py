class cal5:

    def __init__(self):
        self.a=float(input("Enter Length:"))
        self.b=float(input("Enter Height:"))

    def calArea(self):
        self.area=self.a*self.b

    def display(self):
        print("Area of rectangle",self.area)

m=cal5()
m.calArea()
m.display()            