
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
    - The syntax


'''