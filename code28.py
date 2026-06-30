def sum(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mult(a,b):
    print(a*b)

def div(a,b):
    print(a%b)


num1 = int(input("Enter the first number"))

num2 = int(input("Enter the second number"))

print("Choose the required operation")
print("Press 1 for addition \nPress 2 for substraction \nPress 3 for multiplication \nPress 4 for Division")
choice =int(input("Enter your choice from 1 to 4"))

if choice == 1:
    sum(num1,num2)
elif choice == 2:
    sub(num1,num2)
elif choice == 3:
    mult(num1,num2)
else:
    div(num1,num2)