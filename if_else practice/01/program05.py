Write a program to take an integer ranging from 0 to 6 and print corresponding week day (week starting from Monday)


x = int(input("Enter any no. ranging from 0-6"))
if(x==0):
    print(x,"is Monday")
elif(x==1):
    print(x,"is Tuesday")
elif(x==2):
    print(x,"is Wednesday")
elif(x==3):
    print(x,"is Thursday")
elif(x==4):
    print(x,"is Friday")
elif(x==5):
    print(x,"is Saturday")
elif(x==6):
    print(x,"is Sunday")
else:
    print(x,"is an invalid syntax")
