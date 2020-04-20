string = input("Input any string of your choice: ")

word = str(string)
rvs=word[::-1]
print(rvs)
if word == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")