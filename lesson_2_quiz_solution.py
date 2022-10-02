#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Quiz 6 - Booleans and Variable
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
# i.e 100/100 = 1 and 10% = 0.1

total_rainfallpercent = 1   
rainfallpercent_off = 0.1
remainder_rainfall_left = 1 - 0.1
rainfall *= remainder_rainfall_left

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
# i.e 100/100 = 1 and 10% = 0.1

total_reservoirvolumepercent = 1  
reservoirpercent_added = 0.05
added_reservoir_volume = 1 + 0.05
reservoir_volume *= added_reservoir_volume

# decrease reservoir_volume by 5% to account for evaporation
decreased_reservoir_volume  = 1 - 0.05
reservoir_volume *= decreased_reservoir_volume

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)


# In[1]:


#Quiz 11 -Booleans comparison operator and Logical operators
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
total_pop_density = san_francisco_pop_density + rio_de_janeiro_pop_density

is_denser = rio_de_janeiro_pop_density < san_francisco_pop_density > total_pop_density
print(is_denser)


# In[2]:


#14: String
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

server_log_message = "Kinari accessed the site http://petshop.com/pets/mammals/cats at 04:50."
print(server_log_message)


# In[3]:


#Quiz 17: Type and Conversion
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
mon_sales = 121
tues_sales = 105
wed_sales = 110
thurs_sales = 98
fri_sales = 95
total_sales = mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales
 
print("This week's total sales: " + str(total_sales))


# In[4]:


#22: String Methods And Practice
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

print('')
#Q1:Solution
print("The total length of the verse is:",len(verse))

#Q2:Solution
result = verse.find('and')
print("Substring 'and' first occurence found at: " + str(result) + "th index.")

#Q3: Solution
result_you = verse.rfind('you')
print("Substring 'you' last occurence found at: " + str(result_you) + "th index.")

#Q4: Solution
count_you = verse.count('you')
print("The count of the word 'you' in the verse is: " + str(count_you) + " times ")


# In[ ]:




