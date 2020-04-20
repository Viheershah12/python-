a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []

for i in a:
    num = int(i) % 2
    if num == 0:
        even.append(i)

for j in even:
    print(j,end="\t")