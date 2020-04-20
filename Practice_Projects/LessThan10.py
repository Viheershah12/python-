a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if int(i) <= 5:
        nums = i
        b.append(i)

for j in b:
    print(j,end="\t")
    
# exercise 2
num = int(input("\n\n Enter any number of your choice: "))
lessnum = []
for i in a:
    if int(i) < num:
        lessnum.append(i)

for k in lessnum:
    print(k,end="\t")