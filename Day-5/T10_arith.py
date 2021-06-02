class arith:

    def __init__(self):
        self.a=float(input("Enter a value of a :"))
        self.b=float(input("Enter a value of b:"))
    
    def s1(self):
        self.sum=self.a+self.b
        print("Addition Is ",self.sum)

    def s2(self):    
        self.multi=self.a*self.b
        print("Multiplication Is",self.multi)

    def s3(self):    
        self.sub=self.a-self.b
        print("Subtraction Is",self.sub)
        

m=arith()
m.s1()
m.s2()
m.s3()

