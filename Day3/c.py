
height = float (input("Enter your height in m :"))
weight = int (input("Enter your weight in kg :"))

BMI = weight / height **2

New_BMI = int(BMI)
#print(BMI)

print(New_BMI)

#print(round(8/3,2))
if New_BMI < 18.5 :
    print(f"Your bmi is {New_BMI}, You are underweight. ")
elif New_BMI < 25 :
    print(f"Your bmi is {New_BMI}, You are Normal Weight . ")
elif New_BMI < 30 :
    print(f"Your bmi is {New_BMI}, You are OverWeight . ")
elif New_BMI < 35 :
    print(f"Your bmi is {New_BMI}, You are Obese . ")
else:
    print(f"Your bmi is {New_BMI}, You are Clinically Obese . ")
