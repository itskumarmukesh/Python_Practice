"""def fb(n):
    if n == 1 :
        return 0
    elif n == 2:
        return 1
    else:
        return(fb(n-1)+fb(n-2))

num = int(input("Please enter the number "))

print(fb(num))"""

def fibo (n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
n = int(input("Enter a number here : "))    
if n<=0:
    print("Enter a positive number")
else :
    print("Fibonacci Sequence")
    for i in range(n):
        print(fibo(i))