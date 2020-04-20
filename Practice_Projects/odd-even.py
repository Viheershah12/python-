num = int(input("Enter a number of your choice: "))
check = 2
dev = num % 2
if dev > 0:
    print("The number ",num," is a odd number")
else:
    print("The number ",num," is a even number")
    
# more complex function to see if the number is divisible by 4
num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
input("Enter to exit")