n = int(input("Enter the number to find: "))
list = [54, 76, 34, 876, 90]

found = False  # Variable to track if the number is found

for i in range(len(list)):
    if list[i] == n:
        print("Found at position", i+1)
        found = True
        break  # Exiting loop once the number is found

if not found:
    print("Not found")
