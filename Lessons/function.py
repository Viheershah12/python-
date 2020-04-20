#inputting numbers in the array
def array():
	numOfValues = 5
	arrayOfValues = []
	for i in range(numOfValues):
		x = i+1
		number = int(input("Enter the number "+str(x)+":"))
		arrayOfValues.append(number)
	return arrayOfValues

#get the max value
def max(randNumbers):
	max = 0
	for num in randNumbers:
		if num > max:
			max = num
	return max

#getting the min value	
def min(randNumbers):
	min = 1000
	for num in randNumbers:
		if num < min:	
			min = num
	return min

#main function 
values = array()
maxVal = max(values)
minVal = min(values)
print("Maximum value: "+str(maxVal))
print("Minimal value: "+str(minVal))
input("Enter to Exit")	
