
# CREATING NEW LISTS FROM EXISTING LISTS

''' 
- There are three methods for creating a new list from an existing list
- list comprehensions, the map function, filter function

    1. LIST COMPREHENSIONS
    - They provide a shorthand and intuitive way of creating a new list from an existing list.
    - for example, we can create a new list ('colors1') from the list ('colors') we created earlier.
    - This list only contains only those items from the original list that contain the letter 'e'.
'''

''' 
        #CODE

        colors=['violet', 'indigo', 'red', 'blue', 'green', 'yellow']        
        colors1=[color for color in colors if 'e' in color]
        colors1

        #OUTPUT
        ['violet', 'red', 'blue', 'green', 'yellow']

    - THE STRUCTURE OF A LIST COMPREHENSION; 
    - colors1 -> new list
    - color -> output expression
    - colors -> original list
    - in -> optional condition

    - The output expression ('color') for items in the new list comes first.
    - Next comes a for loop to iterate through the original list 
    - note that other loops like the while loop are not used for iteration in a list comprehension
    - finally you can add an optional condition using the if/else statement.

    - the critical point to keep in mind while using list comprehensions is that 
    - readability of the code should not be compromised.
    - if there are too many conditional expressions and loops involved in creating a new list
    - it is better to avoid list comprehensions.

'''

''' 
    2. MAP FUNCTION
    - The map function is used to create a new list by applying a user defined
    - or inbuilt function on an existing list. The map function returns 
    - a map object and we need to apply the list function to convert it to a list.

    - The map function accepts two arguments:
        - The function to be applied
        - The list on which the function is to be applied

    - for example: we are creating a new list ('colors1') from the 'colors' list
    - converting its elements to uppercase. An anonymous (lambda) function is used
    - which is followed by the name of the original list.

        #CODE
        colors=['violet', 'indigo', 'red', 'blue', 'green', 'yellow']
        colors1=map(lambda x:x.upper(), colors)
        colors1

        #OUTPUT
        <map at 0x2dc87148630>

    - The function returns a map object, and the list function needs to be used to convert it to a list.

        #CODE
        list(colors1)

        #OUTPUT
        ['VIOLET', 'INDIGO', 'RED', 'BLUE', 'GREEN', 'YELLOW',]
'''

''' 
    3. FILTER FUNCTION
    - The syntax of the filter function is similar to that of the map function.
    - Whereas the map function returns all the objects in the original list after the function is applied
    - the filter function returns only those items that satisfy the condition specified
    - when the filter function is called
    - Similar to map function, we pass two arguments (a lambda function or a user defined function)
    - followed by the name of the list.

    - In the following example, we are creating a list from the original list, keeping only 
    - those items that have less than five characters

        #CODE
        colors2=filter(lambda x:len(x)<5, colors)
        list(colors)

        #OUTPUT
        ['red', 'green']

    - Now let's see how can we iterate through two or more lists simultaneously.
'''

''' 
    4. ITERATING THROUGH MULTIPLE LISTS USING THE ZIP FUNCTION
    - The zip function provides a way of combining lists and performing operations jointly
    - on these lists, as shown in the following example. The lists that need to be combined
    - are passed as arguments to the list function.

        #CODE
        #zip functions and lists
        colors=['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red',]
        color_ids=[1, 2, 3, 4, 5, 6, 7]
        for i,j in zip(colors, color_ids):
            print(i, "has a serial number", j)

        #OUTPUT
        Violet has a serial number 1
        Indigo has a serial number 2
        Blue has a serial number 3
        Green has a serial number 4
        Yellow has a serial number 5
        Orange has a serial number 6
        Red has a serial number 7

    - The zip function returns a slit of tuples that are stored in an object of type 'zip'. 
    - The type of this object needs to be changed to the list type to view the tuples.

        #CODE
        list(zip(colors, color_ids))

        #OUTPUT
        [   ('Violet', 1),
            ('Indigo', 2) etc.
        ]

    - The next function - enumerate, helps us access the indexes of the items in the list.
'''

''' 
    5. ACCESSING THE INDEX OF ITEMS IN A LIST
    - The enumare function is useful when you want to access the object as well as its index in a given list.
    - This function returns a series of tuples, with each tuple containing the item and its index.

        #CODE
        colors=['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red',]
        for index, item in enumerate(colors):
            print(item, "occurs at index", index)

        #OUTPUT
        Violet occurs at index 0
        Indigo occurs at index 1
        Blue occurs at index 2
        Green occurs at index 3
        Yellow occurs at index 4
        Orange occurs at index 5
        Red occurs at index 6
'''

''' 
    6. CONCATENATING OF LISTS
    - The concatenation of lists, where we combine two or more lists, can be done using the '+' operator.

        #CODE
        x=[1, 2, 3]
        y=[3, 4, 5]
        x+y

        #OUTPUT
        [1, 2, 3, 4, 5]

    - We can concatenate any number of lists. Note that concatenation does not modify any of 
    - the lists being joined. The result of the concatenation operation is stored in a new object.

    - The extend method can also be used for the concatenation of lists. Unlike the '+' operator
    - the extend method changes the original list.

        #CODE
        x.extend(y)
        x

        #OUTPUT
        [1, 2, 3, 4, 5]

    - Other arithmetic operators like -, *, or /, cannot be used to combine lists.
    
    - To find the difference of elements in two lists containing numbers, we use 
    - list comprehension and the zip function, for example:

        #CODE
        x=[1, 2, 3]
        y=[3, 4, 5]
        d=[i-j for i,j in zip(x,y)]
        d

        #OUTPUT
        [-2, -2, -2]


'''