# Python Test - November


# Question 1:
# Which of the following data structures in Python is mutable?
# B. List



# Question 2:
# What method is used to add an element to the end of a list in Python?
# C. append()



# Question 3:
# In Python, what is the primary purpose of the clear() method for a dictionary?
# B. Remove all key-value pairs



# Question 4:
# True or False: A set in Python can contain duplicate elements.
# B. False



# Question 5:
# What does the pop() method do for a list in Python?
# D. Removes all elements



# Question 6:
# Which of the following is a valid way to create an empty dictionary in Python?
# B. my_dict = dict()



# Question 7:
# What does the update() method do for a dictionary in Python?
# A. Adds a new key-value pair
# B. Updates an existing key's value



# Question 8:
# True or False: Lists in Python can be used as values in a dictionary.
# A. True



# Question 9:
# What is the purpose of the intersection() method for sets in Python?
# B. Returns the common elements between two sets



# Question 10:
# What is the output of the following code snippet?
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4])
# A. [2, 3, 4]

# Question 11:
# Describe a scenario where using a Python set would be more appropriate than using a list. 

# 1
# Қайталанады
# the_list = [1 ,  2 , 6 , 5 , 3 , 8 , 6 , 3 , 2 , 1]
# print(the_list)

# Қайталанбайды
# the_set = {1 ,  2 , 6 , 5 , 3 , 8 , 6 , 3 , 2 , 1}
# print(the_set)

# 2
# the_list = [6 ,  5 , 2 , 10 , 1 , 3 , 4 , 9 , 8 , 7 , 10]
# print(the_list)

# # по порядку
# the_set = {6 ,  5 , 2 , 10 , 1 , 3 , 4 , 9 , 8 , 7 , 10}
# print(the_set)



# Question 12:
# Explain the concept of indexing in Python lists. Provide an example to demonstrate how indexing is used to access elements in a list.

# languages = ['C#' , 'C++' , 'Java' , 'Kotlin' , 'Ruby' , 'Python']
# print(languages[-4::])
# print(languages[::-1])
# print(languages[-1::])
# print(languages[3])
# print(languages[1:4])
# print(languages[0:6:2])



# Question 13: 

# You are given a list of integers. Write a Python program that finds and prints the sum of all even numbers in the list.

# my_list =  [1, 2, 3, 4, 5, 6]
# for i in my_list:
#     if i % 2 == 0:
#         sum = i + i
# print(f'Sum of all even numbers:{sum}')



# Question 14:

# You have two dictionaries representing the quantities of items in stock. Write a Python program that updates the first dictionary with the quantities from the second dictionary and prints the updated dictionary.

# # Example:
# fruits = {'apple': 5, 'banana': 3}, {'banana': 2, 'orange': 4}
# print(fruits)


# Output: {'apple': 5, 'banana': 5, 'orange': 4}



# Question 15:

# Given a list of strings, write a Python program that filters out and prints only the strings that start with the letter 'l'.

# fruits =  ['lychee', 'apple', 'banana', 'lemon' , 'orange', 'grape', 'lime']
# for i in fruits:
#         if i.startswith('l'):
#             print(i , end=', ')

# # Output: [‘lychee’, 'lemon', 'lime']
