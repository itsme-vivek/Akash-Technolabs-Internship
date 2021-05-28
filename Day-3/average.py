# Type-1
print("Average of 5 numbers")
a=int(input("Enter a value of 1st number:"))
b=int(input("Enter a value of 2nd number:"))
c=int(input("Enter a value of 3rd number:"))
d=int(input("Enter a value of 4th number:"))
e=int(input("Enter a value of 5th number:"))

average=(a+b+c+d+e)/5

print("Average of 5 numbers:",average)

#Type-2

n = int(input("Enter How Many Number You Want To average:"))
total = 0
for i in range (0,n):
    number = int(input("enter value of numbers:"))
    total += number
avg = total/n
print(total)
print(avg)    
