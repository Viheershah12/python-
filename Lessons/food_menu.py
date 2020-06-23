menu = [[1,"Chapati",50]
	    [2,"Rice",100],
		[3,"Paneer",70],
		[4,"Coffee",20],
		[5,"Tea",30],
		[6,"Cold-Coffee",150],
		[7,"Faluda",200],
		[8,"Fried Noodles", 300],
		[9,"Pizza",800],
		[10,"Chips",250]
		]

def getItem(id):
	found = False
	for item in menu:
		if item[0] == id:
			returnValue = item 
			found = True
	if found == False:
		returnValue = 'Not found'
	return returnValue

print("\n\nwelcome to the highway side restaurant")	
print("\nSelect items you want (Press Enter when you are done)")
for item in menu:
	for i in item:
		print(i,end="\t")
	print()

cart = []
opt  = 0
while opt != "":
    opt = input("Enter your choice (number): ")
    if opt != "":
        cart.append(int(opt))

print("\nYour order details:\n")
total = 0
for item in cart:
	itemDetails = getItem(item)
	total += itemDetails[2]
	for i in itemDetails:
		print(i,end="\t")
	print()

takein = input("\nWould you like to have take away? [Y/N] ")
if takein == 'y' or takein == 'Y':
    total += 50
else:
	total += 0

print("\nSub-total cost: ",str(total))

print("We accept payments via both credit cards and Mpesa")
paymentMeth = input("Choose a payment method: ")
if paymentMeth == "mpesa" or paymentMeth == "Mpesa":
    total += 30
else:
    total += 50
print("\nTotal cost: ",str(total))
input("\nEnter to Exit")

print("hello")
