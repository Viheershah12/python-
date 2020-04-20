def incrementedA():
	array = asts
	num = int(input("Enter the number of asterixs ")) #user enters the number of asterixs
	for i in range(num):
		i = i+1
		inc = "*" * i
		array.append(inc)
	for lists in array:
		print(lists)

def cristmas():
        array = asts
        j = 9
        num = 10
        for i in range(1,num,2):
                i = i+1
                inc = j*" " + "*"*i
                j = j-1
                array.append(inc)
        for lists in array:
                print(lists)
		
asts = [] 
process = incrementedA()
process1 = cristmas()
input("Enter to Exit")
