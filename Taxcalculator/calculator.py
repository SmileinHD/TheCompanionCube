item = float(input("How much was the item?"))
tax = float(input("What percent was the tax?"))
#Asks the user if they want the total or the tax.
totalOrTax = input("Do you want to see the tax or the total?")

realTax = tax / 100
totalTax = realTax * item
total = item + realTax

meal = str(item)
tax = str(tax)

#Prints either the total or the tax of the item which the user asked earlier.
if totalOrTax == "total":
	print("%.2f" % total)

if totalOrTax == "tax":
	print("%.2f" % totalTax)

input("Press any button to close.")
