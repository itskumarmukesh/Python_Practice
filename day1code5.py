#write a program to swap two variables

"""def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number : "))
print("Before swapping : ", num1, num2)
print("After swapping : ",swap(num1,num2))"""


num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

num1, num2 = num2, num1
print("After swapping :", num1, num2)