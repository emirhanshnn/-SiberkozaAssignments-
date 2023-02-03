# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_es = "Emirhan"
age_es = 21

print("Hello, my name is "+ name_es + " and I am "+ str(age_es))

# String Formatting

print("Hello, my name is {name} and I am {age}".format(name=name_es,age=age_es))
print(f"Hello, my name is {name_es} and I am {age_es}")

# String Methods

s_es = "kara kara kara GÖZLER ona BUNA bakıyor mu?"

print(s_es.capitalize()+"->1\n")

print(s_es.upper()+"->2\n")

print(s_es.lower()+"->3\n")

print(s_es.swapcase()+"->4\n")

print(f"{len(s_es)}\t\t\t\t\t  ->5\n")

print(s_es.replace("kara","ela")+"   ->6\n")

print(f"{s_es.count('k')} \t\t\t\t\t  ->7\n")

print(str(s_es.startswith("kar"))+" \t\t\t\t\t  ->8\n")

print(str(s_es.endswith("mu?"))+" \t\t\t\t\t  ->9\n")

print(str(s_es.split())+"->10\n") 

print(str(s_es.find('a',2))+" \t\t\t\t\t  ->11\n")

print(str(s_es.isalpha())+" \t\t\t\t\t  ->12\n")

print(str(s_es.isalnum())+" \t\t\t\t\t  ->13\n")

print(str(s_es.isnumeric())+" \t\t\t\t\t  ->14\n")