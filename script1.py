#this is a comment
#this line will not execute
names = []
num = int(input("Enter number of student "))
num1 = 1
for i in range(num):
	name = input ("Enter your name "+str(i+1)+" ") #declaration of a variable called name given by the user
	names.append(name)
#print (names)
for student in names:
	print(str(num1)+" "+student)
	num1 = num1 + 1
input ("Enter to exit")