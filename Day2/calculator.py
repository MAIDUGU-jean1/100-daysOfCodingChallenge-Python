
print("Welcome to tips Calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("how much tip would you like to give ? 10 , 12, or 15 ? "))

people = int (input("How many people Do you split the bill ? "))

#bill_with_tip = tip/100 * bill + bill 
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_persons = total_bill/people
#final_amount =round(bill_per_persons,2)
final_amount = "{:.2f}".format(bill_per_persons)
print(f"Each Person should Pay: ${final_amount}")