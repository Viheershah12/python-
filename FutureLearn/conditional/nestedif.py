x = 5
if x > 2:
    print("Bigger than 2")
    print("still bigger")
print("done with 2")

for i in range(5):
    print(i,end="\t")
    if i > 2:
        print("bigger than 2")
    else:
        print("done with i", i)
print("all done")