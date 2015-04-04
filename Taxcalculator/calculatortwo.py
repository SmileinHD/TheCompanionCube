import statetaxes

tax = 0.00


#Future feature, asks the user how many items there was for finding the
#total of multiple items
numberItem = float(input("\nHow many items are there?: "))
#Asks the user how much the item was
if numberItem == 1: 
	item = float(input("\nHow much was the item?: "))

#Asks the user what state they live in to determine the sales tax
state = input("\nWhat is the abbreviation or name of your state?: ")


statetaxes.taxes(state)
print(tax)

#Asks the user if they want the total or the tax.
totalOrTax = input("\nDo you want to see the tax or the total?: ")

realTax = tax / 100
totalTax = realTax * item
total = item + totalTax

meal = str(item)
tax = str(tax)

#Prints either the total or the tax of the item which the user asked earlier.
if totalOrTax == "total":
	print("\n %.2f" % total)

if totalOrTax == "tax":
	print("\n %.2f" % totalTax)

input("Press any button to close.")


