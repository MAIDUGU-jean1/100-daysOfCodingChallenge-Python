# Coding Exercise 

Year = int(input("Which Year do You want to check? "))

if Year % 4 == 0 :
    if Year % 100 == 0 :
        if Year % 400 == 0 :
            print(" This is a leap Year ")
        else : 
            print("Not a leap Year ")
    else:
            print("Not a leap Year ")
else:
            print("Not a leap Year ")