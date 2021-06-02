class scheme:
    
    def schems(self):
        print("Scheme Details")
        print("1.JIO")
        print("2.Airtel")
        print("3.Vi")
        self.scheme_id=int(input("Choose Your Scheme ID:"))
        if self.scheme_id==1:
            print("You are Using Jio")
        elif self.scheme_id==2:
            print("You are Using Airtel")
        else :
            print("You are using Vi")

        self.scheme_name=input("Choose Your Scheme Name from jio,airtel:")
        if self.scheme_name=="jio":
            print("You are Using Jio")
            print("You have 100 free message daily")
            print("Your are using unlimited calling")
        elif self.scheme_name=="airtel":
            print("You are Using Airtel")
            print("Your Message Rate is Rs.1.5")
            print("Your Call Rate is Rs.1.5/min")
        else :
            print("You are using other operator")
            

class customer:

    def cus(self):
        self.cusID=int(input("Enter Your Customer ID:"))
        self.cusname=input("Enter Your Name:")
        self.mno=input("Enter Your Mobile No:")
        print("Customer ID is ",self.cusID)
        print("Customer Name is ",self.cusname)
        print("Customer Mobile Number is",self.mno)


m=scheme()
m1=customer()
m.schems()
m1.cus()