num = int(input("Enter the No. for generating Fibonacci series : "))
fib0 = 0
fib1 = 1

if num == 1:
    print(a)
else:
    print(fib0)
    print(fib1)
    for i in range(1, num+1):
        c = fib0 + fib1
        fib0=fib1
        fib1=c
        print(c)