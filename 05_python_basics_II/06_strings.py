
#WORKING WITH STRINGS

''' 
- A string is a sequence of one or more characters enclosed within quotes (both single and 
double quotes are acceptable). The data type for strings is str.

    #DEFINING A STRING

    CODE: 

        x = 'All that glitters is not gold'

        # or 

        x = "All that glitters is not gold."

'''
    # For multiline strings use triple quotes:

    #x = ''' Today is tuesday. 
        #Tomorrow is Wednesday.'''


''' 
    #STRING OPERATIONS
    
    Various functions can be used with strings, some of which are explained in the following:

        1. Finding the length of a string: The len function can be used to calculate the length
        of a string:

            CODE:

            len('Hello')

            OUTPUT: 5

        2. Accessing individual elements in a string:
            The individual characters in a string can be extracted using the indexing operator, [].

            CODE:

            x = 'Python'
            x[3]

            OUTPUT: 'h'

        3. Slicing a string: Slicing refers to the extraction of a postion or subset of an object (in this case, the object is a string).
            Slicing can also be used with other iterable objects like lists and tuples. The colon operator is used for slicing, with an 
            optional start, stop, and step index. Some examples of slicing are provided below:

            CODE: 

            x = 'Python'

            x[1:] #slice from second character (y) to the end (n)

            OUTPUT:

            'ython'      

            Some more examples:

            CODE: 

            x[:2] #first two characters. The starting index is assumed to be 0;

            OUTPUT: 

            'Py'

            CODE: 

            x[::-1] #reversing the string, the last character has an index -1

            OUTPUT: 

            'nohtyP'

        4. Justification: To add spaces to the right or left, or center the string, the rjust, ljust or center method is used.  
        The first argument passed to such a method is the length of the new string and the optional second argument is the 
        character to be used for padding. By default, spaces are used for padding.

            CODE: 

            '123'.rjust(5, "*")

            OUTPUT: 

            '**123'

        5. Changing the case: To change the case of the string, the upper or lower method is used:

            CODE: 

            'COLOR'.lower()

            OUTPUT:

            'color'

        6. Checking what a string contains:
            In order to check whether a string starts or ends with a given character, the startswith or endswith method is used.
        
            CODE: 

            'weather'.startswith('w')

            OUTPUT: True

        7. Removing whitespaces from a string:
            To remove spaces from a string, use the strip method (to remove spaces at both ends), rstrip (from the right end),
            or lstrip (from the left end).

            CODE:

            '           Hello.'.lstrip()

            OUTPUT: 'Hello'

        8. Examining the contents of a string:
            There are several methods to check what a string contains, like isalpha, isupper, isdigit, isalnum etc. 
            All these methods return 'True' only if all the characters in the string satisfy a given condition.

            CODE:
            
            '981'.isdigit() #to check for digits

            OUTPUT: True

            CODE:

            'Abc'.isupper() #Checks if all characters are in uppercase. Since all letters are not uppercase
                            the condition is not satisfied.

            OUTPUT: False

        9. Joining a list of strings:
            The join method combines a list of strings into one string. On the left-hand side of the join 
            method, we mention the delimiter in quotes to be used for joining the strings. On the right-hand
            side, we pass the list of individual strings. 

            CODE:

            ' '.join(['Python', 'is', 'easy', 'to', 'learn'])

            OUTPUT:

            'Python is easy to learn'

        10. Splitting a string:
            The split method does the opposite of what the join method does. It breaks down a string into a list
            of individual words and returns the list. If we just pass one word to this method, it returns a list
            containing just one word and does not split the string further. 

            CODE:

            'Python is easy to learn'.split()

            OUTPUT:

            ['Python', 'is', 'easy', 'to', 'learn']

'''



    