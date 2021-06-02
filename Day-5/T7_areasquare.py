class cal6:

    def setdata(self):
        self.s=float(input("Enter Value of Side:"))

    def area(self):
        self.area=self.s*self.s

    def display(self):
        print("Area of Square is ",self.area)

m=cal6()
m.setdata()
m.area()
m.display()                