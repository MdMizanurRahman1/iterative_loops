#2
#asks the user to enter numbers until they input an empty string to quit.
#prints out the five greatest numbers sorted in descending order

user=input("enter the number: ")
numbers=[]
while user!="":
    numbers.append(int(user))
    user=input("enter the number: ")
numbers.sort(reverse=True)
#print(numbers)
print("The five greatest numbers are:")
print(numbers[:5])
