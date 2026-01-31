#1
# asks the user how many dice to roll
#The program rolls all the dice once
#and prints out the sum of the numbers

import random

user=int(input("enter the number of dice to roll:"))

total_sum=0

for i in range(user):
    number=random.randint(1,6)
    total_sum=total_sum+number
print("The sum of the numbers is",total_sum)