# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

numbers_es = [00,11,22,33,44,55,66,77,88,99]

for number_es in numbers_es:
    if number_es == 7:
        break
    if number_es == 3:
        continue
    print(f"Current Number:{number_es}")

for i in range(5,len(numbers_es)):
    print(numbers_es[i])

# While loops execute a set of statements as long as a condition is true.
ct_es=0
while ct_es < 10:
    print(f"count:{ct_es}")
    ct_es+=1