
# WORKING FITH FILES AND READING FROM A FILE

''' 
- We can use methods or functions in Python to read or write to files. 
- In other words we can create a file, add content or text to it, and read
- its contents by using the methods provided by Python.

- Now we will see how can we read and write to comma-separated value (CSV) files.
- CSV files or comma-separated files are text files that are a text version of an Excel spreadsheet.

- The functions for all of these operations are defined under the CSV module. This module has to be
- imported first, using the import csv statement, to use its various methods.

'''

# READING FROM A FILE

''' 
- Reading from a file from Python involves the following steps:

    1. Using the with open statement, we can open an existing CSV file and 
    assign the resulting file object to a variable or file handle (named 'f' in
    the following example). Bite that we need to specify the path of the file using
    either the absolute or relative path. After this, we need to specify the mode
    for opening the file. For reading, the mode is 'r'. The file is opened for reading
    by default if we do not specify a mode.

    2. Following this, there is a block of code that starts with storing the contents
    of the file in a read object, using the csv.reader function where we specify the 
    file handle, f, as an argument.

    3. However, the contents of this file are not directly accessible through this read
    object. We create and empty list (named 'contents' in the following example), and
    then we loop through the read object we created in step 2 line by line using a for loop
    and append it to the list. This list can then be printed to view the lines of the CSV
    file we created.

        #CODE

        #Reading from a file
        import csv
        with open('animals.csv') as f:
            contents=csv.reader(f)
            lines_of_file=[]
            for line in contents:
                lines_of_file+=line
        lines_of_file
'''

# WRITING TO A FILE

''' 
- Writing to a file involves following steps: 

    1. Using the open function, open an existing CSV file or if the file does
    not exist, the open function creates a new file. Pass the name of the file
    (with absolute path) in quotes and specify the mode as 'w', if you want to
    overwrite the contents or write into a new file.
    Use the 'a' or 'append' mode if you simply want to append some lines to an
    existing file. Since we do not want to overwrite in this case, we open the 
    file using the append ('a') mode. Store it in a variable or file handle and
    give it a name, let us say 'f'.

    2. Using the csv.writer() function, create a writer object to add the content
    since we cannot directly write to the CSV file. Pass the variable (file handle),
    'f', as an argument to this function.

    3. Invoke the writerow method on the writer object created in the previous step.
    The argument to be passed to this method is the new line to be added (as a list).

    4. Open the CSV file on your system to see if the changes have been reflected.

        #CODE

        #writing to a file
        with open(r'animals.csv',"w") as f:
            writer_object=csv.writer(f, delimiter=",")
            writer_object.writerow(['sheep', 'lamb'])

    The modes that can be used with the open function to open a file are:

        - "r": opens a file for only reading
        - "w": opens a file for only writing. It overwrites the file if it already exists.
        - "a": opens a file for writing at the end of the file. It retains the original file
        contents.
        - "w+": opens the file for both reading and writing.

'''