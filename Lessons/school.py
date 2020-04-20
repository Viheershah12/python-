courses = [[1,'Computer Science',50000],
        [2,'Software Engineering',40000],
        [3,'Computer Management',30000],
        [4,'Graphics Manipulation',10000],
        [5,'Hardware Engineering',30000],
        [5,'Mechatronics',60000],
        [6,'Mechanical Engineering',50000],
        [7,'Accounting',40000],
        [8,'Sales Manager',60000],
        [9,'Bachelors in IT',60000],
        [10,'Surgoen',90000]
        ]

teache = [[1,'Mr John'],
        [2,'Mr Joseph'],
        [3,'Mr James'],
        [4,'Mrs Mercy'],
        [5,'Ms jane']
        ]

def getCourse(id):
    found = False
    for course in courses:
        if course[0] == id:
            returnValue = course
            found = True
    if found == False:
        returnValue = 'Not found'
    return returnValue
    
def getTeacher(id):
	found = False
	for teacher in teache:
		if teacher[0] == id:
			returnValue = teacher
			found = True
	if found == False:
		returnValue = 'Not found'
	return returnValue

for course in courses:
    for i in course:
        print(i,end="\t")
    print()
print("\nSelect the courses you want to enroll in (Press Enter when done)")

Courses_Chosen = []
opt = 0
while opt != "":
    opt = input("Enter course chosen to enroll (number): ")
    if opt != "":
        Courses_Chosen.append(int(opt))
print("\n")

total = 0 
for course in Courses_Chosen:
    courseDetails = getCourse(course)
    total += courseDetails[2]
    for i in courseDetails:
        print(i,end="\t")
    print()
print("\n")

for teacher in teache:
    for i in teacher:
        print(i,end="\t")
    print()

print("\nChoose the teacher to be assigned (Press Enter when done")

teacher_Chosen = []
chosen = 0
while chosen != "":
    chosen = input("Enter the teacher chosen (number): ")
    if chosen != "":
        teacher_Chosen.append(int(chosen))
print("\n")

for teacher in teacher_Chosen:
    TeacherDetails = getTeacher(teacher)
    for i in TeacherDetails:
        print(i,end="\t")
    print()

print("\n\ntotal cost of the courses: ",str(total))
print("\n")
print("Year of enrollment in the university")
print("1.Sept 2020")
print("2.Feb 2021")
print("3.June 2021")
print("\n")
enrollment = input("choose a year of enrollment for further info (1/2/3): ")

if int(enrollment) == 1:
    print("\nstart application process with full details")
    print("\nEnter your details: ")
    FullNames = []
    PhoneNum = []
    Age = []
    FullName = input("Enter your full names: ")
    PhoneNump = input("Enter your Phone Number: ")
    Agep = input("Enter your age as of the current date: ")
    FullNames.append(FullName)
    PhoneNum.append(PhoneNump)
    Age.append(Agep)
    print("\nReveiw your details below before submitting: ")
    print("\n",FullNames[0],Age[0],PhoneNum[0],"\n")
    confirm = input("Are you happy with your details?[Y/N] ")
    
    if confirm == "Y" or confirm == "y":
        print("Thank you for the confirmation, your application has been submitted")
    else:
        FullNames.clear()
        PhoneNum.clear()
        Age.clear()
        print("\nResubmit the information you have entered: ")
        FullName = input("Re-Enter your full names: ")
        PhoneNump = input("Re-Enter your Phone Number: ")
        Agep = input("Re-Enter your age as of the current date: ")
        FullNames.append(FullName)
        PhoneNum.append(PhoneNump)
        Age.append(Agep)
        print("\n",FullNames[0],Age[0],PhoneNum[0])
        Reconfirm = input("\nAre the details okay? [Y/N] ")
        if Reconfirm == "Y" or Reconfirm == "y":
            print("\nThank you for the Application, it has been sent to the addmisions team")
        else:
            print("\nKindly gather your data correctly and enter it later on")
            
elif int(enrollment) == 2:
    print("\nYou may research more about our university as the deadline for visa application is far")
else:
    print("\ndeadline for application is on 01/01/2021 please apply in good time")

input("\n\nEnter to Exit")