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
print("select five options from the interests provided below")
for interest in intersts:
    print(str(interest[0]),'.',interest[1])
selection = []
num = 0
while num < 5:
    x = num + 1
    select = int(input("Enter option " + str(x) + ": "))
    if select != " " and select not in selection:
        selection.append(selection)
        num += 1
print(selection)
classifier = []
for course in courses:
    match = 0
    interestList = course[0]
    for userInterest in selection:
        if userInterest in interestList:
            match += 1
    score = match/5
    result = [course[1],score]
    classifier.append(result)
# veiw result
for course in classifier:
    print(str(course[1]) + "\t" + course[0])
input("Enter to Exit")

            


        
        
        
input("Press enter to exit")