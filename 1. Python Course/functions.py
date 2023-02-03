# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
def sayhello(name=" "):
    print(f"Hello {name}")
sayhello("Emirhan")

#Return value
def getsum(x,y):
    return x+y;
print(getsum(1,2))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getmult = lambda a,b : a*b
print(getmult(2,4))