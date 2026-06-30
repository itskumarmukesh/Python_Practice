"""num1 = int(input("Enter the number to check divisibility"))

for i in range(1,num1):
    if num1%1 != 0:
         print("Number is not divisible by ", i)
        
    else:
       print("Number is divisible by ", i)"""

num = int(input("Enter the number to check divisibility "))

L = range(1, num)

result = list(filter(lambda x : num%x == 0, L))

print("The numbers divisible by num are ", result)