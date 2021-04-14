# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

print(f"Opcion 1 {names[random.randint(0,len(names))]} is going to buy the meal today!")
print(f"Opcion 2  {random.choice(names)} is going to buy the meal today!")
