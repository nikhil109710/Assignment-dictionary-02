#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Create a dictionary 
my_dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}
file_name = 'dictionary.json'
store_dictionary_as_json(my_dictionary, file_name)


# In[5]:


import json

def store_dictionary_as_json(dictionary, filename):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)


# In[7]:


# Creating a dictionary
my_dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}
file_name = 'dictionary.json'
store_dictionary_as_json(my_dictionary, file_name)


# In[17]:


def match_key_values(dict1, dict2):
    matching_keys = []
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            matching_keys.append(key)
    return matching_keys


# In[18]:


# Matching and printing the matched keys
dictionary1 = {'name': 'Ramesh', 'age': 26, 'city': 'Bhopal'}
dictionary2 = {'name': 'Rakesh', 'age': 26, 'city': 'Pune'}
matched_keys = match_key_values(dictionary1, dictionary2)
print("Matching keys:", matched_keys)


# In[21]:


def replace_with_average(dictionary):
    values = list(dictionary.values())
    average = sum(values) / len(values)
    for key in dictionary:
        dictionary[key] = average
    return dictionary


# In[22]:


# Replacing dictionary values with their values
my_dictionary = {'A': 10, 'B': 20, 'C': 30}
updated_dictionary = replace_with_average(my_dictionary)
print("Updated dictionary:", updated_dictionary)


# In[23]:


def get_top_three_items(shop):
    sorted_items = sorted(shop.items(), key=lambda x: x[1], reverse=True)
    top_three = sorted_items[:3]
    return top_three


# In[24]:


# Getting top three items 
shop_items = {'item1': 10, 'item2': 30, 'item3': 20, 'item4': 5, 'item5': 15}
top_items = get_top_three_items(shop_items)
print("Top three items:", top_items)


# In[25]:


def create_dictionary_from_string(string):
    dictionary = {}
    for char in string:
        if char.isalpha():
            dictionary[char] = dictionary.get(char, 0) + 1
    return dictionary


# In[26]:


# Creating a dictionary from a string
input_string = "Hello, World!"
result_dict = create_dictionary_from_string(input_string)
print("Dictionary:", result_dict)


# In[27]:


def find_highest_three_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    highest_three = sorted_items[:3]
    return highest_three


# In[28]:


# Finding the highest 3 values of corresponding keys in a dictionary
my_dictionary = {'A': 10, 'B': 30, 'C': 20, 'D': 5, 'E': 15}
highest_values = find_highest_three_values(my_dictionary)
print("Highest three values:", highest_values)


# In[29]:


import itertools

def display_letter_combinations(dictionary):
    keys = list(dictionary.keys())
    combinations = list(itertools.product(*(dictionary[key] for key in keys)))
    for combination in combinations:
        print(''.join(combination))


# In[30]:


# creating and displaying all combinations of letters,selecting each letter from a different key in a dictionary
my_dictionary = {'key1': 'ABC', 'key2': 'DEF', 'key3': 'GHI'}
display_letter_combinations(my_dictionary)


# In[31]:


def print_unique_values(dictionary):
    unique_values = set(dictionary.values())
    for value in unique_values:
        print(value)


# In[32]:


# Printing all unique values in a dictionary
my_dictionary = {'A': 10, 'B': 20, 'C': 10, 'D': 30, 'E': 20}
print("Unique values:")
print_unique_values(my_dictionary)


# In[33]:


def combine_dictionaries(dict1, dict2):
    combined_dict = dict1.copy()
    for key in dict2:
        if key in combined_dict:
            combined_dict[key] += dict2[key]
        else:
            combined_dict[key] = dict2[key]
    return combined_dict


# In[35]:


# Combining two dictionaries and adding the values of the same keys
dictionary1 = {'A': 10, 'B': 20, 'C': 30}
dictionary2 = {'B': 5, 'C': 15, 'D': 25}
combined_dictionary = combine_dictionaries(dictionary1, dictionary2)
print("Combined dictionary:", combined_dictionary)


# In[36]:


def is_dictionary_empty(dictionary):
    if dictionary:
        return False
    else:
        return True


# In[37]:


# Checking if the dictionary if empty or not
empty_dict = {}
non_empty_dict = {'A': 10, 'B': 20, 'C': 30}
print("Is empty_dict empty?", is_dictionary_empty(empty_dict))
print("Is non_empty_dict empty?", is_dictionary_empty(non_empty_dict))


# In[ ]:




