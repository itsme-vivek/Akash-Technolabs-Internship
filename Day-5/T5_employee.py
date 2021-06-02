class employee:

    def info(self):
        self.name=input("Enter Your Name:")
        self.designation=input("ENter Your Designation:")
        print("Name is",self.name)
        print("Designation is",self.designation)

class salary(employee):

    def sal(self):
        self.salary1=input("Enter Your Salary:")
        print("Salary is:",self.salary1)


m1=salary()
m1.sal()
m1.info()