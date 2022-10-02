#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Editing a python Script.
how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)


# In[ ]:


#Quiz 9: Generate Messages
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))


# In[ ]:


#14: practice - Error Handling
def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
try:
    num_each = cookies // people
    leftovers = cookies % people
except ZeroDivisionError:
    print("Oops, you entered 0 people will be attending.")
print("Please enter a good number of people for a party.")
    #       make sure no ZeroDivisionError occurs.
    num_each = cookies // people
    leftovers = cookies % people

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")


# In[ ]:


#18: Reading & Writing Files - Flying circus casr list
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)
    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)


# In[ ]:


#20: Practice Quiz - Debugging
user_list = []
list_sum = 0
raw_input_data = int(input("Enter number of data to add to the list: "))

# seek user input for ten numbers 
for i in range(0, raw_input_data):
   userInput = int(input())
   try:
       number = userInput
       user_list.append(number)
       if number % 2 == 0:
           list_sum += number
   except ValueError:
       print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


# In[ ]:


#24: Quiz -compute an exponent
# print e to the power of 3 using the math module
import math
e = math.e ** 3
print(e)


# In[ ]:


#24: Quiz - Password Generator
# TODO: First import the `random` module
import random

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# TODO: Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spaces

def generate_password():
   return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

# Now we test the function
print(generate_password())


# In[ ]:


# Write your code here

# HINT: create a dictionary from flowers.txt
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict
# HINT: create a function to ask for user's first and last name

def main(): 
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()
# print the desired output
   print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))


# In[ ]:




