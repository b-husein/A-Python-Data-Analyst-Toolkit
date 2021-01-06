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
    - There are multiple ways of adding an item to a list, but there are also multiple ways to remove values from a list.
    - Each of the methods below can remove only a single item at a time:

        * Del
        - the del keyword deletes an item at a given location.

            #CODE: 
            del colors[1]
            #removes the second item of the 'colors' list

        * Remove 
        - This method is used when the name of the item to be removed is known, but not its position.

            #CODE:
            colors.remove('white')
            #removes the item 'white' from the 'colors' list

        * Pop
        - This method removes and returns the last item in the list.

            #CODE:
            colors.pop()
            #removes the last item and displays the item removed.

    - FINDING THE INDEX (LOCATION) OF AN OBJECT IN THE LIST
    - The index method is used to find out the location (or index) of a specific item or value in a list.

            #CODE
            colors.index('violet')

            #OUTPUT: 0

    - CALCULATING THE LENGTH OF A LIST
    - the len function returns the count of the number of items in a list.
    - The name of the list is passed as an argument to this function.
    - Note that len is a function, not a method.
    - A method can be used only with an object.

            #CODE
            len(colors)

            #OUTPUT: 7

    - SORTING A LIST
    - The sort method sorts the values in the list, in ascending or descending order. 
    - By default, this method sorts the item in the ascending order. If the list contains strings, the sorting 
    - is done in alphabetical order (using the first letter of each string), as shown in the following: 

            #CODE
            colors.sort()
            colors

            #OUTPUT:
            ['blue', 'green', 'purple', 'red', 'violet', 'white', 'yellow']

    - Note that the list must be homogeneous (all values in the list should be of the same data type) for the sort
    - method to work. If the list contains items of different data types, applying the sort method leads to an error.

    - If you want to sort your elements in the reverse alphabetical order, you need to add the reverse parameter
    - and set it to 'True'

        #CODE
        colors.sort(reverse=True)
        colors

        OUTPUT:
        ['yellow', 'white', 'violet', 'red', 'purple', 'green', 'blue']

    - Note if you want to just reverse the order of the items in a list, without sorting the items 
    - you can use the reverse method

        #CODE
        colors=['violet', 'indigo', 'red', 'blue', 'green', 'yellow']
        colors.reverse()
        colors

        #OUTPUT
        ['yellow', 'green', 'blue', 'red', 'indigo', 'violet',] 

    
    - SLICING A LIST
    - When we create a slice from a list, we create a subset of the original list by choosing specific values
    - from the list, based on their position or by using a condition. Slicing of a list works similar to 
    - slicing a string, which we studied previously.

    - To create a slice using an index, we use the colon operator ( : ) and specify the start and stop values
    - for the indexed that need to be selected.

    - If we provide no start or stop value before and after the colon, it is assumed that the start value
    - is the index of the first element (0), and stop value is the index of the last element.

        #CODE
        colors[:]

        #OUTPUT

        ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']

    - We can also use the colon operator twice if we are using a step index. 
    - In the following statement, alternate elements of the list are extracted by 
    - specifying a step index of two.

        #CODE
        colors[::2]

        #OUTPUT
        ['Violet', 'Blue', 'Yellow', 'Red']
        #every second one was sliced out

    - Just like strings, lists follow both positive and negative indexing. 
    - Negative indexing (starts from -1, which is te index of last element in the list) works from right to left
    - while positive indexing (starts from 0, which is the index of the first element in the list) works from left to right

    - an example of slicing with negative indexing, where we extract alternate elements starting from the last value in the list:

        #CODE
        colors[-1: -8: -2]

        #OUTPUT
        ['Red', 'Yellow', 'Blue', 'Violet']

'''