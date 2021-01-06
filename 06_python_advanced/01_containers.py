
# EXPLORING CONTAINERS, CLASSES and OBJECTS

''' 
- Previously we talked about variables that can have a data type like int, float and str;
- but variable holds only a sinlge value. 
- Containers are objects that can contain multiple values. These values can have the same or different data types.
- The four built-in containers in Python are:

    1. Lists
    2. Tuples
    3. Dictionaries
    4. Sets

- Containers are also called iterables; That is, you can visit or traverse through each of the values in a given container object.
'''

# 1. LISTS

''' 
- A list contains a set of values that are stored in sequential order. 
- A list is mutable which means that we can modify, add or delete values in a list, making it a flexible container.
- An individual list item can be accessed using an index, which is an integer mentioned in square brackets
- indicating the position of the item. The indexing for a list starts from 0; (zero based)

- How to define and manipulate a list:

    - Defining a list
    - A list can be defined by giving it a name and a set of values that are enclosed within square brackets.

    #CODE:

    colors=['violet', 'indigo', 'red', 'blue', 'green', 'yellow']

    - ADDING ITEMS TO A LIST:
    - Different methods can be used to add values to a list. For example:

        * Append method
        - Adds one item at the end of the list. 
        - The method takes only a single value as an argument.

            #CODE:
            colors.append('white')
            #the value of 'white' is added after the last item in the 'colors' list.

        * Insert method
        - Adds one item at a given location or index.
        - This method takes two arguments - the index and the value to be added.

            #CODE:
            colors.insert(3, 'pink')
            #the value 'pink' is added at the fourth position in the 'colors' list.
        
        * Extend method
        - Adds multiple elements (as a list) at the end of a given list. 
        - This method takes another list as an argument.

            #CODE:
            colors.extend(['purple', 'magenta'])
            #values 'purple' and 'magenta' added at the end of the 'colors' list.


    - REMOVING ELEMENTS FROM A LIST:
    - 




'''