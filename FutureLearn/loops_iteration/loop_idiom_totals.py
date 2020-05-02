count = 0
sum = 0
print("Before", count, sum)
for value in [3,41,12,9,74,15]:
    sum = sum + value
    count = count + 1
    print(count, sum, value)
print("after", count, sum, sum/count)

input()