# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
numbers_es = (1,2,3,4,5)

# Single value needs trailing comma
numbers = (1,)

# Get value
print("\n\n"+str(numbers_es[1])+"\n\n")
del numbers,numbers_es


# A Set is a collection which is unordered and unindexed. No duplicate members.
meyve_es = {"elma", "armut", "muz"}
print(meyve_es)
print('elma' in meyve_es)
print(len(meyve_es))

#add
meyve_es.add('üzüm')
print(meyve_es)

#remove
meyve_es.remove('üzüm')
print(meyve_es)

#clear
meyve_es.clear()
print(meyve_es)