class cal4:
    
    def setdata(self):
        self.n=float(input("Enter A Number:"))

    def display(self):
        square=self.n*self.n
        return square

m=cal4()
m.setdata()
print("Square is",m.display())            