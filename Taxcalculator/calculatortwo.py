
#imports dependinces
import json

tax = 0.00

with open('taxes.json') as data_file:    
    data = json.load(data_file)

def jsoncheck(stateName):
	tax = data["states"][stateName]["tax"]
	pass

item = float(input("How much was the item?: "))
state = input("What state are you in (Short name or fullname): ")
jsoncheck(state)
print(tax)
#Asks the user if they want the total or the tax.
totalOrTax = input("Do you want to see the tax or the total?: ")

realTax = tax / 100
totalTax = realTax * item
total = item + totalTax

meal = str(item)
tax = str(tax)

#Prints either the total or the tax of the item which the user asked earlier.
if totalOrTax == "total":
	print("%.2f" % total)

if totalOrTax == "tax":
	print("%.2f" % totalTax)

input("Press any button to close.")


