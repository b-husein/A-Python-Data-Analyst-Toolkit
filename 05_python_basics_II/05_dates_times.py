"""
- Python has a module called datetime that allows us to define a date, time or duration.
- We first need to import this module so that we can use the functions available in this
module for defining a date or time object, using the following statement: 

CODE: 

    import datetime

Now, let's use the methods that are part of this module to define various date/time objects.

"""
# 1. DATE OBJECT

""" 
    A date consisting of a day, month and year can be defined using the date method:

    #CODE:

        date=datetime.date(year=1999, month=1, day=1)

        print(date)

    #OUTPUT: 

        1999-01-01

    Note that all three arguments of the date method - day, month, year are mandatory, if we skip one, an error occurs.
"""

# 2. TIME OBJECT

""" 
    To define an object in Python that stores time, we use time method.

    #CODE:

        time=datetime.time(hour=12, minute=0, second=0, microsecond=0)
        print("midnight:" , time)

    #OUTPUT: 

        midnight: 00:00:00
"""

# 3. DATETIME OBJECT

""" 
    We can also define a datetime object consisting of both a date and a time, using the datetime method.
    For this method, the date arguments - day, month, and year - are mandatory, but the time argument (like 
    hour, minute etc.) can be skipped.

    #CODE: 

        datetime1 = datetime.datetime(year=1999, month=1, day=1, hour=12, minute=0, second=0, microsecond=0)

        print("1st January 1999 midnight:", datetime1)

    #OUTPUT: 

        1st January 1999 midnight: 1999-01-01 12:00:00
"""

# 4. TIMEDELTA OBJECT

""" 
    A timedelta object represents a specific duration of time, and is created using the timedelta method.

    Let us create a timedelta object that stores a period of 17 days;

    #CODE:

        timedelta1=datetime.timedelta(weeks=2, days=3)
        timedelta1

    #OUTPUT:
        
        datetime.timedelta(days=17)

    We can also add other arguments like seconds, minutes and hours while creating a timedelta object.
    A timedelta object can be added to an existing date or datetime object, but not a time object.

    Adding a duration (timedelta object) to a date object:

    #CODE: 

        #adding a duration to a date object is supported
        date1=datetime.date(year=1995, month=1, day=1)
        timedelta1=datetime.timedelta(weeks=2, days=3)
        date1+timedelta1

    #OUTPUT:

            datetime.date(1995, 1, 18)

    Adding a duration (timedelta object) to a datetime object:

    #CODE:

        #adding a duration to a datetime object is supported
        datetime1=datetime.datetime(year=1995, month=2, day=3)
        timedelta1=datetime.timedelta(weeks=2, days=3)
        datetime1+timedelta1

    #OUTPUT: 

        datetime.datetime(1995, 2, 20, 0, 0)

    Note - adding a duration to a time object leads to an error.

"""


    