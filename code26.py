def findHCF(num1,num2):
    if num1>num2:
        smaller = num2
    else:
        smaller = num1

    for i in range(1,smaller+1):
        if((num1%i == 0) and (num2%i == 0)):
            hcf = i
    return hcf


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The HCF of the given two numbers is ", findHCF(num1,num2))
