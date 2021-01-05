
#Python Enhancement Proposal (PEP) 8 - standards for writing code;

'''  
- PEP is a technical document that provides documentation for new features introduced in Python language.
- There are many types of PEP documents, the most important among these being PEP 8;
- The PEP 8 document provides style guidelines for writing code in Python. T
- The main emphasis of PEP 8 is on providing a set of consistent rules that enhance code readability.

- There are several guidelines in PEP 8 for different aspects of the code, some of which are summarized here:

    1. INDENTATION: used to indicate the starting of a block of code. In Python, four spaces are used
    for indentation. Tabs should be avoided for indentation.

    2. LINE LENGTH: The max. character length for a line of code is 79 characters. For comments
    the limit is 72 characters.

    3. THE NAMING CONVENTIONS - for naming different types of objects in Python are also laid out in PEP 8;
    Short names should be used, and underscores can be used to improve readablity. For naming functions, 
    methods, variables, modules, and packages, use the lowercase (all small letters) notation. With constants
    use the uppercase (all capitals) notation, and for classes, use the CapWords (two words each starting with
    a capital letter, not separated by spaces) notation for naming.

    4. COMMENTS - Block comments, starting with # and describing an entire block of code are recommended. 
    inline comments should be avoided.

    5. IMPORTS: While importing a module to use it in your code, avoid wildcard imports (using the * notation).

        #CODE: 

        from module import *

        Multiple packages or classes should not be imported on the same line.

        #CODE:

        import a, b

        They should be imported on separate lines as shown in the following.

        #CODE: 
        import a
        import b

        Absolute imports should be used as far as possible, for example:

        #CODE:

        import x.y

        Alternatively, we can use this notation from importing modules:
        
        #CODE: 

        from x import y

    6. ENCODING: The encoding format to be used for writing code in Python 3 is UTF-8;




'''