n=int(input("enter the number:"))

sum = 0
temp = n

while temp > 0 :
    digit = temp % 10
    sum += digit **3
    temp = temp//10
if n == sum :
    print("Amstrong number")
else:
    print("Not Amstrong number")
    
