# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_value = 0
for n in student_scores:
 if max_value == None or n > max_value:
   max_value = n

print(f" Max value is : {max_value} ") 
