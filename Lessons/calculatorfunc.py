#define a function to return the square of a given number 
#define anathor function to add up the numbers
#use the functions created to solve the equation
# x = a + b^2

def add(x,y):
	return x + y	

def square(x):
	return x * x
	



num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
x = add(num1 , square(num2))
print(x)
input("Enter to exit")
