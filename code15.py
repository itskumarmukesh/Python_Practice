"""num = int(input("Enter a number : "))
fact = 1
for i in range(1, num+1):
    fact = i*fact
print("Factorial of ", num, "is : ", fact)"""

def Fact(i):
    if i == 0 or i ==1:
        return 1
    else:
        return i * Fact(i-1)
    
num = int(input("Enter a number : "))
factorial = Fact(num)
print("Factorial of ", num, "is : ", factorial)