print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentageTip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

collectivePay = ( float(bill) * ( int(percentageTip) / 100) ) + float(bill)

individualPay = "{:.2f}".format(collectivePay / int(people), 3)

print(f"Each person should pay: ${individualPay}")