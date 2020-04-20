num = int(input("Input a number to divide with: "))

listrange = range(1,num+1)
divisorsList = []

for div in listrange:
    if num % div == 0:
        divisorsList.append(div)
        
for i in divisorsList:
    print(i,end="\t")