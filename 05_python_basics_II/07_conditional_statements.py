
# Conditional statements as the name indicates evaluate a condition or a group of conditions.

''' 

    In Python, the if-elif-else construct is used for this purpose. Python does not have the 
    the switch-case construct, which is used in some other languages for conditional execution.

    Conditional statements start with the if keyword, and the expression or a condition to be 
    evaluated. This is followed by a block of code that executes only if the condition evaluates
    to 'True'; otherwise it's skipped.

    The else statement (which does not contain any condition) is used to execute a block of code
    when the condition mentioned in the if statement is not satisfied. 
    
    The elif statements are used to evaluate specific conditions. The order of elif statement matters. 
    If one of the elif statements evaluatesto True, the elif statements following it are not executed
    at all. 

    The if statement can also exist on its own, without mentioning the else or elif statements.

        #CODE

        #if-elif-else
            color = input('Enter one of te following colors - red, orange or blue: ')
            if color == 'red':
                print('Your favorite color is red')
            elif color == 'orange':
                print('Your favorite color is orange')
            elif color == 'blue':
                print('Your favorite color is blue')
            else:
                print('You have entered the wrong color.')

        #OUTPUT:

            Enter one of te following colors - red, orange or blue:
            You've entered the wrong color.
    
    Conditional statements can be nested, which means that we can have the one conditional statement
    (inner) within another (outer). You need to be particularly careful with indentation while using
    nested statements. An example of nested if statements is shown in the following:

        #CODE: 

        #nested conditionals
        x = 20
        if x < 10: 
            if x < 5:
                print('Number less than 5')
            else:
                print('Number greater than 10')
        
        Output:

        Number greater than 10

'''

''' 
    LOOPS - are used to execute a portion of the code repeatedly. A single execution of a block of code
    is called an iteration, and loops often go through multiple rounds of iteration. There are two types
    of loops that are used in Python - the for loop and the while loop.

    1. WHILE LOOP - used when we want to execute particular instructions as long as a condition is 'True'. 
        After the block of code executes, the execution goes back to the beginning of the block. 

        #CODE:

        #while loop with continue statement: 

        while True:
            x = input('Enter the correct color:')
                if(x!='red'):
                    print('Color needs to be entered as red.')
                    continue
                else:
                    break

        #OUTPUT: 

        Enter the correct color: Blue
        Color needs to be entered as red.
        Enter the correct color: yellow
        Color needs to be entered as red.
        Enter the correct color: red

    The break statement is used to take the control outside the loop. It is useful when we have an 
    infinite loop that we want to break out of.

    The continue statement does the opposite - it takes control to the beginning of the loop. The 
    keywords break and continue can be used both with loops and conditional statements, like if/else.

    2. FOR LOOP is used to execute a block of code a predetermined number of times. The for loop 
    can be used with any kind of iterable object, that is, a sequence of values that can be used 
    by a loop for running repeated instances or iterations. These iterable objects include lists,
    tuples, dictionaries and strings. 

    The foor loop is also used commonly in conjuction with the range function. The range function 
    creates a range object, another iterable, which is a sequence of evenly spaced integers. Consider
    the following example where we calculate the sum of the first five odd integers using a for loop.

        #CODE:

        #for loop
        sum=0
        for i in range(1, 10, 2):
            sum=sum+i
        
        print(sum)

        #OUTPUT: 25

        The range function has three arguments: the start argument, the stop argument, and 
        the step argument. None of these three arguments are mandatory. Numbers from 0 to 9
        (both 0 and 9 included) can be generated as range(10), range(0, 10), or range(0, 10, 1).

        The default start argument is 0, and the default step argument is 1.

        For loops can also be nested (with an outer loop and any number of inner loops), as shown
        in the following:

        #CODE: 

        #nested for loop

        for i in 'abcd':
            for j in range(4):
                print(i, end=" ")
            print("\n")

        #OUTPUT

        a a a a
        b b b b
        c c c c
        d d d d
'''

