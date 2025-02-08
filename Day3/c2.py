
print("Welcome to python pizza Deliveries")
size = input("What size of pizza do you want ?  ,")
add_pepperoni = input(" Do you want pepperoni ? ")
extra_cheese = input("do you want extra cheese")

bill = 0 

if size == "S" :
    bill += 15
elif size == "M" :
    bill += 20 
elif size == "L" :
    bill += 25

if add_pepperoni == "Y" :
    if size == "S" :
        bill +=2
    else:
        bill += 3
if extra_cheese == "Y" :
    bill += 1

print(f"Your final bill is ${bill}")