
#MODULES IN PYTHON

''' 
- A module is a Python file with a .py extension. It can be thought of as a section of a physical library.
- Module contains sections that are related to one another.
- For example, the matplotlib module contains all functions related to plotting graphs. 
- A module can contain another module. The matplotlib module, for instance, contains a module called pyplot.

- A module can be imported using the import keyword, followed by the name of the module:

    # CODE:
    import matplotlib

- We can also import part of a module (a submodule or a function) using the from keyword. 
- Example with the cosine function from the math module:

    # CODE:
    from math import cos

- Creating and importing a customized module in Python requires the following steps:

    1. Type 'idle' in the search bar next to the start menu. Once the Python shell
    is open, create a new file by selecting: File -> New file.

    2. Create some functions with similar functionality. As an example, here, we are creating
    a simple module that creates two functions - sin_angle and cos_angle. These functions
    calculate the sin and cosine of an angle (given in degrees).

    # CODE: 
    import math
    def sin_angle(x):
        y=math.radians(x)  
        return math.sin(y)
    def cos_angle(x):
        y=math.radians(x)
        return math.cos(y)

    3. Save the file. This directory, where the file should be saved, is the same
    directory where Python runs. You can obtain the current working directory using
    the following code:

    # CODE: 
    import os 
    os.getcwd()

    4. Using the import statement, import and use the module you have just created.




'''