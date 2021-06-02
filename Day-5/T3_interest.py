class cal3:

    def callnterest(self):
        self.I=float(input("Enter Value of I:"))
        self.P=float(input("Enter Value of P:"))
        self.R=float(input("Enter Value of R:"))

    def display(self):
        simple_interest=(self.I*self.P*self.R)/100
        print("Simple Interest Is:",simple_interest)


m=cal3()
m.callnterest()
m.display()