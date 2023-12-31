WAP that determines whether a given input year is a leap year or not


x = int(input("Enter year:"))
if (x%4==0 and x%400==0 and x%100!=0):
    print(x,"is an leap year")
else:
    print(x,"is not an leap year")
