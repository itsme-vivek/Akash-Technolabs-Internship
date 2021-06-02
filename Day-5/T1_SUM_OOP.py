class cal1:

    def setdata(self):
        self.n1=int(input("First Number:"))
        self.n2=int(input("Second Number:"))
        self.n3=int(input("Third Number:"))

    def display(self):  
        ans=self.n1+self.n2+self.n3 
        print("Ans is:",ans)

m=cal1()
m.setdata()
m.display()