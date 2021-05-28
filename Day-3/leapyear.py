print("Check Weather Year Is Leap Year Or Not")
year = int(input("Enter A Year:"))
if (year%4) == 0:
    print("This Is Leap Year")
elif (year%400) == 0:
    print("This Is Leap Year")
elif (year%100) != 0:
    print("This Is Leap Year")
else :
    print("This Is Not Leap Year")            