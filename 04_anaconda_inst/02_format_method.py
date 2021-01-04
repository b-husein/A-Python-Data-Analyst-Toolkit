""" 
- The format method can be used in conjunction with the print method 
- for embedding variables within a string.
- It uses curly braces as placeholders for variables that are passed
- as arguments to the method.

- Example on printing variables using the format method:

"""
weight = 4.5
name = "Simi"

print("The weight of {} is {}".format(name, weight))

#OUTPUT: The weight of Simi (name) is 4.5 (weight);

"""
- We can also specify the position of variables passed to the method.
- For example, we use the position "1" to refer to the second object in argument
- and position "0" to specify the first object in the argument list.
"""
#CODE
y = 'Jack'
x = 'Jill'

print("{1} and {0} went up the hill to fetch a pail of water".format(x, y))

#OUTPUT: Jack and Jill went up the hill to fetch a pail of water.

