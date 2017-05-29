#####################
# 1. Print Hello World

print("Hello World!")

# 2. Create a list called "fruit that has Apples, Oranges and Bananas
#    as values.

fruit = ["Apples", "Oranges", "Bananas"]

# 3. Print the list.

print(fruit)

# 4. Change Oranges to Grapes using the numeric list index.

fruit[1] = "Grapes"

# 5. Create a loop that prints out each item in the fruit list.

for afruitinthelist in fruit:
	print(afruitinthelist)

# 6. Create a dictionary called "people" that contains another dictionary
#    for each Bob (age 22), Carol (age 47) and Justin(age 14) with their
#    name and age.

class Peeps(object):
	name = ""
	age  = 0

def make_peeps(name, age):
	person = Peeps(name,age)
	return person

people = []

people.append(make_peeps("Bob", 22))
