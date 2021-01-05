
#FUNCTIONS

''' 
- A function can be thought of as a 'black box' because the user need not to be concerned with the internal workings of the function
- that takes an input, processes it, and produces an output. A function is essentially a block of statements performing a specific task.

- A function may have an optional return value. The utility of functions lies in their reusability. They also help in avoiding redundancy
- and organizing code into logical blocks. We just need to supply it with the set of inputs it needs to run the instructions.

- For example, say you want to find out the prime numbers in a given list of numbers. Once you have written a function for 
- checking whether an integer is a prime number, you can simply pass each number in the list as an argument to the function
- and call it, instead of writing the same lines of code for each integer you want to test.

    #CODE:

    def checkPrime(i):
        #Assume the number is prime initially
        isPrime=True
        for j in range (2, i):
            #checking if the number is divisible by any number between 2 and i
            if i%2==0:
                #if it is divisible by any number in the j range, it is not prime
                isPrime=False
        #This is the same as writing if isPrime==True
        if isPrime:
            print(i, "is prime")
            else:
                print(i, "is not prime")
        for i in range(10, 20):
            checkPrime(i)

    #OUTPUT:

    10 is not prime
    11 is prime
    12 is not prime
    13 is prime
    14 is not prime
    (...)
    19 is prime

'''

#ANONYMOUS OR LAMBDA FUNCTIONS

''' 
- These functions are defined by using the lambda keyword. They are single-expression functions and provide
- a compact way of defining a function without binding the function object to a name. The reason these functions
- are called "anonymous" is that they do not need a name. Consider a following example where we use lambda function
- to calculate the sum of two numbers:

    #CODE:

    (lambda x, y:(x + y))(5, 4)

    #OUTPUT: 9

- The syntax of anonymous function: It starts with the lambda keyword, followed by parameters ('x' and 'y' in our case)
- then comes the colon ( : ) after which there is an expression (x + y) that is evaluated and returned. There is no need 
- to mention a return statement since there is an implicit return in such a function. Notice that the function also doesn't have a name.

'''

