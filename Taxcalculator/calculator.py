#Asks the user how many items they will buy.
numItems = float(input("How many items would you like to buy? "))
if numItems == 1:
#Asks the user how much the item is.
	item = float(input("How much was the item?" " $"))
	
if numItems == 2:
	itemOne = float(input("How much was the first item?" " $"))
	itemTwo = float(input("How much was the second item?" " $"))
	item = itemOne + itemTwo
	
if numItems == 3:
	itemOne = float(input("How much was the first item?" " $"))
	itemTwo = float(input("How much was the second item?" " $"))
	itemThree = float(input("How much was the third item?" " $"))
	item = itemOne + itemTwo + itemThree
	
if numItems > 3:
	print("Sorry, you can only calculate only three items at a time.")
#Defines the tax variable.
tax = 0.00
#Asks the user what state they live in.
state = input("What state do you live in? ")
if state == "AL" or "Alabama":
		tax = 4.00
		
if state == "AK" or "Alaska":
		tax = 1.69
		
if state == "AZ" or "Arizona":
		tax = 8.17
		
if state == "AR" or "Arkansas":
		tax = 9.19
		
if state == "CA" or "California":
		tax = 8.41
		
if state == "CO" or "Colorado":
		tax = 7.39
		
if state == "CT" or "Connecticut":
		tax = 6.35
		
if state == "DE" or "Deleware":
		tax = 0
		
if state == "FL" or "Florida":
		tax = 6.62
		
if state == "GA" or "Georgia":
		tax = 6.97
		
if state =="HI" or "Hawaii":
		tax = 4.35
		
if state == "ID" or "Idaho":
		tax = 6.03
		
if state == "IL" or "Illinois":
		tax = 8.16
		
if state == "IN" or "Indiana":
		tax = 7.00
		
if state == "IA" or "Iowa":
		tax = 6.78
		
if state == "KS" or "Kansas":
		tax = 8.15
		
if state == "KY" or "Kentucky":
		tax = 6.00
		
if state == "LA" or "Lousiana":
		tax = 8.89
		
if state == "ME" or "Maine":
		tax = 5.50
		
if state == "MD" or "Maryland":
		tax = 6.00
		
if state == "MA" or "Massachusetts":
		tax = 6.25
		
if state == "MI" or "Michigan":
		tax = 6.00
		
if state == "MN" or "Minnesota":
		tax = 7.19
		
if state == "MS" or "Mississippi":
		tax =  7.00
		
if state == "MO" or "Missouri":
		tax = 7.58
		
if state == "MT" or "Montana":
		tax = 0
		
if state == "NE" or "Nebraska":
		tax = 6.79
		
if state == "NV" or "Nevada":
		tax = 7.93
		
if state == "NH" or "New Hampshire":
		tax = 0
		
if state == "NJ" or "New Jersey":
		tax = 6.97
		
if state == "NM" or "New Mexico":
		tax = 7.26
		
if state == "NY" or "New York":
		tax = 8.47
		
if state == "NC" or "North Carolina":
		tax = 6.90
		
if state == "ND" or "North Dakota":
		tax = 6.55
		
if state == "OH" or "Ohio":
		tax = 7.11
		
if state == "OK" or "Oklahoma":
		tax = 8.72
		
if state == "OR" or "Oregon":
		tax = 0
		
if state == "PA" or "Pennsylvania":
		tax = 6.34
		
if state == "RI" or "Rhode Island":
		tax = 7.00
		
if state == "SC" or "South Carolina":
		tax = 7.19
		
if state == "SD" or "South Dakota":
		tax = 5.83
		
if state == "TN" or "Tennessee":
		tax = 9.45
		
if state == "TX" or "Texas":
		tax = 8.15
		
if state == "UT" or "Utah":
		tax = 6.68
		
if state == "VT" or "Vermont":
		tax = 6.14
		
if state == "VA" or "Virginia":
		tax = 5.63
		
if state == "WA" or "Washington":
		tax = 8.88
		
if state ==  "WV" or "West Virginia":
		tax = 6.07
		
if state == "WI" or "Wisconsin":
		tax = 5.43
		
if state == "WY" or "Wyoming":
		tax = 5.49
#Asks the user if they want the total or the tax.
totalOrTax = input("Do you want to see the tax, the total, or both? ")


realTax = tax / 100
totalTax = realTax * item
total = item + totalTax

item = str(item)
tax = str(tax)

#Prints either the total or the tax of the item which the user asked earlier.
if totalOrTax == "total":
	print("%.2f" % total)

if totalOrTax == "tax":
	print("%.2f" % totalTax)
	
if totalOrTax == "both":
	print("The sales tax is " "%.2f" % totalTax)
	print("Your total is " "%.2f" % total)

input("Press any button to close.")
