num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
num3 = float(input("Enter Third Number : "))

if num1 > num2:
    if num1 > num3:
        print("Largest number is : ", num1)
    else:
        print("Largest number is : ", num3)
elif num2 > num1:
    if num2 > num3:
        print("largest number is : ", num2)
    else:
        print("largest number is : ", num3)

