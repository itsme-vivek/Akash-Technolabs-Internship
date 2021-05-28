print("Check Number is 100 or less than 100 then check if it is odd or even")
num1 = int(input("Enter A Number:"))
if num1<=100:
    if (num1%2==0):
        print(num1,"is even")
    else:
        print(num1,"is odd")
else:
    print(num1,"is greater than 100")