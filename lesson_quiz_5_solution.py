#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Quiz 3: Population Density
# write your function here
def population_density(population, land_area):
     return population / land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


# In[2]:


#Quiz 3:readable_timedelta
# write your function here
# use integer division to get the number of weeks
def readable_timedelta(days):
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))


# In[3]:


#Quiz 11:write a doc string.
def readable_timedelta(days):
    # insert your docstring here
    """This  is to calculate how many week and day in the function readable_timedelta above """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


# In[4]:


#Quiz 14: lambda Expression
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)


# In[5]:


#Quiz 14: lambda Expression with filter
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)


# In[6]:


#Quiz 17: Iterators and Generators.
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


# In[7]:


#Quiz 17: Chunker-Method.
def chunker(iterable, size):
    # Implement function here
    """calcualtes successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]
        
for chunk in chunker(range(25), 4):
    print(list(chunk))


# In[ ]:




