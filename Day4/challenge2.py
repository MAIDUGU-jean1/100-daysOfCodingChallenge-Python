import random
name_string = input("Give me everybody's names, seperated by a comma: ")
names = name_string.split(", ")




num_items = len(names)
print(num_items)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today")
