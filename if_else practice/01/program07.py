Write a program to take a number of months and print the number of days in that month


month = int(input("Enter any no. from 1-12:"))
if(month==1):
    print("January is a 31-day month.")
elif(month==2):
    print("February is a 28-day month.")
elif(month==3):
    print("March is a 31-day month.")
elif(month==4):
    print("April is a 30-day month.")
elif(month==5):
    print("May is a 31-day month.")
elif(month==6):
    print("June is a 30-day month.")
elif(month==7):
    print("July is a 31-day month.")
elif(month==8):
    print("August is a 31-day month.")
elif(month==9):
    print("September is a 30-day month.")
elif(month==10):
    print("October is a 31-day month.")
elif(month==11):
    print("November is a 30-day month.")
elif(month==12):
    print("December is a 31-day month.")
else:
    print("invalid no")
