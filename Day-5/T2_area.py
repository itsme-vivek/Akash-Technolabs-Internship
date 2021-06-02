class cal2:

    def setdata(self):
        self.pi=3.14
        self.r=float(input("Radius:"))
    
    def area(self):
        self.area=self.pi*self.r*self.r

    def display(self):
        print("Area of circle is",self.area)

m=cal2()
m.setdata()
m.area()
m.display()        
