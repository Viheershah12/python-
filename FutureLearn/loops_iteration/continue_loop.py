while True:
    line = input("Enter: ")
    if line[0] == "#":
        continue
    if line.lower() == "done":
        break
    print(line)
print("done!")

input()