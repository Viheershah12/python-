intersts = [
                [1,'Programming'],
                [2,'Wrinting'],
                [3,'Reading'],
                [4,'Typing'],
                [5,'Listening'],
                [6,'Singing'],
                [7,'Drawing'],
                [8,'Physical Acitivities'],
                [9,'Thinking'],
                [10,'Problem Solving']
            ]
courses =   [
                [[4,1,10,9,5],'computer science',],
                [[3,8,7,10,9],'Engineering'],
                [[2,3,4,5,9],'Teaching']
            ]

#ask the user to enter 5 options
#store the user selection in an array
#check the items in the user selection against the itenms
#each courses array and corresponding value obtained as a percentage
#return the course with the greatest value
for interest in intersts:
	for i in interest:
		print(i,end="\t")
	print()
 
user_interests = []
opt = 0
while opt != "":
    opt = input("Enter your choice (number): ")
    if opt != "":
        user_interests.append(opt)


            


        
        
        
input("Press enter to exit")