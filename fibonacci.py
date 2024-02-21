fibo = int(input("Enter the number of terms: "))

n1, n2 = 0, 1
count = 0

if fibo <= 0:                                                           
    print("Enter a positive number")
elif fibo == 1:
    print("Fibonacci sequence up to", fibo, ":")
    print(n1)
else:
    print("Fibonacci series:")
    while count < fibo:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

