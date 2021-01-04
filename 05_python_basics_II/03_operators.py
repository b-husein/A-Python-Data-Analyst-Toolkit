
# Some commonly used operators in Python

# 1. ARITHMETIC OPERATORS: Take two integer or float values, perform an operation and return a value.

""" 
- The following arithmetic operators are supported in Python: 
    - ** (Exponent)
    - % (modulo or remainder)
    - // (quotient)
    - * (multiplication)
    - - (subtraction)
    - + (addition)

"""

# The order of the operation is basically simple math.
"""
- For example, in the preceding expression, the operation inside the parenthesis
- is performed first, which gives 10, followed by division, which gives 5,
- and then subtraction which gives the final output 2; 
"""

#CODE

(1+9)/2-3

#OUTPUT: 2

# 2. COMPARISON OPERATORS: These operators compare two values and evaluate to a true or false.

""" 
- The following comparison operators are supported in Python: 
    - >: Greater than
    - <: less than
    - <=: less than or equal to
    - >=: greater than or equal to
    - ==: equality, which is different from the assignment operator (=)
    - !=: not equal to.

"""

# 3. LOGICAL OR BOOLEAN OPERATORS: Are similar to comparison operators in that they also evaluate to a true or false value. 
# They operate on boolean variables or expressions. We can use following logical operators:

"""
    - and operator: An expression in which this operator is used evaluates to True only if all of its subexpressions are True.
    otherwise, if any of them is False, the expression evaluates to False; example:
        CODE:
        (2 > 1) and (1 > 3)

        OUTPUT: False, because 1 > 3 is false.

    - or operator: An expression in which the or operator is used, evaluates to True if any of the subexpressions within
    the expression is true. The expression evaluates to False if all its subexpressions are false.
        CODE:
        (2 > 1) or (1 > 3)

        OUTPUT: True, because 2 > 1;
    
    - not operator: An expression in which the not operator is used, evaluates to True if the expression is False, and vice versa.
        CODE: 
        not(1 > 2)

        OUTPUT: True.
"""

# 4. ASSIGNMENT OPERATORS: These operators assign a value to a variable or an operand. 
# The following is the list of assignment operators used in Python: 

""" 
    - = (assigns a value to a variable)
    - += (adds the value on the right to the operand on the left)
    - -= (subtracts the value on the right from the operand on the left)
    - *= (multiplies the operand on the left by the value on the right)
    - %= (returns the remainder after dividing the operand on the left by the value on the right)
    - /= (returns the quotient, after dividing the operand on the left by the value on the right)
    - //= (returns only the integer part of the quotient after dividing the operand on the left by the value on the right)

Examples: 

x=5 #assigns the value 5 to the variable x; 
x+=1 #statement adds 1 to x (equivalent to x=x+1)
x-=1 #statement subtracts 1 from x (equivalent to x=x-1)
x*=2 #multiplies x by 2 (equivalent to x=x*2)
x%=3 #equivalent to x=x%3, returns remainder
x/=3 #equivalent to x=x/3, returns both integer and decimal part of quotient.
x//=3 $equivalent to x=x//3, returns only the integer part of quotient after dividing x by 3; 

"""

# 5. IDENTIFY OPERATORS (is and not is)

""" 
- These operators check for the equality of two objects, that is, whether the two objects point to the same 
    value and return a Boolean value (True/False) depending on whether they are equal or not. In the following
    example, the three variables 'x', 'y' and 'z' contain the same value, and hence, the identity operator (is)
    returns True when 'x' and 'z' are compared.

    x = 3
    y = x
    z = y
    x is z

    OUTPUT: True.
"""

# 6. MEMBERSHIP OPERATORS (in and not in)

""" 
- These operators check if a particular value is present in a string or a container (like lists and tuples). 
- The in operator returns 'True' if the value is present, and the not in operator returns 'True' if the value
- is not present in the string or container.

CODE: 
    'a' in 'and'

OUTPUT: True

"""
