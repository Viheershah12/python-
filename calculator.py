while True:
	print("Choose one of the options below:")
	print(" ")
	print("1.add")
	print("2.subtract")
	print("3.multiply")
	print("4.divide")
	print("5.square")
	print("6.quit\n")
	print(" ")

	user_input = input("choose option(1/2/3/4/5/6): ")

	if user_input == "6":
		break

	elif user_input == "1":
		num1 = int(input("Enter number 1: "))
		num2 = int(input("Enter number 2: "))
		result = str(num1 + num2)
		print("The answer is " + result + "\n")


	elif user_input == "2":
		num1 = int(input("Enter number 1: "))
		num2 = int(input("Enter number 2: "))
		result = str(num1 - num2)
		print("The answer is " + result + "\n")


	elif user_input == "3":
		num1 = int(input("Enter number 1: "))
		num2 = int(input("Enter number 2: "))
		result = str(num1 * num2)
		print("The answer is " + result + "\n")


	elif user_input == "4":
		num1 = int(input("Enter number 1: "))
		num2 = int(input("Enter number 2: "))
		result = str(num1 / num2)
		print("The answer is " + result + "\n")

	elif user_input == "5":
		num = int(input("Enter the number to be squared: "))
		result = str(num * num)
		print("The asnwer is " + result + "\n")

	else:
		print("input a valid number")


input("Enter to exit")
