# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x_es = 6                         #int
y_es = 0.1                       #float
name_es = "Emirhan Şahin"        #str
is_empty_es = True               #bool
print(x_es, y_es, name_es, is_empty_es)

#Multiple assiggnment
x_es, y_es, name_es, is_empty_es = (15, 3.2, "Emir", False)
print(x_es, y_es, name_es, is_empty_es)

#Basic Math & Casting

a_es = x_es + y_es

print(f"{type(x_es)} + {type(y_es)} = {type(a_es)}")