print("Find Smallest Number In 3 NUmbers")
a=int(input("Enter 1st Number:"))
b=int(input("ENter 2nd Number:"))
c=int(input("Enter 3rd Number:"))
if a<b:
    if a<c:
        print(a,"is smaller")
    else:
         print(c,"is smaller")
else :
    if b<c:
        print(b,"is smaller")
    else:
        print(c,"is smaller")                