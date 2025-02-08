# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

Total_height = 0 
for height in student_heights:
  Total_height += height
#print(Total_height  )


number_of_student = 0 
for student in student_heights:
  number_of_student += 1
#print(number_of_student)

average_height = round(Total_height/ number_of_student)

print(average_height)
