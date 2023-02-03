# If/ Else conditions are used to decide to do something based on something being true or false
x_es = 10
y_es = 10
z_es = 50

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
if x_es>y_es:
    print("x>y")
elif y_es>x_es:
    print("y>x")
else:
    print("x=y")

# Logical operators (and, or, not) - Used to combine conditional statements
if (x_es == y_es and z_es>x_es) or z_es>y_es:
    print(not(True))



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_es=[1,2,3,4,5]
if 3 in numbers_es:
    print(True)
if 7 not in numbers_es:
    print(True)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x_es is y_es:
    print(True)